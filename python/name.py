from sys import exit

names = ['David', 'Charlie', 'Aid', 'Mike', 'Donny']

name = input("Enter name: ")

if name in names:
    print("Found name")
    exit(0)

print("Not found")
exit(1)