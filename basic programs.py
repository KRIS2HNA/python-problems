from typing import List
from collections import defaultdict
import heapq

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

# # 33 fibonacci series
# n = int(input())
# a, b = 0, 1
# for _ in range(n):
#     print(a)
#     a, b = b, a+b
    
# # 34 Factorial of a number
# num = 9
# fact = 1
# for i in range(1, num + 1):
#     fact *= i   
# print(fact)

# # 35 Sum of digits
# num = 1234  # Test input
# s = 0
# n = abs(num)
# while n > 0:
#     s += n % 10
#     n //= 10
# print(f"Sum of digits in {num}: {s}")
# print()
    
# # 36 Reverse a number

# num = 1234
# rev = 0
# n = abs(num)
# while n > 0:
#     rev  = rev * 10 + n % 10
#     n //= 10
#     if num < 0:
#         rev = -rev
#         print(f"Reverse of {num}: {rev}")
#     print()

# # 37 Check Armstrong number
# num = 158
# order = len(str(num))
# s = sum(int(d) ** order for d in str(num))
# if s == num:
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not an Armstrong number")
# print()

# # 38 Print multiplication table
# num = 9
# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")
# print()

# # 39 Count vowels and consonants
# s = "Krishna vamsi"
# vowels = 0
# consonants = 0
# for ch in s.lower():
#     if ch.isalpha():
#         if ch in 'aeiou':
#             vowels += 1
#         else:   
#             consonants += 1
# print(f"Vowels: {vowels}, Consonants: {consonants}")
# print()

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# print("Select operation: +, -, *, /")
# op = input("Enter operator: ")

# if op == '+':
#     print("Result:", a + b)
# elif op == '-':
#     print("Result:", a - b)
# elif op == '*':
#     print("Result:", a * b)
# elif op == '/':
#     print("Result:", a / b)
# else:
#     print("Invalid operator")
    
    
# # 40 Simple calculator  
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))            
# operation = input("Enter operation (+, -, *, /): ")
# if operation == '+':
#     print("Result:", num1 + num2)
# elif operation == '-':
#     print("Result:", num1 - num2)
# elif operation == '*':
#     print("Result:", num1 * num2)
# elif operation == '/':
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error: Division by zero")
# else:
#     print("Invalid operation")
    
# # 41 Find largest of three numbers
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))
# if a >= b and a >= c:
#     print(f"Largest number is: {a}")
# elif b >= a and b >= c:
#     print(f"Largest number is: {b}")
# else:
#     print(f"Largest number is: {c}")

# # 42 Check palindrome string
# s = input("Enter a string: ")   
# if s == s[::-1]:
#     print(f'"{s}" is a palindrome')
# else:
#     print(f'"{s}" is not a palindrome')
    

# # 43 Calculate electricity bill
# units = int(input("Enter number of units consumed: "))
# if units <= 100:    
#     bill = units * 1.5
# elif units <= 200:    
#     bill = 100 * 1.5 + (units - 100) * 2.5  
# else:
#     bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
# print(f"Electricity bill: {bill}")

# # 44 Find day of the week
# day = int(input("Enter day number (1-7): "))
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# if 1 <= day <= 7:
#     print(f"Day: {days[day - 1]}")      
# else:
#     print("Invalid day number")

# # 45 Check uppercase or lowercase
# ch = input("Enter a character: ")  
# if ch.isupper():
#     print(f'"{ch}" is an uppercase letter')
# elif ch.islower():
#     print(f'"{ch}" is a lowercase letter')
# else:
#     print(f'"{ch}" is not an alphabet letter')

 
# leetcode 1611

# class Solution:
#     def minimumOneBitOperations(self, n: int) -> int:
#         if n == 0:
#             return 0
#         msb = 1
#         while (msb << 1) <= n:
#             msb <<= 1
#         return (1 << (msb.bit_length())) - 1 - self.minimumOneBitOperations(n ^ msb)

# # leetcode 1
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         num_map = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_map:
#                 return [num_map[complement], i]
#             num_map[num] = i
#         return []

