# from typing import List
# from collections import defaultdict
# import heapq

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

# # # square pattern
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
      
      
# 26
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

# class Solution:
#     def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
#         events.sort(key = lambda x: x[0], reverse = True)
#         events.sort(key = lambda x: int(x[1]))
#         mentions = [0] * numberOfUsers
#         offline = defaultdict(int)

#         for event, time, user in events:
#             if event == 'OFFLINE': offline[int(user)] = int(time) + 60
#             else:
#                 if user == 'ALL':
#                     for u in range(numberOfUsers):
#                         mentions[u] += 1
#                 elif user == 'HERE':
#                     for u in range(numberOfUsers):
#                         if offline[u] <= int(time): mentions[u] += 1
#                 else:
#                     curr = user.split()
#                     for u in curr:
#                         u = int(u[2:])
#                         mentions[u] += 1
#         return mentions

# from typing import List

# class Solution:
#     def validateCoupons(
#         self,
#         code: List[str],
#         businessLine: List[str],
#         isActive: List[bool]
#     ) -> List[str]:

#         # Business line priority
#         priority = {
#             "electronics": 0,
#             "grocery": 1,
#             "pharmacy": 2,
#             "restaurant": 3
#         }

        # # Function to validate coupon code
        # def is_valid_code(s: str) -> bool:
        #     if not s:
        #         return False
        #     for ch in s:
        #         if not (ch.isalnum() or ch == "_"):
        #             return False
        #     return True

        # valid_coupons = []

        # # Filter valid coupons
        # for i in range(len(code)):
        #     if (
        #         isActive[i]
        #         and businessLine[i] in priority
        #         and is_valid_code(code[i])
        #     ):
        #         valid_coupons.append((businessLine[i], code[i]))

        # # Sort by business line priority, then lexicographically
        # valid_coupons.sort(key=lambda x: (priority[x[0]], x[1]))

        # # Return only coupon codes
        # return [c for _, c in valid_coupons]


# from typing import List

# class Solution:
#     def validateCoupons(
#         self,
#         code: List[str],
#         businessLine: List[str],
#         isActive: List[bool]
#     ) -> List[str]:

#         # Business line priority
#         priority = {
#             "electronics": 0,
#             "grocery": 1,
#             "pharmacy": 2,
#             "restaurant": 3
#         }

#         # Function to validate coupon code
#         def is_valid_code(s: str) -> bool:
#             if not s:
#                 return False
#             for ch in s:
#                 if not (ch.isalnum() or ch == "_"):
#                     return False
#             return True

#         valid_coupons = []

#         # Filter valid coupons
#         for i in range(len(code)):
#             if (
#                 isActive[i]
#                 and businessLine[i] in priority
#                 and is_valid_code(code[i])
#             ):
#                 valid_coupons.append((businessLine[i], code[i]))

#         # Sort by business line priority, then lexicographically
#         valid_coupons.sort(key=lambda x: (priority[x[0]], x[1]))

#         # Return only coupon codes
#         return [c for _, c in valid_coupons]

# class Solution:
#     def numberOfWays(self, corridor: str) -> int:
#         MOD = 10**9 + 7
#         n = len(corridor)

#         s = 0
#         for x in corridor:
#             if x == 'S': s += 1
#         if not s or s % 2 == 1: return 0

#         res = 1
#         l = 0
#         while l < n:
#             r = l
#             s = 0
#             while r < n and s < 2:
#                 if corridor[r] == 'S': s += 1
#                 r += 1

#             p = 0
#             while r < n and corridor[r] == 'P':
#                 p += 1
#                 r += 1

#             if r != n and p: res = (res * (p + 1)) % MOD
#             l = r
#         return res


#
# class Solution:
#     def getDescentPeriods(self, prices: List[int]) -> int:
#         n = len(prices)
#         res  = 0
#         l = 0

#         while l < n:
#             r = l + 1
#             while r < n and prices[r] == prices[r - 1] - 1:
#                 r += 1
#             res += comb(r - l + 1, 2)
#             l = r

#         return res
# from functools import lru_cache

# class Solution:
#     def maxProfit(self, n, present, future, hierarchy, budget):
#         g = [[] for _ in range(n)]
#         for u, v in hierarchy:
#             g[u - 1].append(v - 1)

#         def merge(dp1, dp2):
#             new = [0] * (budget + 1)
#             for i in range(budget + 1):
#                 if dp1[i] == 0 and i != 0:
#                     continue
#                 for j in range(budget - i + 1):
#                     if dp2[j] == 0 and j != 0:
#                         continue
#                     new[i + j] = max(new[i + j], dp1[i] + dp2[j])
#             return new

#         @lru_cache(None)
#         def dfs(u):
#             # dp when parent NOT bought
#             dp0 = [0] * (budget + 1)
#             # dp when parent bought (discount allowed)
#             dp1 = [0] * (budget + 1)

#             for v in g[u]:
#                 c0, c1 = dfs(v)
#                 dp0 = merge(dp0, c0)
#                 dp1 = merge(dp1, c1)

#             res0 = dp0[:]   # not buying u
#             res1 = dp0[:]   # buying u

#             full = present[u]
#             half = present[u] // 2

#             profit_full = future[u] - full
#             profit_half = future[u] - half

#             for b in range(budget - full + 1):
#                 res0[b + full] = max(
#                     res0[b + full],
        #             dp1[b] + profit_full
        #         )

        #     for b in range(budget - half + 1):
        #         res1[b + half] = max(
        #             res1[b + half],
        #             dp1[b] + profit_half
        #         )

        #     return res0, res1

        # return max(dfs(0)[0])



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

# num = int(input("Enter the number: "))
# factorial = 1
# for i in range(1, num +1):
#     factorial *= i
# print(f"THe factorial of {num} is {factorial}")

# print list of numbers in ascending order
# n = int(input("Enter the number of elements:"))
# numbers = []
# for i in range(n):
#     num = int(input(f"Enter number {i + 1}: "))
#     numbers.append(num)
# numbers.sort()
# print("Numbers in ascending order:")
# for num in numbers:
#     print(num)  
    
# num = int(input("enter the number: "))
# count = 0
# n = abs(num)
# if n == 0:
#     count = 1
# while n > 0:
#     count += 1
#     n //= 10
# print(f"number of digits in {num} is {count}")



# num = int(input("Enter the number: "))
# is_prime = True
# if num <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(num ** 0.5)+ 1):
#         if num % i == 0:
#             is_prime = False
#             break
# if is_prime:
#     print(f"{num} is a prime number")
            
# else:
#     print(f"{num} is not a prime number")

#print all prime numbers between 1 to 100
# primes = []
# for num in range(2, 100):
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         primes.append(num)
# print(f"prime numbers betwwen 1 to 100 are : {primes}")
    
    
# num = int(input("enter the number: "))
# rev = 0
# n = abs(num)

# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10
#     if num < 0:
#         rev = -rev
# print(f"revers of {num} is {rev}")
    
    
# num = [1,0,1,1,1]
# pre = 0
# res = []
# for x in num:
#     pre = (pre << 1) | x
#     res.append(pre)
# print(res)
# # from typing import List
# # class Solution:

# # #955 leetcode
# # def minDeletionSize(self, strs: List[str]) -> int:
# #     n = len(strs)
# #     m = len(strs[0])
# #     count = 0

# #     for j in range(m):
# #         for i in range(1, n):
# #             if strs[i][j] < strs[i - 1][j]:
# #                 count += 1
# #                 break

# #     return count

# class Solution:
#     def minDeletionSize(self, strs: List[str]) -> int:
#         cols = len(strs[0])
#         rows = len(strs)
#         dp = [1] * cols

#         for c1 in range(cols -2, -1, -1):
#             for c2 in range(c1 + 1, cols):
#                 valid = True
#                 for r in range(rows):
#                     if strs[r][c1] > strs[r][c2]:
#                         valid = False
#                         break

#                 if valid: dp[c1] = max(dp[c1], 1 + dp[c2])

#         return cols - max(dp)


# print(sum(i for i in range(0, 101)))

# print(*[i for i in range(0, 101)], sep = ', ')

# print(*[i*i for i in range(1, 11)], sep = ', ')

