from cs50 import SQL

db = SQL("sqlite:///shows.db")

favorite = input("Enter movie name: ")

rows = db.execute("SELECT * FROM shows WHERE title = ?", favorite)

for row in rows:
    print(row)