# leetcode 2

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy_head = ListNode(0)
#         current = dummy_head
#         carry = 0

#         while l1 or l2 or carry:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
#             total = val1 + val2 + carry
#             carry = total // 10
#             current.next = ListNode(total % 10)
#             current = current.next

#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next

#         return dummy_head.next


# # 2169 leetcode
# class Solution:
#     def countOperations(self, num1: int, num2: int) -> int:
#         ans = 0
#         while num1 and num2:
#             if num1 < num2:
#                 num1, num2 = num2, num1
#             # we can do num1 // num2 subtractions in one go
#             ans += num1 // num2
#             num1 %= num2
#         return ans

# # 3
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         seen = {}
#         left = 0
#         max_len = 0

#         for right in range(len(s)):
#             # If duplicate found and within current window
#             if s[right] in seen and seen[s[right]] >= left:
#                 left = seen[s[right]] + 1
#             seen[s[right]] = right
#             max_len = max(max_len, right - left + 1)

#         return max_len
# # 4 leetcode
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         merged = []
#         i, j = 0, 0

#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] < nums2[j]:
#                 merged.append(nums1[i])
#                 i += 1
#             else:
#                 merged.append(nums2[j])
#                 j += 1

#         while i < len(nums1):
#             merged.append(nums1[i])
#             i += 1

#         while j < len(nums2):
#             merged.append(nums2[j])
#             j += 1

#         n = len(merged)
#         if n % 2 == 1:
#             return merged[n // 2]
#         else:
#             return (merged[n // 2 - 1] + merged[n // 2]) / 2    

# # leetcode 3452
# class Solution:
#     def minOperations(self, nums: list[int]) -> int:
#         ans = 0
#         stack = [0]  # sentinel 0 so that even if nums starts >0 it counts correctly

#         for num in nums:
#             # Pop while the stack top is > current number
#             while stack and stack[-1] > num:
#                 stack.pop()
#             # If stack empty or top < num, then for this new number we need an operation
#             if not stack or stack[-1] < num:
#                 ans += 1
#                 stack.append(num)
#             # if stack[-1] == num: do nothing (already counted)
#         return ans
# # lettcode 5
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def expand_around_center(left: int, right: int) -> str:
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return s[left + 1:right]

#         longest = ""
#         for i in range(len(s)):
#             # Odd length palindromes
#             odd_palindrome = expand_around_center(i, i)
#             if len(odd_palindrome) > len(longest):
#                 longest = odd_palindrome

#             # Even length palindromes
#             even_palindrome = expand_around_center(i, i + 1)
#             if len(even_palindrome) > len(longest):
#                 longest = even_palindrome

#         return longest
    
# # leetcode 6
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1 or numRows >= len(s):
#             return s

#         rows = [''] * numRows
#         current_row = 0
#         going_down = False

#         for char in s:
#             rows[current_row] += char
#             if current_row == 0 or current_row == numRows - 1:
#                 going_down = not going_down
#             current_row += 1 if going_down else -1

#         return ''.join(rows)

# # 474 leetcode
# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
        
#         for s in strs:
#             zeros = s.count('0')
#             ones = s.count('1')
            
#             for i in range(m, zeros - 1, -1):
#                 for j in range(n, ones - 1, -1):
#                     dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
                    
#         return dp[m][n]

# # leetcode 7
# class Solution:
#     def reverse(self, x: int) -> int:
#         sign = -1 if x < 0 else 1
#         x_abs = abs(x)
#         rev = 0
        
#         while x_abs != 0:
#             digit = x_abs % 10
#             rev = rev * 10 + digit
#             x_abs //= 10
            
#         rev *= sign
        
#         if rev < -2**31 or rev > 2**31 - 1:
#             return 0
            
#         return rev
    
# # leetcode 8
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         s = s.lstrip()
#         if not s:
#             return 0

#         sign = 1
#         start_index = 0
#         if s[0] in ('-', '+'):
#             sign = -1 if s[0] == '-' else 1
#             start_index = 1

