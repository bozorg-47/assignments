def factorail(n):
    if (n <= 1):
        return 1
    else:
        return n * factorail(n - 1)
print('factorail of 5 is', factorail(5))