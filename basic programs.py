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

class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        ones = 0
        n = len(s)
        for i, c in enumerate(s):
            if c == '1':
                ones += 1
            else:  # c == '0'
                if i > 0 and s[i-1] == '1':
                    ans += ones
        return ans

# leetcode 11
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area 
    
    
# leetcode 12
class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num
    
# leetcode 13
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0

        for char in reversed(s):
            value = roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total
    
    
# 3234 leetcode
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):
            substring = s[i:i+3]
            if len(set(substring)) == 3:
                count += 1
        return count
    
    
# 1513 leetcode
class Solution:
    def numseb(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        cur = 0
        
        for ch in s:
            if ch == '1':
                cur += 1
            else:
                res += cur * (cur + 1) // 2
                cur = 0
        if cur: res += cur * (cur + 1) // 2
        return res
    