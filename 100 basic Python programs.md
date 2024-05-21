 100 basic Python programs:

1. Hello World Program
```python
print("Hello, World!")
```

2. Addition of Two Numbers
```python
num1 = 5
num2 = 7
sum = num1 + num2
print("Sum:", sum)
```

3. Subtraction of Two Numbers
```python
num1 = 10
num2 = 4
difference = num1 - num2
print("Difference:", difference)
```

4. Multiplication of Two Numbers
```python
num1 = 3
num2 = 6
product = num1 * num2
print("Product:", product)
```

5. Division of Two Numbers
```python
num1 = 20
num2 = 5
quotient = num1 / num2
print("Quotient:", quotient)
```

6. Modulus of Two Numbers
```python
num1 = 15
num2 = 4
remainder = num1 % num2
print("Remainder:", remainder)
```

7. Exponentiation
```python
base = 2
exponent = 3
result = base ** exponent
print("Result:", result)
```

8. Square of a Number
```python
num = 4
square = num ** 2
print("Square:", square)
```

9. Cube of a Number
```python
num = 3
cube = num ** 3
print("Cube:", cube)
```

10. Area of a Rectangle
```python
length = 5
width = 3
area = length * width
print("Area of Rectangle:", area)
```

11. Area of a Circle
```python
radius = 7
area = 3.14 * (radius ** 2)
print("Area of Circle:", area)
```

12. Perimeter of a Rectangle
```python
length = 4
width = 6
perimeter = 2 * (length + width)
print("Perimeter of Rectangle:", perimeter)
```

13. Perimeter of a Circle
```python
radius = 8
perimeter = 2 * 3.14 * radius
print("Perimeter of Circle:", perimeter)
```

14. Simple Interest
```python
principal = 1000
rate = 5
time = 2
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)
```

15. Compound Interest
```python
principal = 1500
rate = 5
time = 2
compound_interest = principal * ((1 + rate / 100) ** time)
print("Compound Interest:", compound_interest)
```

16. Check If a Number is Even or Odd
```python
num = 9
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

17. Check If a Number is Positive or Negative
```python
num = -3
if num >= 0:
    print("Positive")
else:
    print("Negative")
```

18. Check If a Year is a Leap Year
```python
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
```

19. Find the Largest Among Three Numbers
```python
num1 = 12
num2 = 18
num3 = 7
if num1 >= num2 and num1 >= num3:
    print("Largest:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest:", num2)
else:
    print("Largest:", num3)
```

20. Find the Factorial of a Number
```python
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial:", factorial)
```

21. Find the Fibonacci Series
```python
num = 10
a, b = 0, 1
fib_series = [a, b]
for i in range(2, num):
    c = a + b
    a, b = b, c
    fib_series.append(c)
print("Fibonacci Series:", fib_series)
```

22. Check If a Number is Prime
```python
num = 17
is_prime = True
if num > 1:
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print("Prime")
else:
    print("Not Prime")
```

23. Find the Prime Numbers in a Range
```python
start = 10
end = 50
prime_numbers = []
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if num % i == 0:
                break
        else:
            prime_numbers.append(num)
print("Prime Numbers:", prime_numbers)
```

24. Reverse a Number
```python
num = 1234
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num //= 10
print("Reverse:", reverse)
```

25. Find the Sum of Digits of a Number
```python
num = 12345
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print("Sum of Digits:", sum)
```

26. Check If a Number is an Armstrong Number
```python
num = 153
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
```

27. Find the Armstrong Numbers in a Range
```python
start = 100
end = 500
armstrong_numbers = []
for num in range(start, end + 1):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        armstrong_numbers.append(num)
print("Armstrong Numbers:", armstrong_numbers)
```

28. Find the LCM of Two Numbers
```python
num1 = 12
num2 = 15
if num1 > num2:
    greater = num1
else:
    greater = num2
while True:
    if greater % num1 == 0 and greater % num2 == 0:
        lcm = greater
        break
    greater += 1
print("LCM:", lcm)
```

29. Find the GCD of Two Numbers
```python
num1 = 24
num2 = 36
while num2 != 0:
   

 temp = num2
    num2 = num1 % num2
    num1 = temp
gcd = num1
print("GCD:", gcd)
```

30. Convert Decimal to Binary
```python
decimal = 10
binary = ""
while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal //= 2
print("Binary:", binary)
```

31. Convert Decimal to Octal
```python
decimal = 20
octal = ""
while decimal > 0:
    octal = str(decimal % 8) + octal
    decimal //= 8
