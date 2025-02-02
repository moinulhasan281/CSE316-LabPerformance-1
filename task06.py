def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    series = [0, 1]
    for _ in range(n - 2):
        series.append(series[-1] + series[-2])
    return series

n_terms = 10
print(f"Fibonacci series: {fibonacci(n_terms)}")