# print(*[i for i in range(1, 51) if i % 2 == 0], sep = ' , ')

# print(*[i for i in range(1, 51) if i % 2 != 0], sep = ' , ')

# print(*[i for i in range(1, 51) if i % 3 == 0 and i % 5 == 0], sep = ' , ')

# print(*[i for i in range(2, 101) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))], sep = ' , ')

# print(*['*' * i for i in range(1, 6)], sep = '\n')

# print(*['*' * i for i in range(6, 0 , -1)], sep = ' \n')

# print(*['*' * i for i in range(1,17) if i == 3 or i == 5], sep = '\n')

# for i in range(1, 6):
#     print("*" * (6 - i) +" " * ((i-1)*2) + "*" * (6 - i))
    
    
# ********
# ***  ***
# **    **
# *      *
# *      *
# **    **
# ***  ***
# ********

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"i: {i}, j: {j}")
# The outer loop iterates over the


# for i in range(1,8):
#     for j in range(1, 8):
#         if i == 1 or i == 7 or j == 1 or j ==7 or i == j or j == 8 - i:
#             print("*", end = "")
#         else:
#             print(" ", end = "")
#     print()
    
# for i in range(1,6):
#     print("*" * i)
# for j in range(1,5):
#     print("*" * (5-j))
# for i in range(1,8):
#     print(" " * (5 - i)*2 + "*" * i )
# for j in range(1, 7):
#     print(" " * j * 2 + "*" * (5 - j))
    
    
    
# for i in range(1,6):
#     print("*" * i)
# for j in range(1,6):
#     print(" " * (5-j)*2 + "*" * j)

    
# def number(num):
#     for i in range(1, num +1):
#         if i == num:
#             print("*" * (2 * num))
#         else:
#             print("*" * i + " " * (2 * (num - i) + 1) + "*" * i)
            
#     for i in range(num -1, 0, -1):
#         print("*" * i + " " * (2 * (num-i) + 1) + "*" * i) 

# number(6)


# print(*['*' * i for i in range(6, 0 , -2)], sep = ' \n')


# def pattern(n):
#     for i in range(1, n + 1):
#         for j in range(1, n +1):
#             if i == 1 or i == n or j == 1 or j == n:
#                 print("*", end = " ")
#             else:
#                 print(" ", end = " ")
#         print()
# pattern(5)

# def pattern(n):
#     for i in range(1, n +1):
#         for j in range(1, n +1):
#             if i == j or j == n - i + 1:
#                 print("*", end = " " )
#             else: 
#                 print(" ", end= " ")
#         print()
# pattern(5)

# print v pattern
# def pattern(n):
#     for i in range(1, n + 1):
#         for j in range(1, n * 2):
#             if j == i or j == (2 * n - i):
#                 print("*", end = " ")
#             else:
#                 print(" ", end = " ")
#         print()
# # pattern(4)

# def pattern(n):
#     for i in range(1, n + 1):
#         for j in range(1, n * 2):
#             if j == (n - i + 1) or j == ((n + i)-1) or (i == n//2 + 1 and j > n - i + 1 and j < n + i - 1):
#                 print("*", end = " ")
#             else:
#                 print(" ", end = " ")
#         print()
# pattern(6)


# def pattern(n):
#     for i in range(1, n +1):
#         for j in range(1, n +1):
#             if j == 1 or (i == 1 and j < n) or (j == n and i != 1 and i != n//2 + 1 and i != n) or (i == n and j < n) or (i == n//2+1 and j < n):
#                 print("*", end = " ")
#             else:
#                 print(" ", end = " ")
#         print()
# pattern(5) 


# def pattern(n):
#     for i in range(1, n +1):
#         for j in range(1, n + 1):
#             if (j == 1) or (i == 1) or (i == n):
#                 print("*", end = " ")
#             else:
#                 print(" ", end = " ")
#         print()
# pattern(6)


# def maltiply_table(n):
#     for j in range(1, 11):
#         print(f"{n} * {j} = { n * j}",  end = "\n" )        
# maltiply_table(5)


# def factorial(n):
#     fact = 1
#     for i in range(1, n +1):
#         fact *= i
#     print(f"The factorial of {n} is {fact}")
# factorial(5)


# def largest_digit(n):
#     max_digit = 0
#     n = abs(n)
#     while n > 0:
#         digit = n % 10
#         if digit > max_digit:
#             max_digit = digit
#         n //= 10
#     print(f"the largest digit is {max_digit}")

# largest_digit(12)


# def smallest_digit(n):
#     n = abs(n)
#     if n==0:
#         print("The smallest digit is 0")
#         return
#     min_digit = 9
#     while n > 0:
#         digit = n % 10
#         if digit < min_digit:
#             min_digit = digit
#         n //= 10
#     print(f"The smallest digit is {min_digit}")
# smallest_digit(1223)

# def reverse_number(n):
#     rev = 0
#     n = abs(n)
#     while n > 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n //= 10
#     print(f"The reverse number is {rev}")
# reverse_number(1234) 

# def count_digits(n):
#     count = 0
#     n = abs(n)
#     if n == 0:
#         count = 1
#     while n > 0:
#         count += 1
#         n //= 10
#     print(f"The number of digits is {count}")
# count_digits(123456)

# def sum_of_digits(n):
#     sum = 0
#     n = abs(n)
#     while n > 0:
#         digit = n % 10
#         sum += digit
#         n //= 10
#     print(f"sum of digits is {sum}")
# sum_of_digits(123456)
            
            
# def product_of_digits(n):
#     product = 1
#     n = abs(n)
#     while n > 1:
#         digit  = n % 10
#         product *= digit
#         n //= 10
#     print(f"The product of digits  is {product}")
# product_of_digits(1234)

# def average_of_digits(n):
#     sum = 0
#     n = abs(n)
#     if n == 0:
#         print("The average of digits is 0")
#         return
#     count = 0
#     while n > 0:
#         digit = n % 10
#         sum += digit
#         count += 1
#         n //= 10
#     average = sum // count
#     print(f"The average of digits is {average}")
    
# average_of_digits(123456)

# def average_of_digits(n):
#     sum = 0
#     count = 0
#     n = abs(n)
#     digits = str(n)
    
#     for ch in digits:
#         digits = int(ch)
#         sum += digits
#         count += 1
#     average = sum // count
#     print(f"The average of digits is {average}")
    
# average_of_digits(123456)

# # list of prime factors of a number
# def prime_factors(n):
#     factors = []
#     for i in range(2, n +1):
#         if n % i == 0:
#             for j in range(2, int(i ** 0.5) + 1):
#                 if i % j == 0:
#                     break
#             else:
#                 factors.append(i)
#     print(f"The prime factors of {n} are: {factors}")
# prime_factors(28)


# # fibonacci series up to n terms
# def fibonacci_series(n):
#     a, b = 0, 1
#     series = []
#     for _ in range(n):
#         series.append(a)
#         a, b = b+a, a
#     print(f"The fibonacci series up to {n} terms is: {series}")
    
# fibonacci_series(12)


# def feb(n):
#     a,b = 0,1
#     series = []
#     for _ in range(n):
#         a, b = b+a, a
#         series.append(a)
#     print("The fibonacci series is:", series)
# feb(10)


# # code to remove duplicates from a list
# nums = [1,2,3,2,4,5,1,6]
# uniquw_nums = list(set(nums))
# print(f"The list after removiing duplicates is: {uniquw_nums}")


# # list to store frequency of each element
# nums = [1,2,2,3,4,4,4,5]
# freq = {}
# for num in nums:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# print(f"The frequency of each element is: {freq}")

# #maximum and minimum number in a list
# nums = [3,5,1,8,2,7]
# max_num = max(nums)
# min_num = min(nums)
# print(f"the maximum and minimum number in this list are: {max_num}, {min_num}")

# # sum of all elements in a list 
# nums = [1,2,3,4,5,7,8]
# total = sum(nums)
# print(f"The sum of all elements in the list is: {total}")

# # average of elements in a list
# # nums = []
# # n = int(input("Enter the number of elements: "))
# # for i in range(n):
# #     num = int(input(f"Enter number {i + 1}: "))
# #     nums.append(num)
# # average = sum(nums) / n
# # print(f"The average of elements in the list is: {average}")

