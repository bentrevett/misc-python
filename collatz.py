def collatz(n):
    print(int(n))
    if n == 1: return True
    elif n%2 == 0: return collatz(n/2)
    else: return collatz((3*n) + 1)

print("The Collatz conjecture involves taking a number n. If it is even, divide it by 2. If it is odd, multiply by 3 and add 1. Eventually you will always reach 1.\n")

while True:
    x = int(input("Pick a number: "))
    print("The Collatz response is: ")
    collatz(x)
