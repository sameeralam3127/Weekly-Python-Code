number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial of", number, "is", factorial)