# # matrix addition 2*2 matrix
# matrix1 = [[1,2], [3,4]]
# matrix2 = [[5,6], [7,8]]
# result = [[0,0], [0,0]]
# for i in range(len(matrix1)):
#     for j in range(len(matrix1[0])):
#         result[i][j] = matrix1[i][j] + matrix2[i][j]    
# print(f"The result of matrix addition is: {result}")


# armstrong numbers between 1 to 1000


# for num in range(1, 1001):
#     order = len(str(num))
#     sum_of_digits = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum_of_digits += digit ** order
#         temp //= 10
#     if sum_of_digits == num:
#         print(f"{num} is an armstrong number")
        
# # simple banking system
# balance = 0.0
# while True:
#     print("\n Welcome to the Banking System")
#     print("1. Check Balance")
#     print("2. Deposite Money")
#     print("3. Withdraw Money")
#     print("4. Exit")
    
#     choice = int(input("Enter your choice (1-4): "))
#     if choice == 1:
#         print("Cureent Balance is: $", balance)
#     elif choice == 2:
#         amount = float(input("Enter the amount to deposite:"))
#         balance += amount
#         print(f"${amount} deposited sucessfully.")
#     elif choice == 3:
#         amount = float(input("Enter the amount to withdraw: "))
#         if amount > balance:
#             print("Insufficicent balance.")
#         else:
#             print(f"${amount} withdraw sucessfully.")
#             balance -= amount
#     elif choice == 4:
#         print("Thank u for using the banking system. GoodBye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")
        
        
# #  calculator program
# while True:
#     print("\n Simple Calculator")
#     print("1. Addition")
#     print("2. Subtrraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
    
    
#     try:
#         choice = int(input("Enter your choice (1-5): "))
#     except ValueError:
#         print("Invalid input. Please enter a number between 1 and 5.")
#         continue
    
#     if choice == 5:
#         print("Thank for using the calculator. GoodBye!")
#         break
    
#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#     except ValueError:
#         print("Invalid input. Please enter numeric values.")
#         continue
    
#     if choice == 1:
#         result = num1 + num2
#         print(f"The result of {num1} + {num2} = {result}")
        
#     elif choice == 2:
#         result = num1 - num2
#         print(f"The result of {num1} - {num2} = {result}")
        
#     elif choice == 3:
#         result = num1 * num2
#         print(f"The result of {num1} * {num2} = {result}")
    
#     elif choice == 4:
#         if num2 == 0:
#             print("Error: Division by zero is not allowed.")
#         else:
#             result = num1 / num2
#             print(f"The result of {num1} / {num2} = {result}")
            
#     else:
#         print("Invalid choice. Please try again.")
        
# # two sum 
# def two_sum(nums, target):
#     nums_map = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in nums_map:
#             return (nums_map[complement], i)
#         nums_map[num] = i
#     return None
# result = two_sum([2,3,4,5,67,7], 9)
# print(result)

# class Solution:
#     def two_sum(self, nums, target):
#         nums_map = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in nums_map:
#                 return (nums_map[complement], i)
#             nums_map[num] = i
#         return None


# # Create object
# sol = Solution()

# # Call method
# result = sol.two_sum([1, 2, 3, 4, 5, 6, 7], 9)
# print(result)

# class Solution:
#     def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         res = 0

#         def valid(i, j):
#             nums = set()

#             # collect numbers in 3x3 grid
#             for r in range(i - 2, i + 1):
#                 for c in range(j - 2, j + 1):
#                     if grid[r][c] < 1 or grid[r][c] > 9:
#                         return False
#                     nums.add(grid[r][c])

#             if nums != set(range(1, 10)):
#                 return False

#             s = grid[i - 2][j - 2] + grid[i - 2][j - 1] + grid[i - 2][j]

#             # check rows
#             for r in range(i - 2, i + 1):
#                 if grid[r][j - 2] + grid[r][j - 1] + grid[r][j] != s:
#                     return False

#             # check columns
#             for c in range(j - 2, j + 1):
#                 if grid[i - 2][c] + grid[i - 1][c] + grid[i][c] != s:
#                     return False

#             # check diagonals
#             if grid[i - 2][j - 2] + grid[i - 1][j - 1] + grid[i][j] != s:
#                 return False
#             if grid[i - 2][j] + grid[i - 1][j - 1] + grid[i][j - 2] != s:
#                 return False

#             return True

#         for i in range(2, n):
#             for j in range(2, m):
#                 if valid(i, j):
#                     res += 1

#         return res

# class Solution:
#     def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
#         def solve(target):
#             grid = [[0] * col for _ in range(row)]
#             for i in range(target):
#                 r, c = cells[i]
#                 grid[r - 1][c - 1] = 1

#             q = deque([])
#             seen = set()
#             for i in range(col):
#                 if grid[0][i] == 0:
#                     q.append((0, i))
#                     seen.add((0, i))

#             while q:
#                 r, c = q.popleft()
#                 if r == row - 1: return True

#                 for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
#                     if nr < 0 or nr >= row or nc < 0 or nc >= col or (nr, nc) in seen: continue
#                     if grid[nr][nc] == 0:
#                         q.append((nr, nc))
#                         seen.add((nr, nc))

#             return False

#         l = 0
#         h = len(cells) - 1

#         while l < h:
#             mid = l + (h -l + 1) // 2
#             if solve(mid): l = mid
#             else: h = mid - 1

#         return l 

# # list combains 
# list_1 = [1,2,3,4,5,6,7,8]
# list_2 = [1,2,3,4,5,6,7,8]
# print(list_1 + list_2)

#index of i list_! + index of i list_2

# result = []
# for i in range(len(list_1)):
#     result.append(list_1[i] + list_2[i])
# print(result)

# result_1 = []
# for i in range(len(list_1)):
#     result_1.append(list_1[i] * list_2[i])
# print(result_1)
    

# for i in range(1,8):
#     print("*" * i)
# for j in range(1,7):
#     print("*" * j)


# for i in range(1,5):
#     print("*")


# class Solution:
#     def sumFourDivisors(self, nums: List[int]) -> int:
#         res = 0

#         for x in nums:
#             div = set()
#             for d in range(1, floor(sqrt(x)) + 1):
#                 if x % d == 0:
#                     div.add(x // d)
#                     div.add(d)
#                     if len(div) > 4: break

#             if len(div) == 4: res += sum(div)

    
#         return res   


# def fibinocies_series(n):
#     a , b = 0, 1
#     series = []
#     for _ in range(n):
#         a, b = b, b+a, 
#         series.append(a)
        
#     print(f"the fibnociess is of {n} is {series}")
# fibinocies_series(12)

# def feb(n):
#     a,b = 0,1
#     series = []
#     for _ in range(n):
#         a, b = b , a+b
#         series.append(a)
#     print("The fibonacci series is:", series)
# feb(10)

## Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxLevelSum(self, root: Optional[TreeNode]) -> int:
#         q = deque([root])
#         mx = -inf
#         res = 0
#         level = 1

#         while q:
#             total = 0
#             for _ in range(len(q)):
#                 n = q.popleft()
#                 total += n.val
#                 if n.left: q.append(n.left)
#                 if n.right: q.append(n.right)

#             if total > mx:
#                 mx = total
#                 res = level
#             level += 1

#         return res

# def pattern(n):
#     for i in range(n):
#         for j in range(n):
#             if i==0 or j==0 or i==n or i==n//2:
#                 print("*", end = ' ')
#             else:
#                 print(" ", end = " ")
                
#         print()
# pattern(7)
# outer = [[]] * 3
# outer[0].append(1)
# print(outer)

# n= 4
# results = []
# for i in range(1, n+1):
#     for _ in range(i):
#         results.append([i])
# print(results)

# l = [1,2,3,4,5,6,True]
# m = l.pop(True)
# print(m)

# l = [1,2,3,4,5,6,True,False]
# m = l.pop(True)
# print(m)
# m_1 = l.remove(True)
# print(m_1)

# class Solution:
#     def minimumDeleteSum(self, s1: str, s2: str) -> int:
#         n = len(s1)
#         m = len(s2)
#         dp = [[0] * (m + 1) for _ in range(n + 1)]

#         for i in range(1, n + 1):
#             dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

