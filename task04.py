def second_highest(numbers):
    first, second = float('-inf'), float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

numbers = {10, 20, 30, 40, 50}
print(f"Second highest number: {second_highest(numbers)}")