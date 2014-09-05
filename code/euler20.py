def factorial(x):
    if x <= 1:
        return 1
    else:
        return x*factorial(x-1)

def sumDigits(num):
    return sum(map(int, str(num)))

print sumDigits(factorial(100))