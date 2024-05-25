# Python code demonstrating all types of loops:


For Loop: A loop that iterates over a sequence (like a list, tuple, dictionary, string, or range).

While Loop: A loop that continues to execute as long as the condition is true.

Nested Loops: Loops within loops.

Loop with Else: A loop with an else block that executes after the loop completes normally (without a break).


# For loop to iterate over a list
```
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(f"For loop, number: {number}")


```
# For loop to iterate over a dictionary
```
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"For loop, key: {key}, value: {value}")


```
# For loop to iterate over a string
```
message = "Hello"
for char in message:
    print(f"For loop, char: {char}")


```
# For loop with range
```
for i in range(5):
    print(f"For loop with range, i: {i}")


```
# While loop
```
count = 0
while count < 5:
    print(f"While loop, count: {count}")
    count += 1


```
# Nested loops
```
for i in range(3):
    for j in range(3):
        print(f"Nested loop, i: {i}, j: {j}")

```
# Loop with else
```
for i in range(3):
    print(f"Loop with else, i: {i}")
else:
    print("Loop with else completed")


```

# While loop with else
```
count = 0
while count < 3:
    print(f"While loop with else, count: {count}")
    count += 1
else:
    print("While loop with else completed")


```
# Break in a loop
```
for i in range(5):
    if i == 3:
        print(f"Break in loop, breaking at i: {i}")
        break
    print(f"Break in loop, i: {i}")


```
# Continue in a loop
```
for i in range(5):
    if i == 3:
        print(f"Continue in loop, continuing at i: {i}")
        continue
    print(f"Continue in loop, i: {i}")


```

# Loop over a list with indices
```
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Loop with enumerate, index: {index}, fruit: {fruit}")


```
# Loop with zip
```
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"Loop with zip, name: {name}, age: {age}")


```
# Infinite loop (commented out to prevent execution hang)
```
 while True:

print("Infinite loop")
```

# Nested loop with break
```
for i in range(3):
    for j in range(3):
        if j == 1:
            print(f"Nested loop with break, breaking inner loop at j: {j}")
            break
        print(f"Nested loop with break, i: {i}, j: {j}")


```
# Nested loop with continue
```
for i in range(3):
    for j in range(3):
        if j == 1:
            print(f"Nested loop with continue, continuing inner loop at j: {j}")
            continue
        print(f"Nested loop with continue, i: {i}, j: {j}")


```
# Loop with pass
```
for i in range(5):
    if i == 3:
        print(f"Loop with pass, pass at i: {i}")
        pass
    print(f"Loop with pass, i: {i}")


```

# Using loops to create a list (list comprehension)
```
squares = [x ** 2 for x in range(5)]
print(f"List comprehension, squares: {squares}")


```

# Using loops to create a dictionary (dictionary comprehension)
```
squares_dict = {x: x ** 2 for x in range(5)}
print(f"Dictionary comprehension, squares_dict: {squares_dict}")


```
# While loop with a break
```
count = 0
while True:
    print(f"While loop with break, count: {count}")
    count += 1
    if count == 3:
        break


```

# While loop with a continue
```
count = 0
while count < 5:
    count += 1
    if count == 3:
        print(f"While loop with continue, continuing at count: {count}")
        continue
    print(f"While loop with continue, count: {count}")


```
# Loop through a range in reverse
```
for i in reversed(range(5)):
    print(f"Loop in reverse, i: {i}")


```
# Nested loops to create a matrix
```
matrix = [[i * j for j in range(3)] for i in range(3)]
print(f"Nested loop for matrix: {matrix}")


```

# Loop with multiple conditions
```
for i in range(10):
    if i % 2 == 0 and i % 3 == 0:
        print(f"Loop with multiple conditions, i: {i}")


```
# Using a loop to flatten a list of lists
```
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = [item for sublist in list_of_lists for item in sublist]
print(f"Flattened list: {flattened_list}")


```
# Looping over two ranges simultaneously
```
for i, j in zip(range(3), range(10, 13)):
    print(f"Loop over two ranges, i: {i}, j: {j}")


```
# Loop with a set
```

unique_numbers = {1, 2, 3, 4, 5}
for number in unique_numbers:
    print(f"Loop with set, number: {number}")

```