#         for j in range(1, m + 1):
#             dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 if s1[i - 1] == s2[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = min(
#                         dp[i - 1][j] + ord(s1[i - 1]),
#                         dp[i][j - 1] + ord(s2[j - 1])

#                     )
#         return dp[-1][-1]

# class Solution:
#     def minimumDeleteSum(self, s1: str, s2: str) -> int:
#         n = len(s1)
#         m = len(s2)
#         dp = [[0] * (m + 1) for _ in range(n + 1)]

#         for i in range(1, n + 1):
#             dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

#         for j in range(1, m + 1):
#             dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 if s1[i - 1] == s2[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = min(
#                         dp[i - 1][j] + ord(s1[i - 1]),
#                         dp[i][j - 1] + ord(s2[j - 1])

#                     )
#         return dp[-1][-1]


# for num in range(1, 1001):
#     power = len(str(num))
#     total = sum(int(d)**power for d in str(num))
#     if total == num:
#         print(num)

# for num in range(1, 1999):
#     power = len(str(num))
#     total = sum(int(d) ** power for d in str(num))
#     if total == num:
#         print(num)
        
# def pattern(n):
#     for i in range(1, n + 1):
#         for j in range(1, n * 2):
#             if j == i or j == (2 * n - i):
#                 print("*", end= '')
#             else:
#                 print(" ", end= '')
#         print()
# pattern(5)

# # print v pattern
# def pattern(n):
#     for i in range(1, n + 1):
#         for j in range(1, n * 2):
#             if j == i or j == (2 * n - i):
#                 print("*", end = " ")
#             else:
#                 print(" ", end = " ")
#         print()
# pattern(4)

# def pattern(n):
#     for i in range(0, n):
#         for j in range(0, n):
#             if i == 0 or i == n//2 or i == n-1:
#                 print("*", end = " ")
#             elif i < n//2 and j == 0:
#                 print("*", end = " ")
#             elif i > n//2 and j == n-1:
#                 print("*", end = " ")
#             else:
#                 print(" ", end = " ")
#         print()
        
# pattern(8)

# n = 4
# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)

# from itertools import count


# n = 4

# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)

# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "* " * i)

# class Solution:
#     def separateSquares(self, squares: List[List[int]]) -> float:
#         xs = set()
#         events = []

#         for x, y, size in squares:
#             xs.add(x)
#             xs.add(x + size)
#             events.append((y, x, x + size, 1))
#             events.append((y + size, x, x + size, -1))

#         xs = sorted(xs)
#         events.sort()
#         st = SegmentTree(xs)

#         # 1️⃣ Compute total area
#         total_area = 0
#         prev_y = events[0][0]

#         for y, xl, xr, op in events:
#             total_area += st.query() * (y - prev_y)
#             st.update(xl, xr, 0, st.n - 1, op, 0)
#             prev_y = y

#         # Reset segment tree
#         st = SegmentTree(xs)

#         # 2️⃣ Find split y
#         acc = 0
#         prev_y = events[0][0]

#         for y, xl, xr, op in events:
#             width = st.query()
#             area = width * (y - prev_y)

#             if acc + area >= total_area / 2:
#                 return prev_y + (total_area / 2 - acc) / width

#             acc += area
#             st.update(xl, xr, 0, st.n - 1, op, 0)
#             prev_y = y


# class Solution:
#     def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
#         m, n = len(mat), len(mat[0])

#         pref = [[0] * (n + 1) for _ in range(m + 1)]
#         for i in range(m):
#             for j in range(n):
#                 pref[i + 1][j + 1] = (
#                     mat[i][j]
#                     + pref[i][j+1]
#                     + pref[i + 1][j]
#                     - pref[i][j]
#                 )

#         def can(k):
#             for i in range(m - k + 1):
#                 for j in range(n - k + 1):
#                     total = (
#                         pref[i + k][j + k]
#                         - pref[i][j + k]
#                         - pref[i + k][j]
#                         + pref[i][j]

#                     )
#                     if total <= threshold:
#                         return True

#             return False

#         left, right, ans = 0, min(m, n), 0
#         while left <= right:
#             mid = (left + right) // 2
#             if can(mid):
#                 ans = mid
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return ans

# class Solution:
#     def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
#         m, n = len(mat), len(mat[0])

#         pref = [[0] * (n + 1) for _ in range(m + 1)]
#         for i in range(m):
#             for j in range(n):
#                 pref[i + 1][j + 1] = (
#                     mat[i][j]
#                     + pref[i][j+1]
#                     + pref[i + 1][j]
#                     - pref[i][j]
#                 )

#         def can(k):
#             for i in range(m - k + 1):
#                 for j in range(n - k + 1):
#                     total = (
#                         pref[i + k][j + k]
#                         - pref[i][j + k]
#                         - pref[i + k][j]
#                         + pref[i][j]

#                     )
#                     if total <= threshold:
#                         return True

#             return False

#         left, right, ans = 0, min(m, n), 0
#         while left <= right:
#             mid = (left + right) // 2
#             if can(mid):
#                 ans = mid
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return ans


# def palindrome(s):
#     return s == s[::-1]
# print(palindrome("madam"))



# def pattern(n):
#     for i in range(n):
#         for j in range(n+1):
#             if j == 0 or i == 0 or j == n or i == n - 1:
#                 print("*", end = " ")
#             else:
#                 print(" ", end = " ")
#         print()
# pattern(5)

# def pattern(n):
#     for i in range(n):
#         print("*" * ( i + 1))
# pattern(5)

# def pattern(n):
#     for i in range(n):
#         for j in range(n):
#             print("*", end = " ")
#         print()
# pattern(5)
        
        
# def pattern(n):
#     for i in range(n):
#         for j in range(n+1):
#             if i == n // 2 and (j == n // 2):
#                 print(" ", end = " ")
#             else:
#                 print("*", end = " ")
#         print()
# pattern(8)

# for i in range(1, 11):
#     print(i)

# for i in range(1, 11):
#     print(i, end = " ")



# Find the nth number of fibonacci number
# def fibonacci(n):
#     if n <= 1:
#         return n 
    
#     prev, curr = 0, 1
#     for _ in range(2, n + 1):
#         prev, curr = curr, prev + curr
        
#     return curr

# n = int(input("Enter n :"))
# print("Fibonacci at index", n, "is", fibonacci(n))


# def prime_factors(n):
#     factors = []
#     for i in range(2, n +1):
#         if n % i == 0:
#             for j in range(2, int(i ** 0.5) + 1):
#                 if i % j == 0:
#                     break
#             else:
#                 factors.append(i)
#     print(f"The prime factors of {n} are: {factors}")
# prime_factors(28)

# def binary_count(arr):
#     return sorted(arr, key=lambda num: (bin(num).count('1'), num))
# # binary_count([0,1,3,4,5,6,7,7,8,9,9,0,0,0,])
# print(binary_count([0,1,3,4,5,6,7,7,8,9,9,0,0,0,]))

# # minimum number of coins to make a given amount
# def min_coins(coins, amount):
#     dp = [float('inf')] * (amount + 1)
#     dp[0] = 0

#     for coin in coins:
#         for x in range(coin, amount + 1):
#             dp[x] = min(dp[x], dp[x - coin] + 1)

#     return dp[amount] if dp[amount] != float('inf') else -1

# print(min_coins([1, 2, 5], 11))


# def find_vehicles(total_vehicles, total_wheels):
#     if total_wheels % 2 != 0:
#         return "Invalid input:"
#     if total_wheels < 2 * total_vehicles or total_wheels > 4 * total_vehicles:
#         return "Invalid input:"
    
#     four_wheelers = (total_wheels - 2 * total_vehicles) // 2
#     two_wheelers = total_vehicles - four_wheelers
    
#     return two_wheelers, four_wheelers

# # print(find_vehicles(10, 28))


# def largestElement_in_array(nums):
#     if not nums:
#         return None
#     Largest = nums[0]
#     for num in nums:
#         if num > Largest:
#             Largest = num
#     return Largest
# print(largestElement_in_array([1,2,3,4,5,6,7,8,9])) 

# def largestElement_in_array(nums):
#     return max(nums) if nums else None
# print(largestElement_in_array([1,2,3,4,5,6,7,8,9]))


