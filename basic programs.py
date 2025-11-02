# # Part A: Loop Statements

# # 1
# print(sum(range(2, 101, 2)))

# # 2
# for i in range(100, 201):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i)

# # 3
# num = int(input())
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print(fact)

# # 4
# n = int(input())
# a, b = 0, 1
# for _ in range(n):
#     print(a)
#     a, b = b, a + b

# # 5
# num = int(input())
# count = 0
# n = abs(num)
# if n == 0:
#     count = 1
# else:
#     while n > 0:
#         n //= 10
#         count += 1
# print(count)

# # 6
# num = int(input())
# s = 0
# n = abs(num)
# while n > 0:
#     s += n % 10
#     n //= 10
# print(s)

# # 7
# num = int(input())
# rev = 0
# n = abs(num)
# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10
# if num < 0:
#     rev = -rev
# print(rev)

# # 8
# for num in range(2, 101):
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         print(num)

# # 9
# num = int(input())
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# # 10
# s = input().lower()
# vowels = 0
# consonants = 0
# for ch in s:
#     if ch.isalpha():
#         if ch in 'aeiou':
#             vowels += 1
#         else:
#             consonants += 1
# print(vowels, consonants)

# # 11
# for i in range(1, 101):
#     if i % 3 != 0:
#         print(i)

# # 12
# n = int(input())
# for i in range(1, n + 1):
#     print(i ** 3)

# # 13
# for num in range(100, 1001):
#     order = len(str(num))
#     s = sum(int(d) ** order for d in str(num))
#     if s == num:
#         print(num)

# # 14
# for i in range(1, 6):
#     print('*' * i)

# # 15
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

# # Part B: Conditional Statements

# # 16
# num = int(input())
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# # 17
# num = int(input())
# print("Even" if num % 2 == 0 else "Odd")

# # 18
# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not Leap Year")

# # 19
# a, b, c = map(int, input().split())
# print(max(a, b, c))

# # 20
# ch = input()
# if ch.isalpha():
#     if ch.lower() in 'aeiou':
#         print("Vowel")
#     else:
#         print("Consonant")
# elif ch.isdigit():
#     print("Digit")
# else:
#     print("Special Character")

# # 21
# marks = int(input())
# if 90 <= marks <= 100:
#     print("A")
# elif 80 <= marks < 90:
#     print("B")
# elif 70 <= marks < 80:
#     print("C")
# elif 60 <= marks < 70:
#     print("D")
# else:
#     print("F")

# # 22
# num = int(input())
# if num % 3 == 0 and num % 5 == 0:
#     print("Divisible")
# else:
#     print("Not Divisible")

# # 23
# a, b, c = map(int, input().split())
# if a + b > c and a + c > b and b + c > a:
#     print("Valid Triangle")
# else:
#     print("Invalid Triangle")

# # 24
# age = int(input())
# if age >= 18:
#     print("Eligible to Vote")
# else:
#     print("Not Eligible")

# # 25
# num = int(input())
# if num > 1:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not Prime")

# # 26
# s = input()
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# # 27
# units = int(input())
# if units <= 100:
#     bill = units * 1.5
# elif units <= 200:
#     bill = 100 * 1.5 + (units - 100) * 2.5
# else:
#     bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
# print(bill)

# # 28
# day = int(input())
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# if 1 <= day <= 7:
#     print(days[day - 1])
# else:
#     print("Invalid")

# # 29
# a = float(input())
# b = float(input())
# op = input()
# if op == '+':
#     print(a + b)
# elif op == '-':
#     print(a - b)
# elif op == '*':
#     print(a * b)
# elif op == '/':
#     print(a / b)
# else:
#     print("Invalid Operator")

# # 30
# ch = input()
# if ch.isupper():
#     print("Uppercase")
# elif ch.islower():
#     print("Lowercase")
# else:
#     print("Not Alphabet")

# # 31 odd or even

# num = int(input())
# if num % 2 == 0:
#     print("Even")
# else:
#     print("odd")
    
# # 32 Prime number check
# num = int(input())
# if num > 1:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print("NOT PRIME")
#             break
#         else:
#             print("PRIME")

# 33 fibonacci series
n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a+b
    
