def sum_divisible():
    total = 0
    for num in range(50, 101):
        if num % 3 == 0 and num % 5 != 0:
            total += num
    return total

print(f"Sum of numbers between 50 and 100 (divisible by 3, not 5): {sum_divisible()}")
