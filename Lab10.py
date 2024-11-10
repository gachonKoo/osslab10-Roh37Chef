import sys

try:
    number = int(sys.argv[1])
except IndexError:
    number = int(input("Enter a number: "))

for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")

print()
