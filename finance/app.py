import os
import sys

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    balance = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    stocks = db.execute("SELECT stock_name, symbol, SUM(num_shares) as total FROM transactions WHERE transactions.user_id = ? GROUP BY stock_name", session["user_id"])
    total = db.execute("SELECT ROUND(SUM(price)) as grand_total FROM transactions WHERE transactions.user_id = ?", session["user_id"])
    print(total, file=sys.stderr)
    shares_c = db.execute("SELECT * FROM shares_count WHERE shares_count.user_id = ? ORDER BY id DESC", session["user_id"])
    lenght = True
    if len(shares_c) > 0:
        lenght = True
    else:
        lenght = False
    return render_template("index.html", balance=round(balance[0]["cash"]), stocks=stocks, lookup=lookup, total=total, shares_c=shares_c, lenght=lenght)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(float(request.form.get("shares")))
        print(symbol, file=sys.stderr)
        if not symbol:
            return apology("EMPTY")
        elif not shares:
            return apology("EMPTY")
        elif int(shares) < 1:
            return apology("SHARES MUST BE GREATER THAN 0 AND BE AN INTEGER")
        else:
            cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            company = lookup(symbol)
            if not company:
                return apology("INVALID SYMBOL")
            elif (int(shares) * company["price"]) > cash[0]["cash"]:
                return apology("NOT ENOUGHT MONEY")
            else:
                db.execute("UPDATE users SET cash = ? WHERE id = ?", cash[0]["cash"] - (int(shares) * company["price"]), session["user_id"])
                db.execute("INSERT INTO transactions (user_id, price, stock_name, num_shares, symbol, type) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], int(shares) * company["price"], company["name"], shares, symbol, 'B')
                symbols = db.execute("SELECT name, number FROM shares_count WHERE name = ? AND shares_count.user_id = ?", symbol, session["user_id"])

                if any(dictionary.get('name') == symbol for dictionary in symbols):
                    db.execute("UPDATE shares_count SET number = ? WHERE shares_count.user_id = ? AND name = ?", symbols[0]["number"] + int(shares), session["user_id"], symbol)
                else:
                    db.execute("INSERT INTO shares_count (name, number, user_id) VALUES (?, ?, ?)", symbol, shares, session["user_id"])

                return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    transactions = db.execute("SELECT * FROM transactions WHERE transactions.user_id = ?", session["user_id"])
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = lookup(request.form.get("symbol"))
        if not symbol:
            return apology("ENTER SYMBOL")
        return render_template("quoted.html", symbol=symbol, price=round(symbol["price"], 2))
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        password = request.form.get("password")
        username = request.form.get("username")
        users = db.execute("SELECT username FROM users")

        for user in users:
            if user["username"] == username:
                return apology("USERNAME IN USE")

        if not username:
            return apology("TRY AGAIN")

        elif not password:
            return apology("TRY AGAIN")

        elif not request.form.get("confirmation"):
            return apology("TRY AGAIN")

        elif not request.form.get("confirmation") == password:
            return apology("TRY AGAIN")

        else:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
            return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(float(request.form.get("shares")))
        company = lookup(symbol)
        available_shares = db.execute("SELECT number FROM shares_count WHERE name = ? AND shares_count.user_id = ?", symbol, session["user_id"])
        """ print(int(shares) - 1 == available_shares[0]["number"], file=sys.stderr) """

        if not symbol:
            return apology("EMPTY SYMBOL FIELD")
        elif int(shares) < 1:
            return apology("SHARES MUST BE GREATER THAN 0 AND BE AN INTEGER")
        elif not shares or int(shares) > int(available_shares[0]["number"]):
            return apology("EMPTY SHARES FIELD OR NOT ENOUGHT SHARES FROM THAT STOCK")
        else:
            if int(shares) == available_shares[0]["number"]:
                db.execute("DELETE FROM shares_count WHERE name = ? AND shares_count.user_id = ?", symbol, session["user_id"])
                user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
                db.execute("UPDATE users SET cash = ? WHERE id = ?", user[0]["cash"] + (int(shares) * company["price"]), session["user_id"])
                db.execute("INSERT INTO transactions (user_id, price, stock_name, num_shares, symbol, type) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], (int(shares) * company["price"]), company["name"], shares, symbol, 'S')
            else:
                db.execute("UPDATE shares_count SET number = ? WHERE shares_count.user_id = ? AND name = ?", int(available_shares[0]["number"]) - int(shares), session["user_id"], symbol)
                user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
                db.execute("UPDATE users SET cash = ? WHERE id = ?", user[0]["cash"] + (int(shares) * company["price"]), session["user_id"])
                db.execute("INSERT INTO transactions (user_id, price, stock_name, num_shares, symbol, type) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], (int(shares) * company["price"]), company["name"], shares, symbol, 'S')

        return redirect("/")

    else:
        symbols = db.execute("SELECT DISTINCT stock_name, symbol FROM transactions WHERE transactions.user_id = ?", session["user_id"])
        return render_template("sell.html", symbols=symbols)