# Loop with a tuple
```

tuple_values = (10, 20, 30)
for value in tuple_values:
    print(f"Loop with tuple, value: {value}")


```

# Loop with a boolean condition
```

i = 0
while i < 5:
    print(f"Loop with boolean condition, i: {i}")
    i += 1


```

# Nested loops with multiple levels
```

for i in range(2):
    for j in range(2):
        for k in range(2):
            print(f"Nested loops with multiple levels, i: {i}, j: {j}, k: {k}")


```

# Loop with a range step
```

for i in range(0, 10, 2):
    print(f"Loop with range step, i: {i}")


```

# Using a loop to create a set (set comprehension)
```

squares_set = {x ** 2 for x in range(5)}
print(f"Set comprehension, squares_set: {squares_set}")


```

# Using a loop to create a generator (generator comprehension)
```

squares_gen = (x ** 2 for x in range(5))
print(f"Generator comprehension, squares_gen: {list(squares_gen)}")


```

# Using a loop to filter a list
```

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Filtered list, even_numbers: {even_numbers}")


```

# Loop with try-except
```

for i in range(5):
    try:
        result = 10 / i
    except ZeroDivisionError:
        result = "undefined"
    print(f"Loop with try-except, i: {i}, result: {result}")


```

# Looping over multiple lists simultaneously
```

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"Loop over multiple lists, name: {name}, score: {score}")


```

# Loop with a countdown
```

for i in range(5, 0, -1):
    print(f"Countdown loop, i: {i}")


```

# Using a loop to check for prime numbers
```

for num in range(2, 10):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(f"Prime number found: {num}")


```

# Loop with a complex condition
```

for i in range(10):
    if i % 2 == 0 or i % 3 == 0:
        print(f"Loop with complex condition, i: {i}")


```

# Using a loop to find the maximum value in a list
```

numbers = [1, 3, 2, 8, 5, 10]
max_value = numbers[0]
for number in numbers:
    if number > max_value:
        max_value = number
print(f"Maximum value in list: {max_value}")


```

# Using a loop to reverse a string
```

original_string = "hello"
reversed_string = ""
for char in original_string:
    reversed_string = char + reversed_string
print(f"Reversed string: {reversed_string}")


```

# Loop with a nested function
```

def nested_function(x):
    return x ** 2

for i in range(5):
    result = nested_function(i)
    print(f"Loop with nested function, i: {i}, result: {result}")


```

# Loop with a map function
```

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(f"Loop with map function, squares: {squares}")


```

# Loop with a filter function
```

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Loop with filter function, even_numbers: {even_numbers}")


```

# Loop with a reduce function
```

from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(f"Loop with reduce function, sum_of_numbers: {sum_of_numbers}")


```

# Loop with enumerate and a start index
```

names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names, start=1):
    print(f"Loop with enumerate and start index, index: {index}, name: {name}")


```

# Loop with a custom iterator
```

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

for count in Countdown(5):
    print(f"Loop with custom iterator, count: {count}")


```


# Loop with a generator function
```

def countdown_generator(n):
    while n > 0:
        yield n
        n -= 1

for count in countdown_generator(5):
    print(f"Loop with generator function, count: {count}")


```

# Loop with a list of tuples
```

tuple_list = [(1, 2), (3, 4), (5, 6)]
for a, b in tuple_list:
    print(f"Loop with list of tuples, a: {a}, b: {b}")


```

# Loop to find the minimum value in a list
```

numbers = [1, 3, 2, 8, 5, 10]
min_value = numbers[0]
for number in numbers:
    if number < min_value:
        min_value = number
print(f"Minimum value in list: {min_value}")


```

# Loop to calculate the factorial of a number
```

n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n}: {factorial}")


```

