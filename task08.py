def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum of numbers: {sum_numbers(1, 2, 3, 4, 5)}")