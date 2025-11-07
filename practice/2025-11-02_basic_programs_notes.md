# Python Basic Programs - Study Notes

## Date: 2025-11-02
## Focus Area: Basic Python Programming Concepts
## Time Spent: 120 minutes
## Topics Covered: Loops, Number Operations, Pattern Printing

### Quick Reference

#### Python Operators Used
- `+`, `-`, `*`, `/`: Basic arithmetic
- `//`: Integer division (floor division)
- `%`: Modulo (remainder)
- `**`: Power/Exponentiation
- `==`, `!=`, `>`, `<`, `>=`, `<=`: Comparison
- `and`, `or`, `not`: Logical operators

#### Common Built-in Functions
```python
print()    # Output to console
input()    # Get user input
int()      # Convert to integer
str()      # Convert to string
range()    # Generate number sequence
sum()      # Sum of iterable
abs()      # Absolute value
len()      # Length of sequence
```

### 1. Loop-Based Programs

#### Sum of Even Numbers (2-100)
```python
# Method 1: Using range with step
result = sum(range(2, 101, 2))
print(result)  # Output: 2550

# Method 2: Using filter
result = sum(num for num in range(2, 101) if num % 2 == 0)
print(result)  # Output: 2550

# Method 3: Traditional for loop
total = 0
for num in range(2, 101):
    if num % 2 == 0:
        total += num
print(total)  # Output: 2550
```
- **Concept**: Range with step value
- **Key Points**:
  - `range(start, stop, step)`: Generates sequence from start to stop-1
  - `step=2`: Skips odd numbers
  - `sum()`: Built-in function to add all numbers in sequence
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Common Pitfalls**:
  - Forgetting range's end is exclusive
  - Not considering edge cases (start/end values)
- **Variations**:
  - Sum of odd numbers
  - Sum in custom range
  - Product instead of sum

#### Numbers Divisible by 7 but not by 5
```python
for i in range(100, 201):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
```
- **Concept**: Multiple conditions with logical operators
- **Key Points**:
  - `%`: Modulo operator for remainder
  - `and`: Logical operator requiring both conditions true
  - `!=`: Not equal operator

#### Factorial Calculation
```python
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
```
- **Concept**: Accumulator pattern
- **Key Points**:
  - Initialize accumulator (fact = 1)
  - Multiply in each iteration
  - Range includes num (num + 1)

#### Fibonacci Sequence
```python
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```
- **Concept**: Multiple assignment and sequence generation
- **Key Points**:
  - Parallel assignment: `a, b = b, a + b`
  - Uses previous two numbers
  - `end=" "`: Custom print separator

### 2. Number Manipulation Programs

#### Count Digits
```python
num = 12345
count = 0
while num > 0:
    num //= 10
    count += 1
```
- **Concept**: Integer division and counting
- **Key Points**:
  - `//`: Integer division operator
  - While loop with counter
  - Number reduces by factor of 10 each iteration

#### Sum of Digits
```python
num = 12345
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
```
- **Concept**: Digit extraction using modulo
- **Key Points**:
  - `% 10`: Gets rightmost digit
  - `//= 10`: Removes rightmost digit
  - Accumulates sum in loop

#### Number Reversal
```python
num = 12345
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
```
- **Concept**: Building numbers digit by digit
- **Key Points**:
  - Multiply by 10 to shift digits left
  - Add new digit in ones place
  - Original number reduces each iteration

### 3. Pattern Programs

#### Star Pattern
```python
for i in range(1, 6):
    print('*' * i)
```
- **Concept**: String repetition
- **Key Points**:
  - String multiplication with `*`
  - Increasing pattern with loop counter
  - Implicit newline with print

#### Number Pattern
```python
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
```
- **Concept**: Nested loops for 2D patterns
- **Key Points**:
  - Outer loop for rows
  - Inner loop depends on outer loop value
  - Empty print() for newline

### 4. Common Algorithms

#### Prime Number Check
```python
def is_prime(num):
    """
    Check if a number is prime.
    
    Args:
        num (int): Number to check
    Returns:
        bool: True if prime, False otherwise
    """
    # Handle special cases
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # Check odd numbers up to square root
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Example usage:
test_numbers = [2, 3, 4, 17, 25, 97]
for n in test_numbers:
    print(f"{n} is {'prime' if is_prime(n) else 'not prime'}")

# Optimized version for finding multiple primes
def sieve_of_eratosthenes(n):
    """
    Find all prime numbers up to n using Sieve of Eratosthenes.
    
    Args:
        n (int): Upper limit
    Returns:
        list: List of prime numbers
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
                
    return [i for i in range(n + 1) if sieve[i]]

# Example:
primes = sieve_of_eratosthenes(100)
print(f"Primes up to 100: {primes}")
```
- **Concept**: Optimized prime number testing
- **Key Points**:
  - Check only up to square root
  - Early return on finding factor
  - Special case for numbers < 2
  - Optimization for even numbers
  - Sieve method for multiple primes
- **Time Complexity**: 
  - Single prime check: O(√n)
  - Sieve method: O(n log log n)
- **Space Complexity**:
  - Single prime check: O(1)
  - Sieve method: O(n)
- **Applications**:
  - Cryptography
  - Number theory
  - Problem solving

### 5. Study Tips

1. **Understanding Patterns**:
   - Look for accumulator patterns (sum, product)
   - Recognize counter patterns (counting, tracking)
   - Identify digit manipulation patterns

2. **Code Organization**:
   - Use clear variable names
   - Add comments for complex logic
   - Break down complex problems into steps

3. **Common Techniques**:
   - Initialize variables before loops
   - Use appropriate loop type (for vs while)
   - Consider edge cases (zero, negative numbers)

4. **Testing Strategy**:
   - Test with simple inputs first
   - Include edge cases
   - Verify output manually for small inputs

### 6. Practice Exercises

1. Modify the factorial program to handle negative numbers
2. Create a reverse number pattern
3. Implement sum of digits for negative numbers
4. Add input validation to all programs
5. Optimize the prime number checker

### 7. Advanced Concepts and Best Practices

#### Error Handling
```python
def safe_input_number():
    """Get numeric input with error handling."""
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\nOperation cancelled")
            return None

def calculate_factorial(n):
    """Calculate factorial with validation."""
    try:
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < 0:
            raise ValueError("Input must be non-negative")
        
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None
```

#### Unit Testing
```python
import unittest

class TestMathFunctions(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(0), 1)
        self.assertIsNone(calculate_factorial(-1))
        
    def test_is_prime(self):
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(-1))

if __name__ == '__main__':
    unittest.main()
```

#### Performance Optimization
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    """Optimized Fibonacci with memoization."""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### 8. Key Takeaways

1. **Code Organization**:
   - Use functions for reusability
   - Add docstrings for documentation
   - Follow PEP 8 style guidelines

2. **Error Handling**:
   - Validate inputs
   - Use try-except blocks
   - Provide meaningful error messages

3. **Testing**:
   - Write unit tests
   - Test edge cases
   - Use assertions for validation

4. **Optimization**:
   - Consider time/space complexity
   - Use appropriate algorithms
   - Cache results when beneficial

### 9. Follow-up Tasks

1. **Coding Practice**:
   - Implement all programs with error handling
   - Write unit tests for each function
   - Create alternative solutions
   - Add timing measurements

2. **Documentation**:
   - Add detailed comments
   - Write function docstrings
   - Document time/space complexity

3. **Advanced Features**:
   - Try list comprehensions
   - Use generator expressions
   - Implement with recursion

4. **Project Ideas**:
   - Calculator application
   - Number theory toolkit
   - Pattern generator
   - Math quiz game