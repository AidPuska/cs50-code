from cs50 import get_int

scores = []

for i in range(3):
    n = get_int("Enter num: ")
    scores.append(n)

average = sum(scores) / len(scores)
print(f"Average is: {average:.02f}")