#         result = 0
#         for i in range(start_index, len(s)):
#             if not s[i].isdigit():
#                 break
#             result = result * 10 + int(s[i])

#         result *= sign
#         INT_MIN, INT_MAX = -2**31, 2**31 - 1
#         if result < INT_MIN:
#             return INT_MIN
#         if result > INT_MAX:
#             return INT_MAX

#         return result
    
# # 2654 leetcode
# import math
# from typing import List

# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         n = len(nums)
#         # 1) If any element is already 1
#         ones = nums.count(1)
#         if ones > 0:
#             return n - ones
        
#         # 2) If gcd of entire array > 1 -> impossible
#         total_g = nums[0]
#         for x in nums[1:]:
#             total_g = math.gcd(total_g, x)
#         if total_g > 1:
#             return -1
        
#         # 3) Find shortest subarray with gcd == 1
#         min_len_minus_one = float('inf')  # will store j - i (i.e. L - 1)
#         for i in range(n):
#             g = nums[i]
#             if g == 1:
#                 min_len_minus_one = 0
#                 break
#             for j in range(i + 1, n):
#                 g = math.gcd(g, nums[j])
#                 if g == 1:
#                     min_len_minus_one = min(min_len_minus_one, j - i)
#                     break
        
#         # total operations = (min_len_minus_one) to create one `1` + (n - 1) to spread it
#         return (min_len_minus_one if min_len_minus_one != float('inf') else 0) + (n - 1)


# # leetcode 9
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         original = x
#         rev = 0
#         while x > 0:
#             rev = rev * 10 + x % 10
#             x //= 10
#         return rev == original
    
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         original = x
#         rev = 0
#         while x > 0:
#             rev = rev * 10 + x % 10
#             x //= 10
#         return rev == original

# class Solution:
#     def maxOperations(self, s: str) -> int:
#         ans = 0
#         ones = 0
#         n = len(s)
#         for i, c in enumerate(s):
#             if c == '1':
#                 ones += 1
#             else:  # c == '0'
#                 if i > 0 and s[i-1] == '1':
#                     ans += ones
#         return ans

# # leetcode 11
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         left, right = 0, len(height) - 1
#         max_area = 0

#         while left < right:
#             width = right - left
#             current_area = min(height[left], height[right]) * width
#             max_area = max(max_area, current_area)

#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1

#         return max_area 
    
    
# # leetcode 12
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#         ]
#         syms = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#         ]
#         roman_num = ''
#         i = 0
#         while num > 0:
#             for _ in range(num // val[i]):
#                 roman_num += syms[i]
#                 num -= val[i]
#             i += 1
#         return roman_num
    
# # leetcode 13
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_map = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
#         total = 0
#         prev_value = 0

#         for char in reversed(s):
#             value = roman_map[char]
#             if value < prev_value:
#                 total -= value
#             else:
#                 total += value
#             prev_value = value

#         return total
    
    
# # 3234 leetcode
# class Solution:
#     def countGoodSubstrings(self, s: str) -> int:
#         count = 0
#         for i in range(len(s) - 2):
#             substring = s[i:i+3]
#             if len(set(substring)) == 3:
#                 count += 1
#         return count
    
    
# # 1513 leetcode
# class Solution:
#     def numseb(self, s: str) -> int:
#         MOD = 10 ** 9 + 7
#         res = 0
#         cur = 0
        
#         for ch in s:
#             if ch == '1':
#                 cur += 1
#             else:
#                 res += cur * (cur + 1) // 2
#                 cur = 0
#         if cur: res += cur * (cur + 1) // 2
#         return res
    
# # reverse a string without using slicing
# def reverse_string(s:str) -> str:
#     rev = ''
#     for ch in s:
#         rev = ch + rev
#     return rev

# input_str = "Hello world"

# reverse_string = reverse_string(input_str)   

# # print prime numbers 
# def primr_numbers(n:int) -> list[int]:
#     primes = []
#     for num in range(2, n + 1):
#         for i in range(2, int(num ** 0.5)+ 1):
#             if num % i == 0:
#                 break
#         else:
#             primes.append(num)
#     return primes
# prime_list = primr_numbers(100)
# print(prime_list)