# def second_largest(nums):
#     if len(nums) < 2:
#         return None
    
#     first = second = float('-inf')
#     for num in nums:
#         if num > first:
#             second = first
#             first = num
#         elif num > second and num != first:
#             second = num
#         return second if second != float('-inf') else None
# print(second_largest([1,2,3,4,5,6,7,    8,9]))


# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))

# def fibonacci(n):
#     if n <= 1:
#         return n
#     prev, curr = 0, 1
#     list = []
#     for _ in range(2, n + 1):
#         prev, curr = curr, prev + curr
#         list.append(curr)
#     return list
# print(fibonacci(1))

# def feb(n):
#     a,b = 0,1
#     series = []
#     for _ in range(n):
#         a, b = b , a+b
#         series.append(a)
#     print("The fibonacci series is:", series)
# feb(10)


# # example of tree algrothim program explaintion


# def letterCombinations(digits):
#     if not digits:
#         return []
    
#     phone = {
#         "2": "abc", "3": "def", "4": "ghi",
#         "5": "jkl", "6": "mno",
#         "7": "pqrs", "8": "tuv", "9": "wxyz"
#     }
    
#     result = []

#     def backtrack(index, path):
#         # Base case
#         if len(path) == len(digits):
#             result.append(path)
#             return
        
#         # Get letters for current digit
#         letters = phone[digits[index]]
        
#         for letter in letters:
#             backtrack(index + 1, path + letter)

# #     backtrack(0, "")
# #     return len(result)


# # # Example
# # print(letterCombinations("299"))

# # TWO SUM pattern hashmap
# def two_sum(nums, target):
#     nums_map = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in nums_map:
#             return (nums_map[complement], i)
#         nums_map[num] = i   
        
# result = two_sum([2,3,4,5,67,7], 9) 
# print(result)

# # two sum pattern two variable
# def two_sum(nums, target):
#     nums.sort()
#     l, r = 0, len(nums) - 1
#     while l < r:
#         current_sum = nums[l] + nums[r]
#         if current_sum == target:
#             return(l, r)
#         elif current_sum < target:
#             l += 1
#         else:
#             r -= 1
#     return None
# result = two_sum([1,2,3,4,7,75,96,31,1,2,4], 3)

# print(result)   

# # three sum
# def three_sum(nums, target):
#     # nums.sort()
#     for i in range(len(nums) - 2):
#         l , r = i + 1, len(nums) - 1
#         while l < r :
#             complement = nums[i] + nums[l] + nums[r]
#             if complement == target:
#                 return (i, l , r)
#             elif complement < target:
#                 l += 1
#             else:
#                 r -= 1
#     return None
# result = three_sum([1,2,3,4,7,75,96,31,1,2,4], 6)
# print(result)   


# def prime_numbers(n):
#     prime = []
#     for i in range(1, n+1):
#         is_prime = True
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime.append(i)
#     return prime
# print(prime_numbers(100))


# def prime_number(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#         else:
#             return True
# print(prime_number(11))

# # /Time complexity of above code is O(N * SQRT(N)) ans space complexity is O(N) because we are storing the prime numbers in a list.


# def fabanacci(n):
#     a, b = 0, 1
#     series = []
#     for _ in range(n):
#         a, b = b , b + a
#         series.append(a)
#     return series
# print(fabanacci(10))

# # Time complexity of above code is O(N) and space complexity is O(N) because we are storing the series in a list.

# def armstrong(n):
#     power = len(str(n))
#     total = sum(int(a) ** power for a in str(n))
#     return total == n
# print(armstrong(234))

# # Time complexity of above code is O(D) where D is the number of digits in the number and space complexity is O(1) because we are not using any extra space.

# def palindrome(s):
#     return s == s[::-1]
# print(palindrome("madam"))

# # Time complexity of above code is O(N) where N is the length of the string and space complexity is O(1) because we are not using any extra space.

# def palindrome(s):
#     Left, Right = 0, len(s) - 1
#     while Left < Right:
#         if s[Left] != s[Right]:
#             return False
#         Left += 1
#         Right -= 1
#     return True
# print(palindrome("mada"))

# #  time complexity of above code is O(N) where N is the length of the string and space complexity is O(1) because we are not using any extra space.

# def even_or_odd(n):
#     return "Even" if n % 2 == 0 else "Odd"
# print(even_or_odd(10))

# # Time complexity of above code is O(1) and space complexity is O(1) because we are not using any extra space.

# for i in range(1, 11):
#     print(i, end = " ")
    
# for i in range(0, 8):
#     print("*" * i)
    
# for i in range(1, 8):
#     print("*" * (8 - i))
    
# for i in range(1, 8):
#     print(" " * (8 - i) + "* " * i)

# n = 10
# for i in range(n):
#     for j in range(n):
#         print("*", end = " ")
#     print()

# for i in range(n):
#     for j in range(n):
#         if i == j or j == n - i - 1:
#             print("*", end = "")
#         else:  
#             print(" ", end = "")
#     print() 


# 01 square pattern
# for i in range(n):
#     for j in range(n):
#         print( "*", end = " ")
#     print()

# # 02 Right triange

# for i in range(n):
#     print("*" * (i + 1))
    
# # 03 Inverted right triangle
# for i in range(n):
#     print("*" * (n - i))
    
# # 04 number triange

# for i in range(6):
#     for j in range(i  + 1):
#         print(j + 1, end = " ")
#     print()

# # 05 number triangle

# for i in range(8):
#     for j in range(i + 1):
#         print(i + 1, end = "")
#     print()
    
    
# # 06 pyramid pattern
# n = 8
# for i in range(n):
#     print(" " * (n - i - 1) + "* " * (i + 1))   
      
# # 07 inverted pyramid pattern
# n = 9
# for i in range(n):
#     print(" " * i + " * " * ( n - i))
    
# # 08 diamond pattern
# n = 8
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (i + 1))
# for j in range(n):
#     print(" " * j + "*" * (n - j))


# # diamond pattern
# #    *
# #   ***
# #  *****
# # *******
# #  *****
# #   ***
# #    *

# # floyd's triangle
# n = 10
# num = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(num, end = " ")
#         num += 1
#     print()

# 10 pascal triangle
# n = 5
# for i in range(n):

# trees_example_explanation



# array = [65,25,12,22,11]

# for i in range(len(array)):
#     min_index = i
#     for j in range(i + 1, len(array)):
#         if array[j] < array[min_index]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]
# print(array)

# array = [3,2,1,5]

# for i in range(len(array)):
#     min_index = i
#     for j in range(i + 1, len(array)):
#         if array[j] < array[min_index]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]
# print(array[::-1])


# # count total swaps in selection sort
# array = [3,2,1,5]
# count = 0
# n = len(array)
# for i in range(n):
#     min_index = i
#     for j in range(i + 1, n):
#         if array[j] < array[min_index]:
#             min_index = j
#     if min_index != i:
#         array[i], array[min_index] = array[min_index], array[i]
#         count += 1
# print("Total swaps:", count)

# #  Find the mininum element in the each pass
# count = 0
# array = [6,4,7,3,8,2,8,1]
# for i in range(len(array)):
#     min_index = i
#     for j in range(i+1, len(array)):
#         if array[j] < array[min_index]:
#             min_index = j
#     print(f"pass {i + 1}: minimum element is {array[min_index]}")          
#     if min_index != i:
#         array[i], array[min_index] = array[min_index], array[i]    
#         count += 1

# print("total_swaps:", count)

# # selection sort without using python swap

# array = [6,4,7,3,8,2,8,1]
# n = len(array)
# for i in range(n):
#     min_index = i
#     for j in range(i + 1, n):
#         if array[j] < array[min_index]:
#             min_index = j
#     if min_index != i:
#         temp = array[i]
#         array[i] = array[min_index]
#         array[min_index] = temp
# print(array)

# # Sort Strings Using Selection Sort
# array = ["banana", "apple", "grape", "orange", "kiwi"]

# n= len(array)
# for i in range(n):
#     min_index = i
#     for j in range(i + 1, n):
#         if array[j] < array[min_index]:
#             min_index = j
#     if min_index != i:
#         array[i], array[min_index] = array[min_index], array[i]
        
