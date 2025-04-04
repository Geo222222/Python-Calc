# 🧮 PyQt6 Calculator – Responsive GUI with Copy/Paste and Testing

## 📋 Overview

A polished, keyboard-friendly, and responsive calculator built using **PyQt6**. Supports all basic arithmetic operations and is designed with usability in mind. This project features:

- A resizable and responsive GUI
- Keyboard and mouse support
- Clipboard integration for copy/paste
- Unit testing for core logic

---

## 🧰 Technologies Used

- Python 3.x
- PyQt6
- PyTest (for unit testing)

---

## 📁 Project Files

```
PyQt_Calculator/
├── calculator.py         # Main PyQt6 calculator interface
├── logic.py              # Calculation logic (isolated for testing)
├── test_logic.py         # PyTest unit tests for calculator operations
├── README.md             # Project documentation
```

---

## 💡 Features

- Responsive layout with grid-based buttons
- Keyboard support (arithmetic, backspace, enter, etc.)
- Clipboard integration: Ctrl+C (copy), Ctrl+V (paste)
- Error handling and result validation

---

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/Geo222222/PyQt_Calculator.git
cd PyQt_Calculator
```

2. Install dependencies:
```bash
pip install PyQt6 pytest
```

3. Run the application:
```bash
python calculator.py
```

---

## ✅ Running Unit Tests

```bash
pytest test_logic.py
```

Tests cover:
- Basic operations (`+`, `-`, `*`, `/`)
- Edge cases (divide by zero, invalid input)
- Result formatting

---

## 🧠 Keyboard Shortcuts

- `0-9`, `.`, `+`, `-`, `*`, `/` → Input
- `Enter / Return` → Evaluate expression
- `Esc` → Clear input
- `Backspace` → Delete last character
- `Ctrl+C` → Copy result
- `Ctrl+V` → Paste numeric value into input

---

## 📌 Future Improvements

- Add history panel for previous calculations
- Enable scientific functions (sqrt, log, sin, cos)
- Theming (dark/light mode toggle)
- Export results to CSV or text

---

**Author:** [Geo222222](https://github.com/Geo222222)  
**Focus:** GUI Engineering • Functional Programming • Automated Testing

