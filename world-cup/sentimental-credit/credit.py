# TODO
from cs50 import get_int

nums = []

def main():
    num = get_int("Number: ")

    nums = [int(i) for i in str(num)]
    print(len(nums))
    print(isValid(nums))

    firsttwo = int(str(nums[0]) + str(nums[1]))

    if firsttwo == 34 or firsttwo == 37 and len(nums) == 15 and isValid(nums):
        print("AMEX")
    elif firsttwo == 51 or firsttwo == 52 or firsttwo == 53 or firsttwo == 54 or firsttwo == 55 and isValid(nums):
        if len(nums) == 16:
            print("MASTERCARD")
        else:
            print("INVALID")
    elif nums[0] == 4 and len(nums) == 13 or len(nums) == 16:
        if isValid(nums):
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")


def isValid(nums):
    reversed = nums[::-1]
    odd = reversed[1::2]
    not_odd = reversed[0::2]
    mlt = [item * 2 for item in odd]
    total = 0
    for i in mlt:
        if i > 9:
            splt = [int(i) for i in str(i)]
            total = total + splt[1] + splt[0]
        else:
            total += i
    for j in not_odd:
        total += j

    print(total)

    if total % 2 == 0 and str(total).endswith('0'):
        return True
    else:
        return False

main()