print("Octal:", octal)
```

32. Convert Decimal to Hexadecimal
```python
decimal = 30
hexadecimal = ""
while decimal > 0:
    remainder = decimal % 16
    if remainder < 10:
        hexadecimal = str(remainder) + hexadecimal
    else:
        hexadecimal = chr(remainder + 55) + hexadecimal
    decimal //= 16
print("Hexadecimal:", hexadecimal)
```

33. Convert Binary to Decimal
```python
binary = "1010"
decimal = 0
for i in range(len(binary)):
    decimal += int(binary[len(binary) - 1 - i]) * (2 ** i)
print("Decimal:", decimal)
```

34. Convert Binary to Octal
```python
binary = "1010"
decimal = 0
for i in range(len(binary)):
    decimal += int(binary[len(binary) - 1 - i]) * (2 ** i)
octal = ""
while decimal > 0:
    octal = str(decimal % 8) + octal
    decimal //= 8
print("Octal:", octal)
```

35. Convert Binary to Hexadecimal
```python
binary = "1010"
decimal = 0
for i in range(len(binary)):
    decimal += int(binary[len(binary) - 1 - i]) * (2 ** i)
hexadecimal = ""
while decimal > 0:
    remainder = decimal % 16
    if remainder < 10:
        hexadecimal = str(remainder) + hexadecimal
    else:
        hexadecimal = chr(remainder + 55) + hexadecimal
    decimal //= 16
print("Hexadecimal:", hexadecimal)
```

36. Convert Octal to Decimal
```python
octal = "24"
decimal = 0
for i in range(len(octal)):
    decimal += int(octal[len(octal) - 1 - i]) * (8 ** i)
print("Decimal:", decimal)
```

37. Convert Octal to Binary
```python
octal = "24"
decimal = 0
for i in range(len(octal)):
    decimal += int(octal[len(octal) - 1 - i]) * (8 ** i)
binary = ""
while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal //= 2
print("Binary:", binary)
```

38. Convert Octal to Hexadecimal
```python
octal = "24"
decimal = 0
for i in range(len(octal)):
    decimal += int(octal[len(octal) - 1 - i]) * (8 ** i)
hexadecimal = ""
while decimal > 0:
    remainder = decimal % 16
    if remainder < 10:
        hexadecimal = str(remainder) + hexadecimal
    else:
        hexadecimal = chr(remainder + 55) + hexadecimal
    decimal //= 16
print("Hexadecimal:", hexadecimal)
```

39. Convert Hexadecimal to Decimal
```python
hexadecimal = "1E"
decimal = 0
for i in range(len(hexadecimal)):
    if hexadecimal[i].isdigit():
        decimal += int(hexadecimal[i]) * (16 ** (len(hexadecimal) - 1 - i))
    else:
        decimal += (ord(hexadecimal[i].upper()) - 55) * (16 ** (len(hexadecimal) - 1 - i))
print("Decimal:", decimal)
```

40. Convert Hexadecimal to Binary
```python
hexadecimal = "1E"
decimal = 0
for i in range(len(hexadecimal)):
    if hexadecimal[i].isdigit():
        decimal += int(hexadecimal[i]) * (16 ** (len(hexadecimal) - 1 - i))
    else:
        decimal += (ord(hexadecimal[i].upper()) - 55) * (16 ** (len(hexadecimal) - 1 - i))
binary = ""
while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal //= 2
print("Binary:", binary)
```

41. Convert Hexadecimal to Octal
```python
hexadecimal = "1E"
decimal = 0
for i in range(len(hexadecimal)):
    if hexadecimal[i].isdigit():
        decimal += int(hexadecimal[i]) * (16 ** (len(hexadecimal) - 1 - i))
    else:
        decimal += (ord(hexadecimal[i].upper()) - 55) * (16 ** (len(hexadecimal) - 1 - i))
octal = ""
while decimal > 0:
    octal = str(decimal % 8) + octal
    decimal //= 8
print("Octal:", octal)
```

42. Check If a String is Palindrome
```python
string = "radar"
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

43. Count the Number of Vowels in a String
```python
string = "hello"
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of Vowels:", count)
```

44. Count the Number of Words in a String
```python
string = "Hello, how are you?"
words = string.split()
print("Number of Words:", len(words))
```

45. Reverse a String
```python
string = "hello"
reverse = string[::-1]
print("Reverse:", reverse)
```

46. Capitalize the First Letter of Each Word in a String
```python
string = "hello world"
capitalized = string.title()
print("Capitalized:", capitalized)
```

47. Remove Punctuation from a String
```python
string = "Hello, World!"
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punctuation = ""
for char in string:
    if char not in punctuation:
        no_punctuation += char
print("No Punctuation:", no_punctuation)
```

