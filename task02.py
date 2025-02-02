def find_smallest(numbers):
    smallest = float('inf')
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

numbers = {4, 7, 1, 9, 12, 3}
print(f"Smallest number: {find_smallest(numbers)}")