# # palindrome check
# num = 121
# rev = 0
# n = abs(num)
# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10
# if rev == abs(num):
#     print(f"{num} is a palindrome")
# else:
#     print(f"{num} is not a palindrome")

# # fibonacci series

# n = 10
# a, b = 0, 1
# for _ in range(n):
#     print(a, end = " ")
#     a, b = b, a + b
    
# # armstorng number check
# # an armstorng 
# num = 153
# order = len(str(num))
# s = sum(int(d) ** order for d in str(num))
# if s == num:
#     print(f"{num} is an armstrong number")
# else:
#     print(f"{num} is not an armstrong number")

# # calculater
# print("Simple Calculater")
# print("Selct opertion: +, -, *, /")

# choice = input("Enter opertions: ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))    

# if choice == '+':
#     print(f"{num1} + {num2} = {num1 + num2}")
# elif choice == '-':
#     print(f"{num1} - {num2} = {num1 - num2}")
# elif choice == '*':
#     print(f"{num1} * {num2} = {num1 * num2}")
# elif choice == '/':
#     if num2 != 0:
#         print(f"{num1} / {num2} = {num1 / num2}")
#     else:
#         print("Error: Division by Zero")
# else:
#     print("Invalid operation")
    
# # leetcode 717
# class Solution:
#     def isOneBitCharacter(self, bits: List[int]) -> bool:
#         n = len(bits)
#         i = 0

#         while i < n - 1:
#             if bits[i] == 0: i += 1
#             else: i += 2
#         return i == n - 1
    
# # add list of numbers
# def add_numbers(nums: list[int]) -> int:
#     total = 0
#     for num in nums:
#         total += num
#     return total

# numbers = [1,2,3,4,5,6,7]
# result = add_numbers(numbers)
# print(f"sum of {numbers} is {result}")

# #PRINTING PATTERN
# for i in range(1, 6):
#     print("*" * i)

# i =0 *
# i =1 **
# i =2 * 
#
#

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j , end = '')
#     print()

# # square pattern
# n = 9
# for i in range(n):
#     for j in range(n):
#         print("*", end = ' ') 
#     print()
    
# # left triangle pattern

# n = 5
# for i in range(n):
#     for  j in range(n):
#         print("*", * i)
#     print()
    
# for i in range(1, 6):
#     print("*" * (6 - i))
  
  
# n = 5 
# for i in range(n):
#     for j in range(i, n):
#         print("*", end = " ")
#     print()
    

# class Solution:
#     def findFinalValue(self, nums: List[int], original: int) -> int:
#         s = set(nums)
#         while original in s:
#             original *= 2
#         return original
      
      
#
# class Solution:
#     def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
#         adj = defaultdict(list)
#         for a, b in connections:
#             adj[a].append(b)
#             adj[b].append(a)

#         def dfs(id, pg_id):
#             seen.add(id)
#             pg.append(id)
#             id_pg[id] = pg_id

#             for nei in adj[id]:
#                 if  nei not in seen:
#                     dfs(nei, pg_id)

#         seen = set()

#         id_pg = {}
#         pgs = {}
#         pgs_s = {}
#         pg_id = 1


#         for id in range(1, c + 1):
#             if id in seen: continue
#             pg = []
#             dfs(id, pg_id)
#             pgs_s[pg_id] = set(pg)

#             heapq.heapify(pg)
#             pgs[pg_id] = pg
#             pg_id += 1

#         res = []
#         for t, id in queries:
#             pgi = id_pg[id]
#             pg_set = pgs_s[pgi]
#             pg_heap = pgs[pgi]

#             if t == 1:
#                 if id in pg_set:
#                     res.append(id)
#                 else:
#                     while pg_heap and not pg_heap[0] in pg_set: heapq.heappop(pg_heap)
#                     if pg_heap: res.append(pg_heap[0])
#                     else: res.append(-1)
#             else:
#                 if id in pg_set: pg_set.remove(id)

#         return res
    