48. Find the Longest Word in a String
```python
string = "Hello world, how are you?"
words = string.split()
longest_word = max(words, key=len)
print("Longest Word:", longest_word)
```

49. Count the Number of Occurrences of a Character in a String
```python
string = "hello world"
char = 'l'
count = string.count(char)
print("Occurrences of '{}' : {}".format(char, count))
```

50. Concatenate Two Strings
```python
string1 = "Hello"
string2 = "World"
concatenated = string1 + " " +

 string2
print("Concatenated:", concatenated)
```

51. Check If Two Strings are Anagrams
```python
string1 = "listen"
string2 = "silent"
if sorted(string1) == sorted(string2):
    print("Anagrams")
else:
    print("Not Anagrams")
```

52. Find the ASCII Value of a Character
```python
char = 'A'
ascii_value = ord(char)
print("ASCII Value:", ascii_value)
```

53. Find the Character from an ASCII Value
```python
ascii_value = 65
char = chr(ascii_value)
print("Character:", char)
```

54. Remove Spaces from a String
```python
string = "Hello world"
no_spaces = string.replace(" ", "")
print("No Spaces:", no_spaces)
```

55. Convert Lowercase to Uppercase
```python
string = "hello"
uppercase = string.upper()
print("Uppercase:", uppercase)
```

56. Convert Uppercase to Lowercase
```python
string = "HELLO"
lowercase = string.lower()
print("Lowercase:", lowercase)
```

57. Find the Smallest Among Three Numbers
```python
num1 = 10
num2 = 7
num3 = 13
if num1 <= num2 and num1 <= num3:
    print("Smallest:", num1)
elif num2 <= num1 and num2 <= num3:
    print("Smallest:", num2)
else:
    print("Smallest:", num3)
```

58. Swap Two Numbers
```python
num1 = 5
num2 = 8
num1, num2 = num2, num1
print("Swapped Numbers:", num1, num2)
```

59. Find the Sum of Natural Numbers
```python
n = 10
sum = n * (n + 1) // 2
print("Sum of Natural Numbers:", sum)
```

60. Find the Sum of Natural Numbers using Loop
```python
n = 10
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum of Natural Numbers:", sum)
```

61. Find the Sum of Squares of Natural Numbers
```python
n = 5
sum = n * (n + 1) * (2 * n + 1) // 6
print("Sum of Squares of Natural Numbers:", sum)
```

62. Find the Sum of Squares of Natural Numbers using Loop
```python
n = 5
sum = 0
for i in range(1, n + 1):
    sum += i ** 2
print("Sum of Squares of Natural Numbers:", sum)
```

63. Find the Sum of Cubes of Natural Numbers
```python
n = 4
sum = (n * (n + 1) // 2) ** 2
print("Sum of Cubes of Natural Numbers:", sum)
```

64. Find the Sum of Cubes of Natural Numbers using Loop
```python
n = 4
sum = 0
for i in range(1, n + 1):
    sum += i ** 3
print("Sum of Cubes of Natural Numbers:", sum)
```

65. Find the Area of a Triangle
```python
base = 6
height = 4
area = 0.5 * base * height
print("Area of Triangle:", area)
```

66. Check If a Triangle is Equilateral, Isosceles, or Scalene
```python
side1 = 5
side2 = 5
side3 = 5
if side1 == side2 == side3:
    print("Equilateral")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Isosceles")
else:
    print("Scalene")
```

67. Check If a Number is Perfect
```python
num = 28
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("Perfect")
else:
    print("Not Perfect")
```

68. Check If a Number is Abundant
```python
num = 12
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum > num:
    print("Abundant")
else:
    print("Not Abundant")
```

69. Check If a Number is Deficient
```python
num = 15
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum < num:
    print("Deficient")
else:
    print("Not Deficient")
```

70. Find the Sum of Factors of a Number
```python
num = 20
sum = 0
for i in range(1, num + 1):
    if num % i == 0:
        sum += i
print("Sum of Factors:", sum)
```

71. Find the Product of Factors of a Number
```python
num = 30
product = 1
for i in range(1, num + 1):
    if num % i == 0:
        product *= i
print("Product of Factors:", product)
```

72. Check If a Number is Prime or Composite
```python
num = 11
if num > 1:
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            print("Composite")
            break
    else:
        print("Prime")
else:
    print("Composite")
```

73. Find the Prime Factors of a Number
```python
num = 24
prime_factors = []
for i in range(2, num + 1):
    while num % i == 0:
        prime_factors.append(i)
        num //= i
print("Prime Factors:", prime_factors)
```

