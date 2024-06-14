from functools import reduce

# Lambda function with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# Lambda function with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Lambda function with reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)
