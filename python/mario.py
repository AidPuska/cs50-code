def main():
    height = get_height()

    for i in range(height):
        for j in range(i + 1):
            print("#", end="")
        print()
    print()


def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                return n
        except ValueError:
            print("Not a number")


main()