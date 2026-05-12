# # 1. write a python programe to print Hello, world!
# print("Hello, world!")


# #2. write a python progrme to do arthimetical opertaions addition and division.
# def add(a, b):
#     return a + b
# def divide(a, b):
#     return a / b

# result_add = add(10, 5)
# result_divide = divide(10, 5)

# print("Addition:", result_add)
# print("Division:", result_divide)

# #addition 
# num1 = int(input("Enter the number 1: "))
# num2 = int(input("Enter the number 2: "))

# addition = num1 + num2
# print("The additioin of two numbers is: ", addition)

# #division
# division = num1/num2
# print("The division of two numbers is : ", division)

# # 3. Write a python programe to print area of triangle.
# height = float(input("Enter the height of the triangle: "))
# base = float(input("Enter the base of the triangle: "))
# area = 0.5*height*base
# print("The area of the triangle is: ", area)

# def area_of_triangle(base, height):
#     return 0.5 * base * height
# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: ")) 
# area = area_of_triangle(base, height)
# print("The area of the triangle is: ", area)

# # 4. Write a programe to swap two varibles.
# a = input("Enter the value of a: ")
# b = input("Enter the value of b: ")
# print("Before swapping: ", "a= ", a, "b= ", b)
# a, b = b, a
# print("After swapping: ", "a= ", a, "b= ", b)


# # 5. Write a python programe to print a randome numbers
# import random
# print("Random number between 1 to 100: ", random.randint(1, 100))

# n = int(input())
# arr = list(map(int, input().split()))

# count = 0
# total = 0
# for num in arr:
#     if num % 2 != 0:
#         count += 1
#         total += num

# avg = total / count if count else 0

# print((count, total, avg))

# # 6. Write a programe to convert kilometers to meters.
# kilometers = float(input("Enter distance in kilometers: "))
# meters = kilometers * 1000

# print(f"{kilometers} kilometers is equal to {meters} meters.")

# 7. Write a programe to convert Celsius to Fahrenheit.
# celsius = float(input("Enter temperature in celsius: "))
# fahrenheit = (celsius * 9/5) + 32

# print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

         