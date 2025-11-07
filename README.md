
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

## License

This README is for personal use. Copy or adapt freely.

