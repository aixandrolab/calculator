# 🧮 Modern Calculator

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/aixandrolab/calculator)](https://github.com/aixandrolab/calculator/)
![GitHub top language](https://img.shields.io/github/languages/top/aixandrolab/calculator)
[![GitHub](https://img.shields.io/github/license/aixandrolab/calculator)](https://github.com/aixandrolab/calculator/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/aixandrolab/calculator?style=social)](https://github.com/aixandrolab/calculator/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/aixandrolab/calculator?style=social)](https://github.com/aixandrolab/calculator/network/members)

A beautiful and functional calculator built with PyQt6, featuring a modern dark theme, keyboard shortcuts, and scientific notation support.

---

## ⚠️ Disclaimer

**By using this software, you agree to the full disclaimer terms.**

**Summary:** Software provided "AS IS" without warranty. You assume all risks.

**Full legal disclaimer:** See [DISCLAIMER.md](https://github.com/aixandrolab/calculator/blob/master/DISCLAIMER.md)

---

![Calculator Screenshot](https://github.com/aixandrolab/calculator/blob/master/data/images/logo.png)

---

## ✨ Features

- **Modern Dark Theme** - Eye-friendly dark interface with orange accents
- **Keyboard Support** - Full keyboard control for faster calculations
- **Scientific Notation** - Automatically switches to scientific notation for large numbers
- **Error Handling** - Proper error handling for division by zero and invalid operations
- **Responsive Design** - Clean and intuitive button layout

---

## 🎯 Keyboard Shortcuts

| Key               | Action              |
|-------------------|---------------------|
| `0-9`             | Numbers             |
| `.` or `,`        | Decimal point       |
| `+ - * /`         | Operations          |
| `Enter` or `=`    | Calculate result    |
| `Esc` or `Delete` | Clear all (AC)      |
| `_` or `±`        | Change sign (+/-)   |
| `%`               | Percentage          |
| `Ctrl+Q`          | Exit application    |
| `F1`              | Open Help           |
| `Ctrl+Alt+A`      | Show About          |
| `Ctrl+/`          | Show shortcuts help |

---

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Step 1: Clone the repository

```bash
git clone https://github.com/aixandrolab/calculator.git
cd calculator
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the application

```bash
python app.py
```

---

## 📁 Project Structure

```
calculator/
├── app.py                 # Main application entry point
├── core/
│   ├── __init__.py
│   ├── main_window.py    # Main calculator window
│   ├── dialogs/
│   │   ├── __init__.py
│   │   ├── about_dialog.py
│   │   ├── help_dialog.py
│   │   └── shortcuts_dialog.py
│   └── models/
│       ├── __init__.py
│       └── buttons.py     # Button classes
├── data/
│   ├── icons/
│   │   └── icon.png       # Application icon
│   └── images/
│       └── screenshot.png # Screenshot for README
├── LICENSE
├── requirements.txt
└── README.md
```

---

## 🎮 How to Use

1. **Basic Calculations**
   - Click the number buttons or use your keyboard to enter numbers
   - Select an operation (+, -, *, /)
   - Press `=` or `Enter` to see the result

2. **Special Functions**
   - `AC` - Clears everything and resets to zero
   - `+/-` - Changes the sign of the current number
   - `%` - Calculates the percentage of the current number

3. **Decimal Numbers**
   - Use the `.` button or press `.` on your keyboard
   - The calculator prevents multiple decimal points

4. **Error Recovery**
   - If you see "Error" (usually from division by zero), press `AC` to continue

---

## 🛠️ Development

### Building from source

1. Ensure you have Python 3.9+ installed
2. Clone the repository
3. Install dependencies: `pip install -r requirements.txt`
4. Run `python app.py`

### Adding Custom Icon

Place your `icon.png` file in:
- `data/icons/icon.png` (recommended)

The application will automatically use it for the window and dialogs.

---

## 📝 License

This project is licensed under the BSD-3 Clause License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Alexander Suvorov**
- GitHub: [@aixandrolab](https://github.com/aixandrolab)
- Website: [https://aixandrolab.ru](https://aixandrolab.ru)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/aixandrolab/calculator/issues).

---

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

## 📧 Contact

For questions or suggestions, please open an [issue](https://github.com/aixandrolab/calculator/issues/) on GitHub.

---

Made with ❤️. Made for users.