def sum_odd_even(numbers):
    odd_sum, even_sum = 0, 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return odd_sum, even_sum

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds, evens = sum_odd_even(numbers)
print(f"Sum of odd numbers: {odds}")
print(f"Sum of even numbers: {evens}")