# Loop to calculate the Fibonacci sequence
```

n = 10
a, b = 0, 1
fib_sequence = []
for _ in range(n):
    fib_sequence.append(a)
    a, b = b, a + b
print(f"Fibonacci sequence: {fib_sequence}")


```

# Loop with dictionary comprehension
```

squares_dict = {x: x ** 2 for x in range(5)}
print(f"Dictionary comprehension, squares_dict: {squares_dict}")

```


# Loop to remove duplicates from a list
```

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(f"List without duplicates: {unique_numbers}")


```

# Loop to transpose a matrix
```

matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = []
for i in range(len(matrix[0])):
    transposed_matrix.append([row[i] for row in matrix])
print(f"Transposed matrix: {transposed_matrix}")


```

# Loop with string formatting
```

names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"Person {index + 1}: {name}")


```

# Loop with a set comprehension
```

squares_set = {x ** 2 for x in range(5)}
print(f"Set comprehension, squares_set: {squares_set}")


```

# Loop with a generator expression
```

squares_gen = (x ** 2 for x in range(5))
print(f"Generator expression, squares_gen: {list(squares_gen)}")


```

# Loop with list slicing
```

numbers = [1, 2, 3, 4, 5]
for number in numbers[::-1]:
    print(f"Loop with list slicing, number: {number}")


```

# Loop with list slicing to reverse
```

numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]
print(f"Reversed list with slicing: {reversed_numbers}")


```


# Loop with a step size in range
```

for i in range(0, 10, 2):
    print(f"Loop with step size in range, i: {i}")
```


# Loop to merge two lists
```

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = []
for a, b in zip(list1, list2):
    merged_list.append(a)
    merged_list.append(b)
print(f"Merged list: {merged_list}")

```


# Loop to find common elements in two lists
```

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = [x for x in list1 if x in list2]
print(f"Common elements in two lists: {common_elements}")

```


# Loop to calculate the power of numbers
```

numbers = [1, 2, 3, 4, 5]
powers = [x ** 2 for x in numbers]
print(f"Powers of numbers: {powers}")

```


# Loop to separate even and odd numbers
```

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []
odd_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
```


# Loop to create a list of tuples
```

tuple_list = [(x, x ** 2) for x in range(5)]
print(f"List of tuples: {tuple_list}")
```


# Loop to calculate the sum of digits of a number
```

number = 12345
sum_of_digits = 0
for digit in str(number):
    sum_of_digits += int(digit)
print(f"Sum of digits: {sum_of_digits}")
```


# Loop to create a multiplication table
```

n = 5
multiplication_table = [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
print(f"Multiplication table:")
for row in multiplication_table:
    print(row)
```


# Loop to find the length of a string
```

string = "Hello, world!"
length = 0
for _ in string:
    length += 1
print(f"Length of the string: {length}")
```


# Loop to count the occurrences of a character in a string
```

string = "hello world"
char = 'l'
count = 0
for c in string:
    if c == char:
        count += 1
print(f"Occurrences of '{char}' in the string: {count}")

```


# Loop to find the index of an element in a list
```

numbers = [10, 20, 30, 40, 50]
target = 30
for index, number in enumerate(numbers):
    if number == target:
        print(f"Index of {target} in the list: {index}")
        break
```


# Loop to find the maximum value in a list of tuples
```

tuple_list = [(1, 2), (3, 4), (5, 6)]
max_value = max(tuple_list, key=lambda x: x[1])
print(f"Maximum value in list of tuples: {max_value}")
```


# Loop to find the common characters in two strings
```

string1 = "hello"
string2 = "world"
common_chars = [char for char in string1 if char in string2]
print(f"Common characters in strings: {common_chars}")
```


# Loop to create a dictionary of counts of elements in a list
```

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counts = {}
for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1
print(f"Dictionary of counts: {counts}")

```


# Loop to create a list of prime numbers
```

prime_numbers = []
for num in range(2, 20):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        prime_numbers.append(num)
print(f"List of prime numbers: {prime_numbers}")
```


