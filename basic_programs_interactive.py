# Modified version with preset test values
print("Part A: Loop Statements\n")

# 1
print("1. Sum of even numbers from 2 to 100:")
print(sum(range(2, 101, 2)))
print()

# 2
print("2. Numbers between 100-200 divisible by 7 but not by 5:")
for i in range(100, 201):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
print()

# 3
print("3. Factorial calculation:")
num = 5  # Test value
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")
print()

# 4
print("4. Fibonacci sequence:")
n = 8  # Test value
print(f"First {n} terms of Fibonacci sequence:")
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("\n")

# 5
print("5. Count digits:")
num = 12345  # Test value
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

print("Program completed with test values:")