#
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end = " ")
#     print()    
    
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*", end = " ")
#     print()    

# n = 5
# for i in range(n):
#     for j in range(i,5):
#         print("*", end = " ")
#     print()

# n = 7
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))

# n = 7
# for i in range(n):
#     print(" ", end = " ")
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i or i == n - 1:
#             print("*", end = "")
#         else:
#             print(" ", end = "")
#     print()

# # leetcode 11
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         left, right = 0, len(height) - 1
#         max_area = 0

#         while left < right:
#             width = right - left
#             current_area = min(height[left], height[right]) * width
#             max_area = max(max_area, current_area)

#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1

#         return max_area
    
    
# # leetcode 12
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#         ]
#         syms = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#         ]
#         roman_num = ''
#         i = 0
#         while num > 0:
#             for _ in range(num // val[i]):
#                 roman_num += syms[i]
#                 num -= val[i]
#             i += 1
#         return roman_num


# # leetcode 1016
# class Solution:
#     def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
#         n = len(nums)
#         res = []
#         pre = 0

#         for x in nums:
#             pre = (pre << 1) | x
#             res.append(pre % 5 == 0)
#         return res
    
# # # Part A: Loops
# # # 1
# # for i in range(1, 11):    
# #     print(i)

    
# # # 2
# # n = int(input())
# # for i in range(1, n + 1):
# #     print(i)

# #leetcode 1096
# class Solution:
#     def smallestRepunitDivByK(self, k: int) -> int:
#         n = 0
#         for i in range(1, k + 1):
#             n = (n * 10 + 1) % k
#             if n % k == 0: return i
#         return -1

# # # 3
# for i in range(10, 0,-1):
#     print(i)

# # # 4
# n = int(input())
# for i in range(n , 0, -1):
#     print(i)
    
# # 5
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)
        
# what is loops:
# loops are used to repeat a block of code multiple time until a certain condition is met.

# Types of loops in python:
# 1. for  loop:
# definition:  A for loop is used to iterate a swquence (like a  list, tuple, dictionary, set, or string) or other iterable objects:
#for(start, end, step):
    # code block to be executed
    
# syntax:

# for  item in variables:
#   # code block to be executed
# example: 
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)
    
# 2. while loop:
# defination: A while  loop repeatedly executes a block of code as long as a specified condition is true.
# syntax: 
# while condion:
#   # code block to be executed:
# example:
# fruits = ['apple', 'banana', 'cherry']
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1
    
# explain the example:
# In this example, we have a list of fruits. We initialize a variable i to 0, 
# which will be used as an index to access elements in the list. The while loop checks 
# if i is less than the length of the fruits list. If the condition is true, 
# it prints the fruit at index i and then increments i by 1.
# This process continues until i is no longer less than the length of the list, 
# at which point the loop terminates.

# 3. Nested loops:
# defination: A nested loop is a loop inside another loop. The inner loop is excuted completely 
# for each iteration of the outer loop.
# syntax:
# for item1 in variables:
#   for item2 in variables:
#      code block to be excuted
# example: 
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"i: {i}, j: {j}")
    

# explain the example:
# In this example, we have two nested for loops. The outer loop iterates over the
# values of i from 1 to 3, and for each value of i, the inner loop iterates over
# the values of j from 1 to 3. The print statement inside the inner loop    
# displays the current values of i and j for each iteration. This results in a total
# of 9 print statements, as the inner loop runs 3 times for each of the
# 3 iterations of the outer loop.

## loops problems:
''' 1. Print numbers from 1 to 10 using a loop
2. Print even numbers from 1 to 50
3. Print the multiplication table of any number
4. Print the sum of first N natural numbers
5. Count digits in a number using a loop
6. Reverse a number using a loop
7. Print characters of a string one by one
8. Count vowels in a string
9. Find factorial of a number
10. Print Fibonacci series of N numbers '''

# # 01
# for i in range(1, 11):
#     print(i)
    
# # 02
# list_even = []
# for i in range(1, 51):
#     if i % 2 == 0:
#         list_even.append(i)
# print(list_even)