# print(array)


# # kth smallest number

# array = [7, 10, 4, 3, 20, 15]

# k = 1
# for i in range(len(array)):
#     min_index = i
#     for j in range(i + 1, len(array)):
#         if array[j] < array[min_index]:
#             min_index = j
#     if min_index != i:
#         array[i], array[min_index] = array[min_index], array[i]
#     if i == k - 1:
#         print(f"The {k}th smallest number is: {array[i]}")
#         break


# # print the every pass of selection sort
# def selection_sort(arr,k):
#     n = len(arr)
#     count = 0
    
#     for i in range(n):
#         min_index = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         if min_index != i:
#             arr[i], arr[min_index] = arr[min_index], arr[i]
#             count += 1
#         print(f"pass {i + 1}: {arr}")
#         if i == k -1:
#             print(f"the {k}th smallest number is: {arr[i]}")
# selection_sort([7, 10, 4, 3, 20, 15], 7)
# print("total swaps:", count)

# # bobble sort
# array = [64, 34, 25, 12, 22, 11, 90]
# n = len(array)
# for i in range(n):
#     for j in range((n - i - 1)):
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]
# print("Sorted array is:", array)
# print(n)
# # ascending order
# def bobble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j]> arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# print(bobble_sort([64, 34, 25, 12, 22, 11, 90]))

# #  desending order
# def bobble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# print(bobble_sort([64, 34, 25, 12, 22, 11, 90])[::-1])

# #  count
# def bobble_sort_count(arr):
#     n = len(arr)
#     count = 0
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 count += 1
#     return arr, count
# sorted_array, total_swaps = bobble_sort_count([64, 34, 25, 12, 22, 11, 90])
# print("Sorted array is:", sorted_array)
# print("Total swaps:", total_swaps)

# # print the each case pass
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         # swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j+ 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 # swapped = True
#         print(f"pass {i + 1}: {arr}")
#     return arr
# print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))


# # 
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1]= arr[j+1], arr[j]
#                 swapped = True
#         if not swapped:
#             print(f"array is already sorted at pass {i + 1}")
#             break
#         return arr
# print(bubble_sort([1,2,3,4,5]))

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j+1]:
#                 # arr[j], arr[j+1] = arr[j+1], arr[j]
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
#                 swapped = True
#         if not swapped:
#             print(f"array is already sorted at pass {i + 1}")
#             break
#     return arr
# print(bubble_sort([1,2,3,4,5]))

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True  
#         if not swapped:   
#             print(f"array is already sorted at pass {i + 1}")
#             break  
#     return arr
# print(bubble_sort(["apple", "banana", "grape", "orange", "kiwi"]))


# array = [64, 34, 25, 12, 22, 11, 90]
# n = len(array)
# for i in range(n):
#     insert_index = i
#     current_value = array[i]
#     for j in range(i-1, -1, -1):
#         if array[j] > current_value:
#             array[j+1] = array[j]
#             insert_index= j
#         else:
#             break
#         array[insert_index] = current_value
# print("Sorted array is:", array)
    
    
    

#  Quicksort
# Quicksort is a divide-and-conquer algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively. This process continues until the base case of an empty array or an array with a single element is reached, which is inherently sorted.
#  Descending order
# def partition(arr, low, high):
#     pivot= arr[low]
#     i, j = low-1, high + 1
    
#     while True:
        
#         i += 1
#         while arr[i] < pivot:
#             i += 1
            
#         j -= 1
#         while arr[j] > pivot:
#             j -= 1
            
#         if i >= j:
#             return j
        
#         arr[i], arr[j] = arr[j], arr[i]
        
# def quicksort(arr, low, high):
#     if low < high:
#         p = partition(arr, low, high)
        
#         quicksort(arr, low, p)
#         quicksort(arr, p + 1, high)
        
# if __name__ == "__main__":
#     arr = [10, 7, 8, 9, 1, 5]
#     n = len(arr)
#     quicksort(arr, 0, n - 1)
#     print("Sorted array is:", arr[::-1])  
        
#Count Number of Swaps
# count= 0
# def partition(arr, low, high):
#     global count
#     pivot = arr[low]
#     i, j = low- 1, high + 1
    
#     while True:
#         i += 1
#         while arr[i] < pivot:
#             i += 1
        
#         j -= 1
#         while arr[j] > pivot:
#             j -= 1
            
#         if i >= j:
#             return j 
         
         
#         arr[i], arr[j] = arr[j], arr[i]
#         count += 1
        
# def quicksort(arr, low, high):
#     if low < high:
#         p = partition(arr, low, high)
        
#         quicksort(arr, low, p)
#         quicksort(arr, p+1, high)
        
# if __name__ == "__main__":
#     arr = [10, 7, 8, 9, 1, 5]
#     n = len(arr)
#     quicksort(arr, 0, n - 1)
#     print("Sorted array is:", arr)
#     print("Total swaps:", count)
    
    
# # kth smallest element in an array using quicksort
# def partition(arr, low, high):
#     pivot = arr[low]
#     i, j = low - 1, high + 1
    
#     while True:
#         i += 1
#         while arr[i] < pivot:
#             i += 1
            
#         j -= 1
#         while arr[j] > pivot:
#             j -= 1
        
#         if i >= j:
#             return j
        
#         arr[i], arr[j] = arr[j], arr[i]
        
# def quicksort(arr, low, high):
#     if low < high:
#         p = partition(arr, low, high)
        
#         quicksort(arr, low, p)
#         quicksort(arr, p +1, high)
        
# if __name__ == "__main__":
#     arr = [10, 7, 8, 9, 1, 5]
#     n = len(arr)
#     k = 3
#     quicksort(arr, 0, n - 1)
#     print(f"The {k}rd smallest element is: {arr[k - 1]}")
    
# # counting algrothim

# def counting_sort(arr):
#     max_element = max(arr)
#     count = [0] * (max_element + 1)
    
#     for num in arr:
#         count[num] += 1
        
#     result = []
#     for i in range(len(count)):
#         while count[i] > 0:
#             result.append(i)
#             count[i] -= 1
#     return result


# arr = [4, 2, 2, 8, 3, 3, 1]
# sorted_arr = counting_sort(arr)
# print("Sorted array is:", sorted_arr)   

# arr = [4, 2, 2, 8, 3, 3, 1]
# max_element = max(arr) #find the maximum elememt
# count = [0] * (max_element + 1) # create a count array

# for num in arr:
#     count[num] += 1 # count the frequency of each element
    
# result = []
    
# for i in range(len(count)):
#     while count[i] > 0:
#         result.append(i) #append the element to the result array
#         count[i] -= 1 # decrease the count of the element
# print("Sorted array is:", result)   

# def sort_student_marks(marks):
#     max_mark = max(marks)
#     count = [0] * (max_mark + 1)
#     result = []
    
#     for mark in marks:
#         count[mark] += 1
        
#     for i in range(len(count)):
#         while count[i] > 0:
#             result.append(i)
#             count[i] -= 1
#     return result

# marks = [85, 92, 78, 90, 88, 95, 80]
# sorted_marks = sort_student_marks(marks)
# print("Sorted marks:", sorted_marks)

# # count the frequency of elements
# def count_frequency(arr):
#     max_element = max(arr)
#     count = [0] * (max_element + 1)
#     for num in arr:
#         count[num]  += 1
    
#     for i in range(len(count)):
#         if count[i] > 0:
#             print(i, "->", count[i])
            
# arr = [4, 2, 2, 8, 3, 3, 1]
# count_frequency(arr)


# # duplicate elements in an array
# def find_duplicates(arr):
#     max_element = max(arr)
#     count = [0] * (max_element + 1)
#     duplicates = []
    
#     for num in arr:
#         count[num] += 1
        
#     for i in range(len(count)):
#         if count[i] > 1:
#             duplicates.append(i)
            
#     return duplicates

# arr = [4, 2, 2, 8, 3, 3, 1]
# duplicates =   find_duplicates(arr)
# print("Duplicate elements are:", duplicates)

# #  time complexity of above code is O(N + K) where N is the number of elements in the input array and K is the range of the input values. The space complexity is O(K) because we are using a count array to store the frequency of each element.

