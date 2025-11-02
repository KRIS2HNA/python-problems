# Python Basic Programs - Study Notes

## Date: 2025-11-02
## Focus Area: Basic Python Programming Concepts

### 1. Loop-Based Programs

#### Sum of Even Numbers (2-100)
```python
print(sum(range(2, 101, 2)))
```
- **Concept**: Range with step value
- **Key Points**:
  - `range(start, stop, step)`: Generates sequence from start to stop-1
  - `step=2`: Skips odd numbers
  - `sum()`: Built-in function to add all numbers in sequence

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
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```
- **Concept**: Optimized prime number testing
- **Key Points**:
  - Check only up to square root
  - Early return on finding factor
  - Special case for numbers < 2

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

### 7. Key Takeaways

- Mastering basic loops and conditions is fundamental
- Understanding number manipulation techniques is crucial
- Pattern programs help develop logical thinking
- Always consider edge cases and input validation
- Use appropriate data types and operators

### Follow-ups
- Add error handling to all programs
- Create unit tests for each function
- Implement alternative solutions for comparison
- Document time and space complexity