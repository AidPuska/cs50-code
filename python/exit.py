import sys

if len(sys.argv) < 2:
    print("Missing comand-line argument")
    sys.exit(1)

print(sys.argv[1:])
sys.exit(0)