# # sort characters in a string
# def sort_characters(s):
#     max_char = max(s)
#     count = [0] * (ord(max_char) + 1)
#     result = []
    
#     for char in s:
#         count[ord(char)] += 1
        
#     for i in range(len(count)):
#         while count[i] > 0:
#             result.append(chr(i))
#             count[i] -= 1
#     return ' '.join(result)
# s = "banana"
# sorted_string = sort_characters(s)
# print("Sorted characters:", sorted_string)

# # relative sorting
# def relative_sort(arr1, arr2):
#     max_element = max(arr1)
#     count = [0] * (max_element + 1)
#     result = []
    
#     for num in arr1:
#         count[num] += 1
        
#     for num in arr2:
#         while count[num] > 0:
#             result.append(num)
#             count[num] -= 1 

#     for i in range(len(count)):
#         while count[i] > 0:
#             result.append(i)
#             count[i] -= 1
    
#     return result  

# arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
# arr2 = [2, 1, 8, 3]
# sorted_arr = relative_sort(arr1, arr2)
# print("Relative sorted array:", sorted_arr)


# Radix sort explanation
# Radix sort is a non-comparative integer sorting algorithm that sorts numbers by processing individual digits. The sorting is done by grouping the numbers based on each digit, starting from the least significant digit to the most significant digit. The algorithm uses a stable sorting algorithm, such as counting sort, to sort the numbers based on each digit.

# def counting_sort(arr, exp):
#     n = len(arr)                                # length of the input array example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] then n will be 8 because there are 8 elements in the array
#     output = [0]* n                             #  output array to store the sorted array ex ample if the input array is [170, 45, 75, 90, 802, 24, 2, 66] then output will be [0,0,0,0,0,0,0,0] because we are initializing the output array with 0 and the length of the output array is same as the input array
#     count = [0]* 10                             # count array to store the count of occurence of each digit example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] then count will be [0,0,0,0,0,0,0,0,0,0] because we are initializing the count array with 0 and the length of the count array is 10 because we are counting the occurence of each digit from 0 to 9
    
#     for i in range(n):                          # count of occurence of each digit in the input array example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] and exp is 1 then the count array will be [1,0,2,0,1,2,1,0,0,0] 
#         index = (arr[i] // exp) % 10            # find the digit at the current exponent position example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] and exp is 1 then the index will be (170 // 1) % 10 = 0 for the first element, (45 // 1) % 10 = 5 for the second element and so on for the rest of the elements in the array
#         count[index] += 1                       # increment the count of the digit in the count array example if the digit is 3 then count[3] will be increment by 1 at the index place of 3 in the count array
        
#     for i in range(1, 10):                      # update the count array to store the cumulative count of each digit example if the count array is [1,0,2,0,1,2,1,0,0,0] then after this loop the count array will be [1,1,3,3,4,6,7,7,7,7] because we are adding the count of the previous digit to the current digit in the count array  why we doing this because we want to know the position of the digit in the output array example if the digit is 3 then we want to know the position of the last occurrence of 3 in the output array so we can place the next occurrence of 3 at the correct position in the output array and this is done by adding the count of the previous digit to the current digit in the count array
#         count[i] += count[i -1]                 # exapmple count[1] = count[1] + count[0] = 0 + 1 = 1, count[2] = count[2] + count[1] = 2 + 1 = 3 and so on for the rest of the digits in the count array
        
#     i = n-1                                     # build the output array example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] and exp is 1 then the output array will be [170, 90, 75, 45, 802, 24, 2, 66] because we are building the output array based on the count array and the input array
#     while i >= 0:                               # find the index of the digit in the count array and place the element in the output array example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] and exp is 1 then the output array will be [170, 90, 75, 45, 802, 24, 2, 66] because we are placing the elements in the output array based on the count array and the input array
#         index = (arr[i] // exp) % 10            # find the digit at the current exponent position example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] and exp is 1 then the index will be (170 // 1) % 10 = 0 for the first element, (45 // 1) % 10 = 5 for the second element and so on for the rest of the elements in the array
#         output[count[index] - 1] = arr[i]       # example if the digit is 3 then we will place the element at the index position of count[3] - 1 in the output array because we want to place the element at the correct position in the output array and this is done by using the count array to find the correct position of the element in the output array
#         count[index] -= 1                       # decrement the count of the digit in the count array example if the digit is 3 then count[3] will be decremented by 1 at the index place of 3 in the count array because we have placed one occurrence of 3 in the output array so we need to decrement the count of 3 in the count array to find the correct position of the next occurrence of 3 in the output array
#         i -= 1                                  # decrement the index of the input array to process the next element in the input array example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] and exp is 1 then we will process the elements in the input array from right to left because we are building the output array from right to left and this is done by decrementing the index of the input array
        
#     for i in range(n):                          # copy the output array to the input array so that the input array now contains the sorted numbers based on the current digit example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] and exp is 1 then after this loop the input array will be [170, 90, 75, 45, 802, 24, 2, 66] because we are copying the output array to the input array so that we can sort the input array based on the next digit in the next iteration of the radix sort algorithm
#         arr[i] = output[i]                      # example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] and exp is 1 then after this loop the input array will be [170, 90, 75, 45, 802, 24, 2, 66] because we are copying the output array to the input array so that we can sort the input array based on the next digit in the next iteration of the radix sort algorithm
        
# def radix_sort(arr):                            # main function to perform radix sort example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] then the output will be [2, 24, 45, 66, 75, 90, 170, 802] because we are sorting the input array based on each digit from least significant digit to most significant digit using the counting sort algorithm
#     max_element = max(arr)                      # find the maximum element in the input array to know the number of digits in the maximum element example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] then the max_element will be 802 because it is the largest number in the input array and it has 3 digits so we need to sort the input array based on each digit from least significant digit to most significant digit for 3 iterations of the counting sort algorithm
#     exp = 1                                     # initialize the exponent to 1 to start sorting based on the least significant digit example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] then we will start sorting based on the least significant digit which is the units place and this is done by initializing the exponent to 1 because we will be dividing the elements in the input array by 1 to find the digit at the units place in the counting sort algorithm
#     while max_element // exp > 0:               # loop until we have processed all the digits in the maximum element example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] then we will process the digits in the maximum element which is 802 from least significant digit to most significant digit and this is done by looping until max_element // exp > 0 because we will be dividing the maximum element by the exponent to find the digit at the current exponent position in the counting sort algorithm
        
#         counting_sort(arr, exp)                 # call the counting sort function to sort the input array based on the current digit example if the input array is [170, 45, 75, 90, 802, 24, 2, 66] and exp is 1 then we will sort the input array based on the least significant digit which is the units place and this is done by calling the counting sort function with the input array and the exponent as arguments
#         exp *= 10                               #
        
# arr = [170, 45, 75, 90, 802, 24, 2, 66]
# radix_sort(arr) 
# print("Sorted array is:", arr)

# selection sort
# def sort(arr):
#     n = len(arr)
    
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
        
# arr = [64, 25, 12, 22, 11]
# sort(arr)
# print("Sorted array is:", arr)


# # Bubble Sort
# count = 0
# def sort_1(arr):
#     global count
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 count += 1
#         if not count:
#             print(f"array is already sorted at pass {i + 1}")
#             break
                
# arr = [64, 34, 25, 12, 22, 11, 90]
# sort_1(arr)
# print("Sorted array is:", arr)
# print("Total swaps:", count)


# def sorting(arr):
#     n= len(arr)
#     for i in range(n):
#         insert_index = i
#         current_index = arr[i]
#         for j in range(i - 1, -1, -1):
#             if arr[j] > current_index:
#                 arr[j+1] = arr[j]
#                 insert_index = j
#             else:
                
#                 break
#         arr[insert_index] = current_index

                
# k = 0
# arr = [6, 4, 7, 3, 8, 2, 8, 1]
# sorting(arr)
# print("Sorted array is:", arr)
# print(f"the kth smallest number is: {arr[k]}")

# merge sort
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2
#     leftHalf = arr[:mid]
#     rightHalf = arr[mid:]
    
#     sortedleft = merge_sort(leftHalf)
#     sortedright = merge_sort(rightHalf)
    
#     return merge(sortedleft, sortedright)

