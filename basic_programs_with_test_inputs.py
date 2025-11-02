# Part A: Loop Statements

# 1 - Sum of even numbers from 2 to 100
print("1. Sum of even numbers from 2 to 100:")
print(sum(range(2, 101, 2)))
print()

# 2 - Numbers divisible by 7 but not by 5
print("2. Numbers between 100-200 divisible by 7 but not by 5:")
for i in range(100, 201):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
print()

# 3 - Factorial
print("3. Factorial of 5:")
num = 5  # Test input
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")
print()

# 4 - Fibonacci
print("4. First 8 Fibonacci numbers:")
n = 8  # Test input
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("\n")

# 5 - Count digits
print("5. Count digits in number 12345:")
num = 12345  # Test input
count = 0
n = abs(num)
if n == 0:
    count = 1
else:
    while n > 0:
        n //= 10
        count += 1
print(f"Number of digits in {num}: {count}")
print()

# 6 - Sum of digits
print("6. Sum of digits in 12345:")
num = 12345  # Test input
s = 0
n = abs(num)
while n > 0:
    s += n % 10
    n //= 10
print(f"Sum of digits in {num}: {s}")
print()

# 7 - Reverse number
print("7. Reverse of number 12345:")
num = 12345  # Test input
rev = 0
n = abs(num)
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
if num < 0:
    rev = -rev
print(f"Reverse of {num}: {rev}")
print()

# 8 - Prime numbers
print("8. Prime numbers from 2 to 100:")
for num in range(2, 101):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
print("\n")

# 9 - Multiplication table
print("9. Multiplication table of 5:")
num = 5  # Test input
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

# 10 - Count vowels and consonants
print("10. Count vowels and consonants in 'Hello World':")
s = "Hello World"  # Test input
s = s.lower()
vowels = 0
consonants = 0
for ch in s:
    if ch.isalpha():
        if ch in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print(f"Vowels: {vowels}, Consonants: {consonants}")
print()

# 11 - Numbers not divisible by 3
print("11. First 10 numbers not divisible by 3:")
count = 0
for i in range(1, 101):
    if i % 3 != 0:
        print(i, end=" ")
        count += 1
        if count == 10:
            break
print("\n")

# 12 - Cube of numbers
print("12. Cubes of first 5 numbers:")
n = 5  # Test input
for i in range(1, n + 1):
    print(f"{i}³ = {i ** 3}")
print()

# 13 - Armstrong numbers
print("13. Armstrong numbers between 100 and 1000:")
for num in range(100, 1001):
    order = len(str(num))
    s = sum(int(d) ** order for d in str(num))
    if s == num:
        print(num, end=" ")
print("\n")

# 14 - Star pattern
print("14. Star pattern:")
for i in range(1, 6):
    print('*' * i)
print()

# 15 - Number pattern
print("15. Number pattern:")
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
print()

# Part B: Conditional Statements

# 16 - Check positive/negative
print("16. Check if number is positive/negative/zero:")
num = 42  # Test input
if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print("Zero")
print()

# 17 - Even or odd
print("17. Check if number is even or odd:")
num = 15  # Test input
print(f"{num} is", "Even" if num % 2 == 0 else "Odd")
print()

# 18 - Leap year
print("18. Check leap year:")
year = 2024  # Test input
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
print()

# 19 - Maximum of three numbers
print("19. Maximum of three numbers:")
a, b, c = 10, 20, 30  # Test inputs
print(f"Maximum of {a}, {b}, {c} is {max(a, b, c)}")
print()

# 20 - Check character type
print("20. Check character type:")
ch = 'A'  # Test input
if ch.isalpha():
    if ch.lower() in 'aeiou':
        print(f"'{ch}' is a Vowel")
    else:
        print(f"'{ch}' is a Consonant")
elif ch.isdigit():
    print(f"'{ch}' is a Digit")
else:
    print(f"'{ch}' is a Special Character")
print()

# 21 - Grade calculation
print("21. Calculate grade:")
marks = 85  # Test input
if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks < 90:
    grade = "B"
elif 70 <= marks < 80:
    grade = "C"
elif 60 <= marks < 70:
    grade = "D"
else:
    grade = "F"
print(f"Marks: {marks}, Grade: {grade}")
print()

# 22 - Divisibility check
print("22. Check if number is divisible by both 3 and 5:")
num = 15  # Test input
print(f"{num} is", "Divisible" if num % 3 == 0 and num % 5 == 0 else "Not Divisible")
print()

# 23 - Valid triangle
print("23. Check if triangle is valid:")
a, b, c = 3, 4, 5  # Test inputs
if a + b > c and a + c > b and b + c > a:
    print(f"Triangle with sides {a}, {b}, {c} is Valid")
else:
    print(f"Triangle with sides {a}, {b}, {c} is Invalid")
print()

# 24 - Voting eligibility
print("24. Check voting eligibility:")
age = 19  # Test input
print(f"Age {age}:", "Eligible to Vote" if age >= 18 else "Not Eligible")
print()

# 25 - Prime number check
print("25. Check if number is prime:")
num = 17  # Test input
is_prime = True
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False
print(f"{num} is", "Prime" if is_prime else "Not Prime")
print()

# 26 - Palindrome check
print("26. Check if string is palindrome:")
s = "radar"  # Test input
print(f"'{s}' is", "Palindrome" if s == s[::-1] else "Not Palindrome")
print()

# 27 - Electricity bill
print("27. Calculate electricity bill:")
units = 150  # Test input
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2.5
else:
    bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
print(f"Units: {units}, Bill: ₹{bill}")
print()

# 28 - Day of week
print("28. Day of week:")
day = 3  # Test input
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if 1 <= day <= 7:
    print(f"Day {day} is {days[day - 1]}")
else:
    print("Invalid day")
print()

# 29 - Simple calculator
print("29. Simple calculator:")
a, b = 10, 5  # Test inputs
op = '+'  # Test input
if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    result = a / b
else:
    result = "Invalid Operator"
print(f"{a} {op} {b} = {result}")
print()

# 30 - Check character case
print("30. Check character case:")
ch = 'K'  # Test input
if ch.isupper():
    print(f"'{ch}' is Uppercase")
elif ch.islower():
    print(f"'{ch}' is Lowercase")
else:
    print(f"'{ch}' is Not Alphabet")
print()

# 31 - Even or odd (alternative)
print("31. Check if number is even or odd (alternative):")
num = 24  # Test input
print(f"{num} is", "Even" if num % 2 == 0 else "Odd")
print()

# 32 - Prime number check (alternative)
print("32. Check if number is prime (alternative):")
num = 29  # Test input
is_prime = True
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False
print(f"{num} is", "PRIME" if is_prime else "NOT PRIME")