# # 03
# # n = 9
# # for i in range(1, 11):
# #     print(f"{n} * {i} = { n * i }")
# n = 9
# print(*[f"{n} * {i} = { n * i } " for i in range(1, 11)], sep='\n')

# # 04
# n = int(input("Enter the number: "))
# sum_n = 0
# for i in range(1, n +1):
#     sum_n += i
# print(f"sum of first {n} natural numbers is {sum_n}")

# # 05
# num = int(input("Enter a number: "))
# count = 0
# n = abs(num)
# while n > 0:
#     count += 1
#     n //= 10
# print(f"number of digits in {num} is {count}")

# # 06
# num = int(input("Enter the number: "))
# rev = 0
# n = abs(num)
# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10
# if num < 0:
#     rev = -rev
# print(f"Reverse of {num} is {rev}")

# # 07
# s = input("Enter the string: ")
# for ch in s:
#     print(ch)
    
# # 08
# s = input("Enter the string: ")
# vowels, constants = 0, 0
# vowels_check = 'aeiou'
# for ch in s.lower():
#     if ch.isalpha():
#         if ch in vowels_check:
#             vowels += 1
#         else:
#             constants += 1
# print(f"vowels: {vowels}, constants: {constants}")

# # 09
# num = int(input("Enter the number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print(f"factorial of {num} is {fact}")


# # 10
# m = int(input("Enter the number of terms: "))
# a, b = 0, 1
# for _ in range(m):
#     print(a, end = " ")
#     a, b = b, a + b 
# print(f" Fibonacci series of {m} terms printed.")

'''
11. Find the largest digit in a number
12. Check if a number is prime using a loop
13. Print all prime numbers between 1–100
14. Print pattern:
*
**
***
****

15. Print reverse pattern:
****
***
**
*

16. Sum of digits of a number
17. Count how many times a character appears in a string
18. Check if a string is palindrome using loops
19. Find GCD of two numbers using loops
20. Print all numbers divisible by 3 and 5 between 1–200

'''

# # 11
# num = int(input("Enter the number: "))
# max_digit = 0
# n = abs(num)
# while n > 0:
#     digit = n % 10
#     if digit > max_digit:
#         max_digit = digit
#     n //= 10
# print(f"Largest digit in {num} is {max_digit}")

# # 12
# num = int(input("Enter the number: "))
# is_prime = True
# if num <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
# if is_prime:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

#3**0.5 + 1 = 2.732...
#
# # 13 print prime numbers between 1 to n
# n = int(input("Enter the number: "))
# primes = []
# for num in range(2, n + 1):
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         primes.append(num)
# print(f"prime numbers between 1 to {n} are: {primes}")

# # 14
# n = 5
# for i in range(1, n):
#     print("*" * i)
    
# # 15
# n = 5
# for i in range(n, 0, -1):
#     print("*" * i)  
    
# # 16
# n = int(input("Enter the number: "))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n //= 10
# print(f"Sum of digits is {sum}")


# # 17
# s = input("Enter the string: ")
# ch = input("Enter the character to count: ")
# count = 0
# while True:
#     index = s.find(ch)
#     if index == -1:
#         break
#     count += 1
#     s = s[index + 1:]
    
# print(f"Character '{ch}' appears {count} times in the string.")

# # 18
# s = input("Enter the string: ")
# is_palindrome = True
# length = len(s)
# for i in range(length // 2):
#     if s[i] != s[length - i - 1]:
#         is_palindrome = False
#         break
# if is_palindrome:
#     print(f'"{s}" is a palindrome')
# else:
#     print(f'"{s}" is not a palindrome')
            

# # 19
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))  
# a, b = num1, num2
# while b != 0:   
#     a, b = b, a % b
# gcd = a
# print(f"GCD of {num1} and {num2} is {gcd}")


