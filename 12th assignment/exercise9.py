def sum_multiples(n):
    total_sum = 0
    for i in range(n):
        if i %3 ==0 or i %5 == 0:
            total_sum += i
    return total_sum
n = 100
result = sum_multiples(n)
print(f"The sum of multiples of 3 and 5 less than {n} is :{result}")