74. Find the Sum of First n Natural Numbers
```python
n = 10
sum = n * (n + 1) // 2
print("Sum of First {} Natural Numbers:".format(n), sum)
```

75. Find the Sum of First n Natural Numbers using Loop
```python
n = 10
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum of First {} Natural Numbers:".format(n), sum)
```

76. Check If a Number is a Perfect Square
```python
num = 16
if num >= 0 and int(num ** 0.5) ** 2 == num:
    print("Perfect Square")
else:
    print("Not Perfect Square")
```

77. Find the Square Root of a Number
```python
num = 25
square_root = num ** 0.5
print("Square Root:", square_root)
```

78. Find the Cube Root of a Number
```python
num = 64
cube_root = num ** (1/3)
print("Cube Root:", cube

_root)
```

79. Find the Smallest Element in a List
```python
numbers = [5, 2, 8, 1, 9]
smallest = min(numbers)
print("Smallest Element:", smallest)
```

80. Find the Largest Element in a List
```python
numbers = [5, 2, 8, 1, 9]
largest = max(numbers)
print("Largest Element:", largest)
```

81. Find the Second Largest Element in a List
```python
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers)
second_largest = sorted_numbers[-2]
print("Second Largest Element:", second_largest)
```

82. Find the Sum of Elements in a List
```python
numbers = [5, 2, 8, 1, 9]
sum = 0
for num in numbers:
    sum += num
print("Sum of Elements:", sum)
```

83. Find the Average of Elements in a List
```python
numbers = [5, 2, 8, 1, 9]
average = sum(numbers) / len(numbers)
print("Average of Elements:", average)
```

84. Count the Number of Even and Odd Numbers in a List
```python
numbers = [5, 2, 8, 1, 9]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even Count:", even_count)
print("Odd Count:", odd_count)
```

85. Remove Duplicate Elements from a List
```python
numbers = [5, 2, 8, 5, 1, 9, 2]
unique_numbers = list(set(numbers))
print("Unique Elements:", unique_numbers)
```

86. Check If a List is Empty
```python
numbers = []
if not numbers:
    print("List is Empty")
else:
    print("List is Not Empty")
```

87. Reverse a List
```python
numbers = [5, 2, 8, 1, 9]
reversed_numbers = numbers[::-1]
print("Reversed List:", reversed_numbers)
```

88. Concatenate Two Lists
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated List:", concatenated_list)
```

89. Find the Union of Two Lists
```python
list1 = [1, 2, 3]
list2 = [3, 4, 5]
union_list = list(set(list1 + list2))
print("Union of Lists:", union_list)
```

90. Find the Intersection of Two Lists
```python
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection_list = list(set(list1) & set(list2))
print("Intersection of Lists:", intersection_list)
```

91. Find the Difference Between Two Lists
```python
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
difference_list = list(set(list1) - set(list2))
print("Difference Between Lists:", difference_list)
```

92. Check If a List is Palindrome
```python
numbers = [1, 2, 3, 2, 1]
if numbers == numbers[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

93. Check If a List is Sorted
```python
numbers = [1, 2, 3, 4, 5]
if numbers == sorted(numbers):
    print("Sorted")
else:
    print("Not Sorted")
```

94. Bubble Sort
```python
numbers = [64, 25, 12, 22, 11]
for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Sorted List:", numbers)
```

95. Selection Sort
```python
numbers = [64, 25, 12, 22, 11]
for i in range(len(numbers)):
    min_index = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
print("Sorted List:", numbers)
```

96. Insertion Sort
```python
numbers = [64, 25, 12, 22, 11]
for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    while j >= 0 and key < numbers[j]:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = key
print("Sorted List:", numbers)
```

97. Linear Search
```python
numbers = [64, 25, 12, 22, 11]
target = 12
found = False
for i in range(len(numbers)):
    if numbers[i] == target:
        print("Element found at index:", i)
        found = True
        break
if not found:
    print("Element not found")
```

98. Binary Search
```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

numbers = [11, 12, 22, 25, 64]
target = 12
result = binary_search(numbers, target)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
```

99. Merge Sort
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right

_half[j]
            j += 1
            k += 1

numbers = [64, 25, 12, 22, 11]
merge_sort(numbers)
print("Sorted List:", numbers)
```

100. Quick Sort
```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

numbers = [64, 25, 12, 22, 11]
quick_sort(numbers, 0, len(numbers) - 1)
print("Sorted List:", numbers)
```

These are basic Python programs covering various concepts such as arithmetic operations, conditionals, loops, functions, and data structures like lists.
