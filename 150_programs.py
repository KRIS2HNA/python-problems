# 1. write a python programe to print Hello, world!
print("Hello, world!")


#2. write a python progrme to do arthimetical opertaions addition and division.
def add(a, b):
    return a + b
def divide(a, b):
    return a / b

result_add = add(10, 5)
result_divide = divide(10, 5)

print("Addition:", result_add)
print("Division:", result_divide)

#addition 
num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))

addition = num1 + num2
print("The additioin of two numbers is: ", addition)

#division
division = num1/num2
print("The division of two numbers is : ", division)

# 3. Write a python programe to print area of triangle.
height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base of the triangle: "))
area = 0.5*height*base
print("The area of the triangle is: ", area)

def area_of_triangle(base, height):
    return 0.5 * base * height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: ")) 
area = area_of_triangle(base, height)
print("The area of the triangle is: ", area)

