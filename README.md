
# Daily Coding Practice

Keep this repository as your daily practice hub. Use the sections below as a living guide for consistent, focused progress in Python and general programming skills.

## Quick Start

1. **Setup Python Environment**:
   ```powershell
   # Check Python version
   python --version
   
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   .\venv\Scripts\activate
   ```

2. **Run Python Programs**:
   ```powershell
   # Basic run
   python filename.py
   
   # Run with input
   python -i filename.py
   
   # Run with debugger
   python -m pdb filename.py
   ```

3. **VS Code Integration**:
   - `F5`: Run with debugging
   - `Ctrl + F5`: Run without debugging
   - `Ctrl + Shift + P`: Command palette for more options

## Goal

Build a short, repeatable daily practice habit that improves problem solving, fluency with Python, and small project delivery.

## Daily Routine (30–90 minutes)

- Warm-up (10–20 min): quick drills — review notes, flashcards, or 2-3 easy problems.
- Core practice (20–50 min): algorithmic problems, katas, or focused language features.
- Project / Application (10–30 min): incremental work on a small project or automation script.
- Review (5–10 min): write a 2–3 line daily log and note one learning or bug to revisit.

Adjust timeboxes to match your available window; consistency matters more than duration.

## Weekly Structure

- Monday: Fundamentals (data structures, complexity, Python idioms)
- Tuesday: Algorithms (search, sort, recursion, dynamic programming)
- Wednesday: Small Project / Automation
- Thursday: Libraries & Tools (pandas, requests, pytest, virtualenv)
- Friday: Code Review & Refactor (improve earlier work)
- Weekend: Challenge (Advent of Code / Project Euler / take-home practice)

## Exercise Types

- Katas / Algorithmic problems (LeetCode, Codewars)
- Mini-projects (CLI tools, scrapers, automation)
- Reading & rewriting (read a short tutorial and implement it)
- Tests & refactoring (write tests, improve design)

## Daily Log Template

Copy this template for each day in a `practice/` folder as `YYYY-MM-DD.md` or inside a notebook.

- Date: YYYY-MM-DD
- Time spent: 45 min
- Focus areas: e.g., recursion, list comprehensions
- Exercises completed: (list problems or filenames)
- Key takeaways: 1–2 bullets
- Follow-ups: items to revisit

Example entry

- Date: 2025-11-01
- Time spent: 40 min
- Focus areas: Binary tree traversal
- Exercises completed: LeetCode 94 (inorder), small script `tree_traversal.py`
- Key takeaways: Iterative stack approach is often simpler than recursion for large trees
- Follow-ups: Add unit tests, handle edge cases

## Progress Tracking

- Track streaks, total time, and problems solved per week.
- Keep one file per day in `practice/` and a short `progress.md` that lists weekly metrics.

## Tools & Files

- Use virtual environments (venv) for projects.
- Name practice files clearly: `practice/2025-11-01_my-kata.py` or `practice/2025-11-01.md` for notes.
- Keep runnable examples small and documented with a short header comment explaining purpose and usage.

## File Organization

```
python-problems/
│
├── practice/                    # Daily practice files
│   ├── YYYY-MM-DD_topic.py     # Python scripts
│   ├── YYYY-MM-DD_notes.md     # Study notes
│   └── progress.md             # Progress tracking
│
├── templates/                   # Template files
│   ├── daily_log.md           # Daily log template
│   └── script_header.py       # Script header template
│
├── solutions/                   # Completed solutions
│   ├── basic/                 # Basic problems
│   ├── intermediate/          # Intermediate problems
│   └── advanced/             # Advanced problems
│
└── README.md                   # This file
```

## Code Documentation Template

```python
"""
Problem: [Problem Name]
Difficulty: [Easy/Medium/Hard]
Category: [Arrays/Strings/etc.]

Description:
    Brief description of the problem

Example:
    Input: example_input
    Output: example_output
    Explanation: Why this output?

Solution Approach:
    1. Step one of the approach
    2. Step two of the approach
    
Time Complexity: O(?)
Space Complexity: O(?)

Author: [Your Name]
Date: YYYY-MM-DD
"""
```