# Loop to calculate the sum of elements in a nested list
```

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total_sum = 0
for sublist in nested_list:
    for item in sublist:
        total_sum += item
print(f"Sum of elements in nested list: {total_sum}")

```


# Loop to count the number of vowels in a string
```

string = "hello world"
vowels = "aeiou"
vowel_count = 0
for char in string:
    if char in vowels:
        vowel_count += 1
print(f"Number of vowels in string: {vowel_count}")

```


# Loop to find the intersection of two sets
```

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1 & set2
print(f"Intersection of sets: {intersection}")

```


# Loop to find the difference of two sets
```

difference = set1 - set2
print(f"Difference of sets: {difference}")
```


# Loop to find the symmetric difference of two sets
```

symmetric_difference = set1 ^ set2
print(f"Symmetric difference of sets: {symmetric_difference}")
```


# Loop to count the occurrences of words in a string
```

string = "hello hello world"
words = string.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(f"Word counts: {word_counts}")

```


# Loop to create a list of even numbers from 1 to 20
```

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(f"List of even numbers: {even_numbers}")

```


# Loop to create a list of odd numbers from 1 to 20
```

odd_numbers = [x for x in range(1, 21) if x % 2 != 0]
print(f"List of odd numbers: {odd_numbers}")
```


# Loop to create a list of squares of numbers from 1 to 10
```

squares = [x ** 2 for x in range(1, 11)]
print(f"Squares of numbers from 1 to 10: {squares}")

```


# Loop to find the sum of squares of numbers from 1 to 10
```

sum_of_squares = sum(x ** 2 for x in range(1, 11))
print(f"Sum of squares from 1 to 10: {sum_of_squares}")
```


# Loop to find the factorial of a number using recursion
```

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5 using recursion: {factorial(5)}")

```


# Loop to find the greatest common divisor (GCD) of two numbers
```

a, b = 48, 18
while b:
    a, b = b, a % b
print(f"GCD of 48 and 18: {a}")
```


# Loop to find the least common multiple (LCM) of two numbers
```

a, b = 48, 18
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

lcm = (a * b) // gcd(a, b)
print(f"LCM of 48 and 18: {lcm}")
```


# Loop to create a dictionary from two lists
```

keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
dictionary = dict(zip(keys, values))
print(f"Dictionary from two lists: {dictionary}")

```


# Loop to find the longest word in a string
```

string = "hello world this is a test"
words = string.split()
longest_word = max(words, key=len)
print(f"Longest word in string: {longest_word}")

```

# Loop to find the shortest word in a string
```

shortest_word = min(words, key=len)
print(f"Shortest word in string: {shortest_word}")
```


# Loop to find the sum of odd numbers from 1 to 10
```

sum_of_odds = sum(x for x in range(1, 11) if x % 2 != 0)
print(f"Sum of odd numbers from 1 to 10: {sum_of_odds}")

```


# Loop to find the product of even numbers from 1 to 10
```

product_of_evens = 1
for x in range(1, 11):
    if x % 2 == 0:
        product_of_evens *= x
print(f"Product of even numbers from 1 to 10: {product_of_evens}")

```


# Loop to create a dictionary of squares of numbers from 1 to 5
```

squares_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Dictionary of squares: {squares_dict}")
```


# Loop to create a list of cubes of numbers from 1 to 5
```

cubes = [x ** 3 for x in range(1, 6)]
print(f"List of cubes: {cubes}")

```


# Loop to find the sum of cubes of numbers from 1 to 5
```

sum_of_cubes = sum(x ** 3 for x in range(1, 6))
print(f"Sum of cubes: {sum_of_cubes}")

```


# Loop to create a list of factorials from 1 to 5
```

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorials = [factorial(x) for x in range(1, 6)]
print(f"List of factorials: {factorials}")

```


# Loop to find the sum of factorials from 1 to 5
```

sum_of_factorials = sum(factorials)
print(f"Sum of factorials: {sum_of_factorials}")
```