# # 20
# divisible_numbers = []
# for i in range(1, 201): 
#     if i % 3 == 0 and i % 5 == 0:
#         divisible_numbers.append(i)
# print(f"Numbers divisible by 3 and 5 between 1 to 200 are: {divisible_numbers}")

     
'''
21. Remove duplicates from a list using loops only (do not use set()).
22. Find the frequency of each element in a list using loops.
23. Find the second largest number in a list using loops (no built-in functions like max()).
24. Print the following pattern using loops:
1
12
123
1234

25. Write a program to check if a number is an Armstrong number using loops.
26. Print all Armstrong numbers between 1 and 1000 using loops.
27. Count the number of words in a sentence without using split().
28. Create a menu-driven program (ATM-like) using loops to perform:

Check Balance

Deposit

Withdraw

Exit

29. Create an infinite loop that stops only when the user types “exit”.
30. Write a program to find the longest word in a sentence using loops (no split()).
'''

# # 21
# nums = [1, 2, 2, 3, 4, 4, 5]
# unique_nums = []
# for num in nums:
#     if num not in unique_nums:
#         unique_nums.append(num) 
# print(f"List after removing duplicates: {unique_nums}")

# # 22
# n = [1, 2, 2, 3, 4, 4, 5]
# frequency = {}
# for num in n:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1
# print(f"Frequency of each element: {frequency}")

# # 23
# nums = [10, 20, 4, 45, 99]
# first = second = float('-inf')
# for num in nums:    
#     if num > first:
#         second = first
#         first = num
#     elif num > second and num != first:
#         second = num
# print(f"Second largest number is {second}")

# # 24
# n = 5
# for i in range(1, n):
#     for j in range(1, i + 1):
#         print(j, end = '')
#     print()
    

# # 25
# n = int(input("Enter the number: "))
# sum = 0
# temp = n
# order = len(str(n))
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** order
#     temp //= 10
# if sum == n:
#     print(f"{n} is an Armstrong number")
# else:
#     print(f"{n} is not an Armstrong number")
      
      
# # 26
# armstorng_numbers = []
# for num in range(1, 1001):
#     sum = 0
#     order = len(str(num))
#     temp = num
    
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
        
# if sum == num:
#     armstorng_numbers.append(num)
# print(f"armstorng numbers between 1 to 1000 are: {armstorng_numbers}")

# # 27
# sentence = input("Enter the sentence: ")
# count = 0
# in_word = False
# for ch in sentence:
#     if ch != ' ' and not in_word:
#         count += 1
#         in_word = True
#     elif ch == ' ':
#         in_word = False
# print(f"Number of words in the sentence: {count}")


    
# # 28
# balance = 0
# while True:
#     print("\nMenu:")
#     print("1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Exit")
    
#     choice = input("Enter your choice (1-4): ")
    
#     if choice == '1':
#         print(f"Your current balance is: ${balance}")
#     elif choice == '2':
#         amount = float(input("Enter amount to deposit: "))
#         balance += amount
#         print(f"${amount} deposited successfully.")
#     elif choice == '3':
#         amount = float(input("Enter amount to withdraw: "))
#         if amount > balance:
#             print("Insufficient balance.")
#         else:
#             balance -= amount
#             print(f"${amount} withdrawn successfully.")
#     elif choice == '4':
#         print("Exiting the program. Thank you!")
#         break
#     else:
#         print("Invalid choice. Please try again.")

# # 29
# while True:
#     command = input("Type 'exit' to stop the loop: ")
#     if command.lower() == 'exit':
#         print("Exiting the loop. Goodbye!")
#         break
    
    
# # 30
# sentence = input("Enter the sentence: ")
# longest_word = ''
# current_word = ''
# for ch in sentence:
#     if ch != ' ':
#         current_word += ch
#     else:
#         if len(current_word) > len(longest_word):
#             longest_word = current_word
#         current_word = ''
# if len(current_word) > len(longest_word):
#     longest_word = current_word
# print(f"The longest word in the sentence is: '{longest_word}'")

# # # leetcode 5
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def expand_around_center(left: int, right: int) -> str:
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return s[left + 1:right]


# hello#         longest = ''

# class Solution:
#     def countTriples(self, n: int) -> int:
#         res = 0

