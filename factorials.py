def factorial_calc(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Factorial is not possible for negative numbers"
    elif type(n) != int:
        return "Factorial is not possible for non-integer numbers"
    return n * (factorial_calc(n - 1))

n = input("Enter a number: ")
print("Factorial of", n, "is", factorial_calc(int(n)))
