# Copyright (c) 2023-2026, Alexander Suvorov. All rights reserved.
import os
import sys

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QLabel,
    QFrame,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QAction, QIcon

from core.dialogs.about_dialog import AboutDialog
from core.dialogs.help_dialog import HelpDialog
from core.dialogs.shortcuts_dialog import ShortcutsDialog
from core.models.buttons import FunctionButton, OperatorButton, NumberButton, EqualsButton
from core import __version__ as ver

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"Calculator v{ver}")
        self.setFixedSize(400, 650)

        self.setup_application_icon()

        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a1a;
            }
            QMenuBar {
                background-color: #2d2d2d;
                color: #ffffff;
                border-bottom: 1px solid #3d3d3d;
            }
            QMenuBar::item {
                background-color: transparent;
                padding: 4px 8px;
            }
            QMenuBar::item:selected {
                background-color: #ff9500;
            }
            QMenu {
                background-color: #2d2d2d;
                color: #ffffff;
                border: 1px solid #3d3d3d;
            }
            QMenu::item {
                padding: 6px 24px;
            }
            QMenu::item:selected {
                background-color: #ff9500;
            }
        """)

        self.reset_state()

        self.setup_menu_bar()
        self.setup_ui()

    def setup_application_icon(self):
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "icons", "icon.png")

        if not os.path.exists(icon_path):
            icon_path = os.path.join(os.path.dirname(__file__), "icon.png")

        if os.path.exists(icon_path):
            icon = QIcon(icon_path)
            self.setWindowIcon(icon)

    def create_desktop_entry(self):
        from core.dialogs.desktop_entry_dialog import DesktopEntryDialog

        dialog = DesktopEntryDialog(self)
        dialog.exec()

    def setup_menu_bar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")

        if sys.platform.startswith('linux'):
            desktop_entry_action = QAction('Create Desktop Entry...', self)
            desktop_entry_action.triggered.connect(self.create_desktop_entry)
            file_menu.addAction(desktop_entry_action)
            file_menu.addSeparator()

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        help_menu = menubar.addMenu("Help")

        help_action = QAction("Help", self)
        help_action.setShortcut("F1")
        help_action.triggered.connect(self.show_help)
        help_menu.addAction(help_action)

        about_action = QAction("About", self)
        about_action.setShortcut("Ctrl+Alt+A")
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

        help_menu.addSeparator()

        shortcuts_action = QAction("Shortcuts Help", self)
        shortcuts_action.setShortcut("Ctrl+/")
        shortcuts_action.triggered.connect(self.show_shortcuts)
        help_menu.addAction(shortcuts_action)

    def show_help(self):
        dialog = HelpDialog(self)
        dialog.exec()

    def show_about(self):
        dialog = AboutDialog(self)
        dialog.exec()

    def show_shortcuts(self):
        dialog = ShortcutsDialog(self)
        dialog.exec()

    def reset_state(self):
        self.current_number = "0"
        self.previous_number = None
        self.operator = None
        self.waiting_for_operand = True
        self.error_state = False

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(20, 20, 20, 20)
        central_widget.setLayout(main_layout)

        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont("Segoe UI", 48, QFont.Weight.Light))
        self.display.setStyleSheet("""
            QLabel {
                color: #ffffff;
                background-color: #1a1a1a;
                padding: 20px;
                border: none;
                min-height: 100px;
            }
        """)
        main_layout.addWidget(self.display)

        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet("background-color: #333333; max-height: 1px;")
        main_layout.addWidget(line)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)
        main_layout.addLayout(grid_layout)

        ac_btn = FunctionButton("AC")
        ac_btn.clicked.connect(self.make_handler("AC"))
        grid_layout.addWidget(ac_btn, 0, 0)

        sign_btn = FunctionButton("+/-")
        sign_btn.clicked.connect(self.make_handler("+/-"))
        grid_layout.addWidget(sign_btn, 0, 1)

        percent_btn = FunctionButton("%")
        percent_btn.clicked.connect(self.make_handler("%"))
        grid_layout.addWidget(percent_btn, 0, 2)

        divide_btn = OperatorButton("/")
        divide_btn.clicked.connect(self.make_handler("/"))
        grid_layout.addWidget(divide_btn, 0, 3)

        for i, num in enumerate(["7", "8", "9"]):
            btn = NumberButton(num)
            btn.clicked.connect(self.make_handler(num))
            grid_layout.addWidget(btn, 1, i)

        multiply_btn = OperatorButton("*")
        multiply_btn.clicked.connect(self.make_handler("*"))
        grid_layout.addWidget(multiply_btn, 1, 3)

        for i, num in enumerate(["4", "5", "6"]):
            btn = NumberButton(num)
            btn.clicked.connect(self.make_handler(num))
            grid_layout.addWidget(btn, 2, i)

        minus_btn = OperatorButton("-")
        minus_btn.clicked.connect(self.make_handler("-"))
        grid_layout.addWidget(minus_btn, 2, 3)

        for i, num in enumerate(["1", "2", "3"]):
            btn = NumberButton(num)
            btn.clicked.connect(self.make_handler(num))
            grid_layout.addWidget(btn, 3, i)

        plus_btn = OperatorButton("+")
        plus_btn.clicked.connect(self.make_handler("+"))
        grid_layout.addWidget(plus_btn, 3, 3)

        zero_btn = NumberButton("0")
        zero_btn.setFixedSize(170, 80)
        zero_btn.clicked.connect(self.make_handler("0"))
        grid_layout.addWidget(zero_btn, 4, 0, 1, 2)

        dot_btn = NumberButton(".")
        dot_btn.clicked.connect(self.make_handler("."))
        grid_layout.addWidget(dot_btn, 4, 2)

        equals_btn = EqualsButton()
        equals_btn.clicked.connect(self.make_handler("="))
        grid_layout.addWidget(equals_btn, 4, 3)

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def keyPressEvent(self, event):
        key = event.text()
        key_code = event.key()

        if key_code == Qt.Key.Key_Backspace:
            self.handle_backspace()
            self.update_display()
            event.accept()
            return

        if key_code == Qt.Key.Key_Escape:
            self.handle_button("AC")
            self.update_display()
            event.accept()
            return

        if key_code == Qt.Key.Key_Return or key_code == Qt.Key.Key_Enter:
            self.handle_button("=")
            self.update_display()
            event.accept()
            return

        if key.isdigit():
            self.handle_button(key)
        elif key in ['.', ',']:
            self.handle_button('.')
        elif key in ['+', '-', '*', '/']:
            self.handle_button(key)
        elif key in ['=', '\r']:
            self.handle_button('=')
        elif key in ['\x1b', '\x7f']:
            self.handle_button('AC')
        elif key in ['_', '±']:
            self.handle_button('+/-')
        elif key == '%':
            self.handle_button('%')

        self.update_display()

    def make_handler(self, text):

        def handler():
            self.handle_button(text)

        return handler

    def handle_button(self, value):
        if self.error_state and value != "AC":
            return

        if value.isdigit() or value == ".":
            self.handle_number(value)
        elif value in ("+", "-", "*", "/"):
            self.handle_operator(value)
        elif value == "=":
            self.handle_equals()
        elif value == "AC":
            self.handle_clear()
        elif value == "+/-":
            self.handle_negate()
        elif value == "%":
            self.handle_percent()

        self.update_display()

    def handle_backspace(self):
        if self.waiting_for_operand:
            return

        if len(self.current_number) > 1:
            self.current_number = self.current_number[:-1]
        else:
            self.current_number = "0"
            self.waiting_for_operand = True

    def handle_number(self, number):
        if self.waiting_for_operand:
            if number == ".":
                self.current_number = "0."
            else:
                self.current_number = number
            self.waiting_for_operand = False
        else:
            if self.current_number == "0" and number != ".":
                self.current_number = number
                return

            if number == "." and "." in self.current_number:
                return

            self.current_number += number

        if len(self.current_number) > 15:
            self.current_number = self.current_number[:15]

    def handle_operator(self, operator):
        if self.previous_number is not None and not self.waiting_for_operand:
            self.calculate_result()

        self.previous_number = float(self.current_number)
        self.operator = operator
        self.waiting_for_operand = True

    def handle_equals(self):
        if self.previous_number is not None and self.operator and not self.waiting_for_operand:
            self.calculate_result()
            self.previous_number = None
            self.operator = None
            self.waiting_for_operand = True

    def handle_clear(self):
        self.reset_state()
        self.error_state = False

    def handle_negate(self):
        try:
            value = float(self.current_number)
            value = -value
            self.current_number = self.format_number(value)
            self.waiting_for_operand = False
        except:
            pass

    def handle_percent(self):
        try:
            value = float(self.current_number) / 100
            self.current_number = self.format_number(value)
            self.waiting_for_operand = False
        except:
            pass

    def calculate_result(self):
        try:
            current = float(self.current_number)
            previous = float(self.previous_number)

            if self.operator == "+":
                result = previous + current
            elif self.operator == "-":
                result = previous - current
            elif self.operator == "*":
                result = previous * current
            elif self.operator == "/":
                if current == 0:
                    self.error_state = True
                    self.current_number = "Error"
                    return
                result = previous / current
            else:
                return

            self.current_number = self.format_number(result)
            self.waiting_for_operand = True

        except Exception as e:
            self.error_state = True
            self.current_number = "Error"

    def format_number(self, num):
        if num == int(num):
            return str(int(num))

        formatted = f"{num:.10f}".rstrip('0').rstrip('.')
        return formatted

    def update_display(self):
        if self.error_state:
            self.display.setText(self.current_number)
            return

        if len(self.current_number) > 15:
            try:
                value = float(self.current_number)
                self.display.setText(f"{value:.10e}")
            except:
                self.display.setText(self.current_number[:15] + "...")
        else:
            self.display.setText(self.current_number)
