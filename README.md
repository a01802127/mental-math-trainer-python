# Mental Math Trainer

Mental Math Trainer is a Python-based application designed to improve arithmetic speed and accuracy through timed practice sessions. It generates random math problems, evaluates user input, tracks performance, and stores scores locally for progress monitoring.

---

## Features

- Randomly generated arithmetic problems:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Real-time answer validation
- Score tracking system
- Persistent score storage using a local text file
- Error handling for invalid input
- Lightweight and runs entirely in the terminal

---

## How It Works

The program generates a series of math problems and prompts the user to solve them. After each answer, it checks correctness and keeps track of the score. At the end of the session, the score is saved locally for future reference.

Scores are stored in:

```
scores.txt
```

---

## Requirements

- Python 3.x

No external libraries are required.

---

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/mental-math-trainer.git
```

2. Navigate to the project folder:

```
cd mental-math-trainer
```

3. Run the program:

```
python mental_math_trainer.py
```

---

## Example Session

```
Solve: 7 + 5 = 12
Correct!

Solve: 9 × 6 = 54
Correct!

Solve: 15 − 8 = 10
Incorrect. The correct answer is 7.

Final Score: 2/3
Score saved successfully.
```

---

## File Structure

```
mental-math-trainer/
│
├── mental_math_trainer.py   # Main program
├── scores.txt               # Score storage file (created automatically)
└── README.md                # Project documentation
```

---

## Error Handling

The program safely handles:

- Empty input
- Non-numeric input
- Invalid values
- Missing score file (automatically created)

---

## Educational Purpose

This project demonstrates practical use of:

- Python input/output
- Exception handling
- File handling
- Random number generation
- Conditional logic
- Loop control

---

## Future Improvements

Possible enhancements include:

- Difficulty levels
- Timer-based challenges
- Graphical interface (GUI)
- Performance statistics
- Leaderboard system

---

## Author

Developed as a practical Python project focused on applied programming and algorithmic logic.
