def factorial_calc(n):
    if n == 0:
        return 1
    return n * (factorial_calc(n - 1))

n = input("Enter a number: ")
print("Factorial of", n, "is", factorial_calc(int(n)))