#         for i in range(1, n + 1):
#             for j in range(i + 1, n + 1):
#                 k = int(sqrt(i**2 + j**2))
#                 if k <= n and i**2 + j**2 == k**2:
#                     res += 2
#         return res
    
    
# # leetcode 6
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1 or numRows >= len(s):
#             return s

#         rows = [''] * numRows
#         current_row = 0
#         going_down = False

#         for char in s:
#             rows[current_row] += char
#             if current_row == 0 or current_row == numRows - 1:
#                 going_down = not going_down
#             current_row += 1 if going_down else -1

#         return ''.join(rows)
    
# # # leetcode 474

# class Solution:       
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
        
#         for s in strs:
#             zeros = s.count('0')
#             ones = s.count('1')
            
#             for i in range(m, zeros - 1, -1):
#                 for j in range(n, ones - 1, -1):
                    # dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)   
    

# class Solution:       
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
        
#         for s in strs:
#             zeros = s.count('0')
#             ones = s.count('1')
            
#             for i in range(m, zeros - 1, -1):
#                 for j in range(n, ones - 1, -1):
#                     dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)   
    
    


# class Solution:       
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
        
#         for s in strs:
#             zeros = s.count('0')
#             ones = s.count('1')
            
#             for i in range(m, zeros - 1, -1):
#                 for j in range(n, ones - 1, -1):
#                     dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)   
                    
# class Solution:       
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
        
#         for s in strs:
#             zeros = s.count('0')
#             ones = s.count('1')
            
#             for i in range(m, zeros - 1, -1):
#                 for j in range(n, ones - 1, -1):
#                     dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)   
                    
# class Solution:       
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
        
#         for s in strs:
#             zeros = s.count('0')
#             ones = s.count('1')
            
#             for i in range(m, zeros - 1, -1):
#                 for j in range(n, ones - 1, -1):
#                     dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)   

# class Solution:       
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
        
#         for s in strs:
#             zeros = s.count('0')
#             ones = s.count('1')
            
#             for i in range(m, zeros - 1, -1):
#                 for j in range(n, ones - 1, -1):
#                     dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)   

# # leetcode 9
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False    
#         original = x
#         rev = 0
#         while x > 0:

#             rev = rev * 10 + x % 10
#             x //= 10        
#         return rev == original
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         original = x
#         rev = 0
#         while x > 0:
#             rev = rev * 10 + x % 10
#             x //= 10
#         return rev == original


# num = int(input("Enter the number:"))

# if num <= 1:
#     print(f"{num} is not a prime number")
    
# else: 
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(f"{num} is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
    
# class Solution:
#     def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
#         rows = defaultdict(lambda: [n, 0])
#         cols = defaultdict(lambda: [n, 0])

#         for c, r in buildings:
#             rows[r][0] = min(rows[r][0], c)
#             rows[r][1] = max(rows[r][1], c)

#             cols[c][0] = min(cols[c][0], r)
#             cols[c][1] = max(cols[c][1], r)

#         res = 0
#         for c, r in buildings:
#             if rows[r][0] < c < rows[r][-1] and cols[c][0] < r < cols[c][-1]:
#                 res += 1
#         return res


# # # leetcode 12
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#         ]
#         syms = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#         ]
#         roman_num = ''
#         i = 0
#         while num > 0:
#             for _ in range(num // val[i]):
#                 roman_num += syms[i]
#                 num -= val[i]   

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key = lambda x: x[0], reverse = True)
        events.sort(key = lambda x: int(x[1]))
        mentions = [0] * numberOfUsers
        offline = defaultdict(int)

        for event, time, user in events:
            if event == 'OFFLINE': offline[int(user)] = int(time) + 60
            else:
                if user == 'ALL':
                    for u in range(numberOfUsers):
                        mentions[u] += 1
                elif user == 'HERE':
                    for u in range(numberOfUsers):
                        if offline[u] <= int(time): mentions[u] += 1
                else:
                    curr = user.split()
                    for u in curr:
                        u = int(u[2:])
                        mentions[u] += 1
        return mentions