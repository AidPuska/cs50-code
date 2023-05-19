# TODO
from cs50 import get_int

n = 0

while n < 1 or n > 8:
    n = get_int("Height: ")

for i in range(n):
    for k in range(n - (i + 1)):
        print(" ", end="")
    for j in range(i + 1):
        print("#", end="")
    print(end="  ")
    for m in range(i + 1):
        print("#", end="")
    print()