## Resources

- Python docs: https://docs.python.org/3/
- LeetCode: https://leetcode.com/
- Project Euler: https://projecteuler.net/
- Real Python: https://realpython.com/
- "Automate the Boring Stuff with Python" by Al Sweigart

## Debugging Tips

1. **Print Debugging**:
   ```python
   print(f"Variable x = {x}")  # Format string
   print("Debug:", variable)   # Simple debug print
   ```

2. **Using VS Code Debugger**:
   - Set breakpoints by clicking left of line number
   - Use F5 to start debugging
   - Use Step Over (F10) and Step Into (F11)
   - Watch variables in debug window

3. **Python Debugger (pdb)**:
   ```python
   import pdb; pdb.set_trace()  # Add this line where you want to break
   # Commands: n (next), s (step), c (continue), p variable
   ```

## Common Python Commands

```powershell
# Environment Management
python -m venv venv              # Create virtual environment
.\venv\Scripts\activate          # Activate (Windows)
pip install package_name         # Install package
pip freeze > requirements.txt    # Save dependencies

# Running Programs
python script.py                 # Run script
python -i script.py             # Interactive mode
python -m pytest tests/         # Run tests
```

## Tips for Consistency

- Make the practice time a calendar event.
- Keep problems bite-sized; prefer short wins.
- Review mistakes and record the correct approach in your daily log.
- Pair practice with small, enjoyable projects to keep momentum.

## How to run example programs in this repo

This repository contains multiple example scripts and practice files. Use the instructions below to run them quickly.

### Quick Run Examples

**Run all 32 basic programs with test inputs (no interaction required)**:
```powershell
python "d:\Python\basic_programs_with_test_inputs.py"
```

**Run interactive version (provide inputs when prompted)**:
```powershell
python "d:\Python\basic programs.py"
```

**Run in VS Code**:
- Open the file and press `F5` (debug) or `Ctrl+F5` (run)

**Create a daily practice file from template**:
```powershell
mkdir -p practice
copy .\templates\daily_log.md practice\2025-11-23_notes.md
```

### Important Notes

- Use quotes around paths with spaces: `python "basic programs.py"`
- Activate virtual environment first: `.\venv\Scripts\activate`
- All programs include detailed comments explaining each concept

## Example Walkthrough

Here's a quick walkthrough of the basic programs included in this repo:

**Part A: Loop Statements** (Programs 1-15)
1. Sum of even numbers 2-100: Demonstrates range with step parameter
2. Numbers divisible by 7 but not 5: Multiple conditions with logical operators
3. Factorial: Accumulator pattern with loops
4. Fibonacci: Sequence generation with multiple assignment
5. Count digits: Integer division technique
6. Sum of digits: Digit extraction using modulo
7. Reverse number: Building numbers digit by digit
8. Prime numbers 2-100: Optimization with square root
9. Multiplication table: Nested loops
10. Count vowels/consonants: String iteration and conditions

**Part B: Conditional Statements** (Programs 16-32)
- Positive/negative/zero checks
- Even/odd detection
- Leap year validation
- Maximum of three numbers
- Character type classification
- Grade calculation
- Triangle validity
- Palindrome detection
- Electricity bill calculation
- And more...

Each program builds on fundamental Python concepts. Start with Part A to master loops, then move to Part B for conditional logic.

## Project Structure Guide

Organize your practice work as follows:

```
python-problems/
├── basic programs.py              # Original programs with input prompts
├── basic_programs_with_test_inputs.py  # Pre-filled test version
├── basic_programs_interactive.py  # Interactive demonstration
├── README.md                      # This file
└── practice/
    ├── 2025-11-02_basic_programs_notes.md  # Study notes
    ├── 2025-11-23_daily_log.md    # Daily practice log
    └── progress.md                # Weekly progress tracker
```