# def merge(left, right):
#     result = []
#     i = j = 0
    
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
            
#     result.extend(left[i:])
#     result.extend(right[j:])
    
#     return result



# arr = [38, 27, 43, 3, 9, 82, 10]
# sorted_arr = merge_sort(arr)
# print("Sorted array is:", sorted_arr)


# from typing import List


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2
#     lefthalf = arr[:mid]
#     righthalf = arr[mid:]
    
#     sortedleft = merge_sort(lefthalf)
#     sortedright = merge_sort(righthalf)
    
#     return merge(sortedleft, sortedright)

# def merge(left, right):
#     result =[]
    
#     i = j = 0
    
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
            
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
            
#     result.extend(left[i:])
#     result.extend(right[j:])
    
#     return result

# arr = [38, 27, 43, 3, 9, 82, 10]
    
# sorted_arr = merge_sort(arr)
# print("Sorted array is:", sorted_arr)   

# #  merge two sorted arrays
# class solution:
#     def merge_sorted_arrays(self, nums1, m, nums2, n):
#         i = m -1
#         j = n- 1
#         k = m + n - 1
        
#         while i >= 0 and j >= 0:
#             if nums1[i] > nums2[j]:
#                 nums1[k] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[k] = nums2[j]
#                 j -= 1
                
#             k -= 1
#         while j >= 0:
#             nums1[k] = nums2[j]
#             j -= 1
#             k -= 1
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3   
# nums2 = [2, 5, 6]
# n = 3
# solution().merge_sorted_arrays(nums1, m, nums2, n)
# print("Merged array is:", nums1)

# merge k sorted lists
#  check if array is good or not

# class solution:
#     def isGood(self, nums: List[int]) -> bool:
#         nums.sort()
#         n = len(nums)
        
#         for i in range(n - 1):
#             if nums[i] != i + 1:
#                 return False
#         return nums[-1] == nums[n- 2]
    
# nums = [1,2,3,4]
# print("Is the array good?", solution().isGood(nums))

# # Arrays
# # 01 Find the largest sum contiguous subarray

# def longestsubarray(arr):
#     max_sum = arr[0]
#     current_sum = arr[0]
    
#     for i in range(1, len(arr)):
#         current_sum = max(arr[i], current_sum + arr[i])
#         max_sum = max(max_sum, current_sum)
        
#     return max_sum

# arr = [-2,1,-3,4,-1,2,1,-5,4]
# sum = longestsubarray(arr)
# print("largest subarray", sum)
    

# #  rotate an array keep k steps
# def rotate(arr, k):
#     n = len(arr)
#     for _ in range(k):
#         last = arr[-1]
        
#         for i in range(n-1, 0, -1):
#             arr[i] = arr[i -1]
            
#         arr[0] = last
        
#     return arr

# arr = [1,2,3,4,5,6,7,7,8]
# print(rotate(arr, 6))

# class solution:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# c = solution("krishna")
# print(c.data)

# 153.mimimum number in rotated sorted array
# class solution:
#     def findmin(self, nums):
#         nums.sort()
#         k = len(nums)
#         w = 2
#         for i in range(k - 1):
#             if nums[i] > nums[i + 1]:
#                 w = i + 1
#                 break
#         return nums[w]
# nums = [3,4,5,1,2]
# print("Minimum number in the rotated sorted array is:", solution().findmin(nums))   

# # selection sort algorithm finds the lowest value in the array and places it at the beginning of the array.

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr

# arr = [64, 25, 12, 22, 11]
# sorted_arr = selection_sort(arr)    
# print("Sorted array is:", sorted_arr)


# bobble sort algorithm repeatedly steps through the list, compares  the adjacent elements and swaps them if they in wrong order. until the list is sorted.
# class Solution:
#     def bobble_sort(self, arr):
#         n = len(arr)
#         for i in range(n):
#             for j in range(0, n -i -1):
#                 if arr[j] > arr[j+1]:
#                     arr[j], arr[j+1] = arr[j+1], arr[j]
#         return arr
# arr = [64, 34, 25, 12, 22, 11, 90]
# print("Sorted array is:", Solution().bobble_sort(arr))


# # INSERTION SORT
# class Solution:
#     def insertion_sort(self, arr):
#         n = len(arr)
#         for i in range(1, n):
#             insert_index = i
#             current_index = arr[i]
#             for j in range(i - 1, -1, -1):
#                 if arr[j] > arr[j+1]:
#                     arr[j+1] = arr[j]
#                     insert_index = j
#                 else:
#                     break
#             arr[insert_index] = current_index
#         return arr

# # Dynamic Programming  

# def min_coins(coins, amount):
#     """Minimum number of coins needed to make amount."""
#     dp = [float('inf')] * (amount + 1)
#     dp[0] = 0

#     for coin in coins:
#         for x in range(coin, amount + 1):
#             dp[x] = min(dp[x], dp[x - coin] + 1)

#     return dp[amount] if dp[amount] != float('inf') else -1


# def minimum_delete_sum(s1, s2):
#     """Minimum ASCII delete sum to make two strings equal."""
#     n, m = len(s1), len(s2)
#     dp = [[0] * (m + 1) for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

#     for j in range(1, m + 1):
#         dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if s1[i - 1] == s2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = min(
#                     dp[i - 1][j] + ord(s1[i - 1]),
#                     dp[i][j - 1] + ord(s2[j - 1])
#                 )

#     return dp[n][m]


# def length_of_lis(nums):
#     """Length of longest increasing subsequence."""
#     if not nums:
#         return 0

#     dp = [1] * len(nums)
#     for i in range(1, len(nums)):
#         for j in range(i):
#             if nums[j] < nums[i]:
#                 dp[i] = max(dp[i], dp[j] + 1)

#     return max(dp)


# print("min_coins([1, 2, 5], 11) =", min_coins([1, 2, 5], 11))
# print('minimum_delete_sum("sea", "eat") =', minimum_delete_sum("sea", "eat"))
# print("length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) =", length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))



# # Recursion is a programming technique where a function calls itself in order to solve a problem. It typically involves a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems. Recursion can simplify code and make it easier to read, but it can also lead to performance issues if not used carefully, such as stack overflow or excessive memory usage.
# # Add Two Numbers
# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next
        
#     def add_two_numbers(self, l1, l2):
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
# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))
# result = ListNode().add_two_numbers(l1, l2)
# print("Result of adding two numbers:", end=" ")
# while result:
#     print(result.val, end=" ")
#     result = result.next
        
# def fibnocci(n):
#     num = []
#     a, b  = 0, 1
#     while a <= n:
#         num.append(a)
#         a, b = b, a + b
#     return num

# print(fibnocci(8))


# VIP Customer Queue Problem

def solve(N: int, customers: list):
    vip = []
    regular = []
    
    for t, v in customers:
        if v == 1:
            vip.append(t)
        else:
            regular.append(t)
            # Shortest job First with each group
    vip.sort()
    regular.sort()
    
    total_wait = 0
    current_time = 0
    
    for t in vip:
        total_wait += current_time
        current_time += t
    for t in regular:
        total_wait += current_time
        current_time += t
    return total_wait

if __name__ == "main__":
    try:
        N = int(input())
        customers = []
        for _ in range(N):
            line = input().split()
            customers.append([int(x) for x in line[:2]])
        result = solve(N, customers)
        print(result)
    except (EOFError, ValueError):
        pass
        
        
# 
def solve(N: int, C1: int, C2: int, penalties: list):
    INF = float('inf')
    dp = [INF] * (N + 1)
    dp[0] = 0
    
    for i in range(N):
        if dp[i] == INF:
            continue
        base = dp[i] + penalties[i]
    
        if i + 1 <= N:
            dp[i + 1] = min(dp[i + 1], base + C1)
        if i + 2 <= N:
            dp[i + 2] = min(dp[i + 2], base + C2)
        if i + 3 <= N:
            dp[i + 3] = min(dp[i + 2], base + C3)
    return dp[N]

if __name__ == "__main__":
    try:
        N = int(input())
        C1, C2, C3 = map(int, input().split())
        penalties = list(map(int, input().split()))
        result = solve(N, C1, C2, C3, penalties)
        print(result)
    except (EOFError, ValueError):
        pass
        
        
