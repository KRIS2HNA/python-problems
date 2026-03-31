'''
1.Is python a complied language or an interpreted language?
Pytho is an interpreted language that is internally complied to bytecode.

compliation:
the process is converting source code into machine code 

Interpretation:
after compliation the interpreter excutes the machine code line-by-line.

2.How can you concatenate two list in python?

we can concatennate two lists using + operator or using extend() method.

1.using + operatror:

'''
List_1 = [1,2,3,4,5]
List_2 = [6,7,8,9,10]

print(List_1 + List_2)

'''output: [1,2,3,4,5,6,7,8,9,10]

2.using extend() method:

'''
List_1 = [1,2,3,4,5]
List_2 = [6,7,8,9,10]

List_1.extend(List_2)
print(List_1)

'''output: [1,2,3,4,5,6,7,8,9,10]

3.Difference Between for loop andd While loop?

for loop: 
when we know how many times to repeat, often with lists, tuples, sets, or dictionaries.

While loop:
when we only have an end condition and don't know how many times it will repeat.
'''
# for loop example:
for i in range(6):
    print((6-i)*"*")
    
'''output:
******
*****
****
***
**
*'''
# while loop example:
count = 0
while count < 6:
    print((6-count) * "*")
    count += 1

'''output:
******
*****
****
***
**
*
'''

'''
4.How do you floor a number in python?
We can floor a number in python using math.floor() method from math module.

Also we can use int() function to floor a postive number.

and also we can use cell() method from math module to ceil a negative number.'''

import math
num1 = 86.9
f_num = math.floor(num1)
print(f_num)

# output: 8

num2 = 8.76
c_num = math.ceil(num2)
print(c_num)

# output: 9
# 4

num3 = 7.55
i_num3 = int(num3)
print(i_num3)

# output: 7

'''
5.What is the differnce between / and // operators in python?

/ operator:it is used for division and returns a floot result.

// operator:it is used foe floor division and returns an integer.

'''
# / operator example:
def division(a,b):
    return a/b

result=division(16,5)
print(result)

# output: 3.2

def floor_division(a,b):
    return a//b

result2 = floor_division(16,5)
print(result2)

#  output: 3

'''
6.Is indentation required in python? why ?
Yes, Indentation is required in python because it defines the block of code. It indicates a block of code belongs to a particular control structure, function, or class.'''

def great(num):
    if num > 0:
        print("postive number")
    else:
        print("negative number")
great(5)

'''
7.
Can we pass a function as an argument to another function in python? explain with an example.
Yes, python allows passing functions as arguments because functions are first-class objects in python.
'''

def great(num):
    square = num * num
    return square
def display(func, value):
    result = func(value)
    print("The result is:", result)
display(great, 6)

# output: The result is: 36
nums = [1,2,3,4,5,6,7,8,9,10]

def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, nums)))


'''
8.What is a dynamically typed language? is python a dynamically typed language?
In a dynamically typed language, the data type of a variable is determined at runtime, not at complie time
No need to declare data types manually; python automatically detects it based on the assigned value'''

a = 0 # now a is an integer
print(type(a))

a = "hello" # now a is a string
print(type(a))

a = 9.0 # now a is a float
print(type(a))

'''
output:
<class 'int'>
<class 'str'>
<class 'float'>


9.What is pass statement in python?
The pass statement in python is a null operation; it used as a placeholder when a statement is synatically required but no action required.
Example:
def function_not_implemented_yet():
    pass
function_not_implemented_yet()

output: None


10.How are arguments passed in python? by value or by reference?
In python argument-passing model is neither "pass by value" nor "pass by reference" but it is called "pass by object reference".

In this model, when an argument is passed to a function, a reference to the object is passed, not the actual object itself. If the object is mutable (like list
s or dictionaries), changes made to the object inside the function will affect the original object outside the function. However, if the object is immutable (like 
integers, strings, or tuples), any changes made inside the function will not affect the original object.
'''

def modify_List(lst):
    lst.append(4)
my_list = [1, 2, 3]
modify_List(my_list)

print(my_list)  # Output: [1, 2, 3, 4]  
    
'''
11. list
def modify_List(lst):
    lst.append(4)
my_list = [1, 2, 3]
modify_List(my_list)

print(my_list)  # Output: [1, 2, 3, 4]  
    

'''


def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "odd"
print(even_or_odd(5))

def prime_numbers(num):
    if num < 2:
        return "Not prime"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "not prime"
    return "prime"
print(prime_numbers(17))

#Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# Fibonacci sequence
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
print(fibonacci(10))


#  reversa a number
def reverse_number(num):
    sign = -1 if num < 0 else 1
    num = abs(num)
    
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num * sign
print(reverse_number(-12345))

# palindrome number
def is_palindrome(num):
    is_palinrome = True
    num_str = str(num)
    left, right = 0, len(num_str) - 1
    while left < right:
        if num_str[left] != num_str[right]:
            is_palinrome = False
            break
        left += 1
        right -= 1
    return is_palinrome
print(is_palindrome(12321))  # Output: True

print(bool(" 0"))  # Output: True

n = int(input())
arr = list(map(int, input().split()))

count = 0
total = 0
for num in arr:
    if num % 2 == 0:
        count += 1
        total += num

avg = total / count if count else 0

print((count, total, avg))