## QR Project - Quick Reference & Progress Tracking

A mini-project tracker to monitor your coding progress and maintain accountability.

### What is QR Project?

QR Project is a lightweight system for:
- Tracking daily coding sessions with timestamps
- Recording problem-solving insights and "aha moments"
- Building streaks and maintaining consistency
- Creating a personal reference guide of solutions

### QR Project Structure

```
qr_project/
├── daily/
│   ├── 2025-12-05.md          # Today's session
│   ├── 2025-12-04.md          # Yesterday's session
│   └── ...
├── insights.md                 # Key learnings and patterns
├── solutions_index.md          # Quick index of solved problems
└── streak.txt                  # Current streak counter
```

### Daily Session Template (for QR Project)

```markdown
# 2025-12-05 - Daily Coding Session

## Time: 45 minutes
## Focus: Loops and Conditionals

### Programs Completed
- [ ] Program 1: Sum of even numbers
- [ ] Program 3: Factorial
- [ ] Program 8: Prime numbers

### Problems Encountered
- Issue: Confusion with range() exclusive end
- Solution: Remember range(start, stop, step) where stop is exclusive

### Key Insights
- Modulo operator is powerful for divisibility checks
- Multiple conditions can be chained with 'and'/'or'

### Next Session Goals
- Master nested loops
- Practice pattern printing
- Implement all 15 Part A programs

### Difficulty Rating: 6/10
### Energy Level: 7/10
```

### Getting Started with QR Project

1. Create the directory structure:
```powershell
mkdir qr_project/daily
cd qr_project
```

2. Create your first daily session:
```powershell
# Windows PowerShell
$date = Get-Date -Format "yyyy-MM-dd"
New-Item -Path "daily/$date.md" -ItemType File -Force
```

3. Use the template above to log your session

4. Track your streak in `streak.txt`:
```
Current Streak: 5 days
Longest Streak: 12 days
Total Sessions: 47
```

### QR Project Benefits

✓ **Accountability** – Visible daily commitment  
✓ **Pattern Recognition** – Spot your learning patterns  
✓ **Reference** – Build your personal knowledge base  
✓ **Motivation** – Watch your streak grow  
✓ **Reflection** – Understand what works for you  

### Sample Insights File (`qr_project/insights.md`)

```markdown
# Programming Insights & Patterns

## Frequently Used Techniques
- **Accumulator Pattern**: Use for sum, product, count
- **Two-Pointer**: Useful for array/string problems
- **Digit Extraction**: Use modulo (%) and division (//)

## Common Mistakes to Avoid
- Forgetting range() is exclusive on the end
- Off-by-one errors in loops
- Confusing += with =

## Best Problem-Solving Approach
1. Understand the problem completely
2. Write pseudocode first
3. Implement step by step
4. Test with edge cases

## Breakthrough Moments
- Realized recursive solutions can be optimized with memoization (Day 12)
- Understood why square root optimization works for primes (Day 8)
```

## Troubleshooting

### "Python is not recognized"
- Ensure Python is installed and added to PATH
- Check: `python --version`
- Reinstall Python with "Add Python to PATH" option checked

### "List is not defined" or import errors
- File has missing imports at the top
- Required imports for this repo:
  ```python
  from typing import List
  from collections import defaultdict
  import heapq
  ```

### Program waits for input but nothing appears
- The script is waiting for your input
- Type a value and press Enter
- Example: for factorial, type `5` and press Enter

### Can't find file
- Use full paths: `python "d:\Python\basic programs.py"`
- Or navigate to folder first: `cd d:\Python` then `python "basic programs.py"`

### Virtual environment not activating
- Ensure you created it: `python -m venv venv`
- Windows activation: `.\venv\Scripts\activate` (not /bin)
- On success, prompt shows `(venv)` prefix

## License

This README is for personal use. Copy or adapt freely.




















































