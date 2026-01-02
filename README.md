# Daily Coding Practice 🧠

Build a short, repeatable daily habit to improve Python fluency and problem solving.

## Table of Contents
- [About](#about)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## About
A small, personal repository for daily practice: algorithm katas, mini-projects, and short notes. Keep small, runnable examples with clear headers and daily logs in `practice/`.

## Quick Start 🔧

### Prerequisites
- Python 3.8+ installed
- (Optional) Create and activate a virtual environment

Windows PowerShell:
```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate
```

Cross-platform note: On macOS/Linux use `source .venv/bin/activate`.

### Install dependencies (if any)
```powershell
pip install -r requirements.txt
```

## Usage Examples ▶️

Run a single script:
```powershell
python "basic programs.py"
```

Run the pre-filled test program (no interaction):
```powershell
python "basic_programs_with_test_inputs.py"
```

Debug in VS Code:
- F5 to debug, Ctrl+F5 to run without debugging.

Tip: Use quotes around paths containing spaces.

## Project Structure 📁
```
.
├── basic programs.py
├── basic_programs_with_test_inputs.py
├── basic_programs_interactive.py
├── README.md
└── practice/
    ├── YYYY-MM-DD_notes.md
    └── progress.md
```

## Contributing ✨
- Keep daily files small and named `YYYY-MM-DD_topic.md` or `.py`.
- Add a short header comment to scripts (name, date, problem, complexity).
- Open a PR for larger changes or restructuring.

## License
Add your preferred license here (e.g., MIT). I can add an `LICENSE` file if you'd like.

---

*Shortened and reorganized for clarity — original content kept in history.*

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




















































