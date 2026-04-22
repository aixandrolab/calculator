# Copyright (c) 2023-2026, Alexander Suvorov. All rights reserved.
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QLabel,
    QDialog,
    QTextEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class HelpDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Help - Calculator")
        self.setFixedSize(500, 400)

        if parent and parent.windowIcon():
            self.setWindowIcon(parent.windowIcon())

        self.setStyleSheet("""
            QDialog {
                background-color: #2d2d2d;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
            }
            QTextEdit {
                background-color: #1a1a1a;
                color: #ffffff;
                border: 1px solid #ff9500;
                border-radius: 10px;
                font-size: 13px;
                padding: 10px;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("📱 Calculator - User Guide")
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #ff9500; margin-bottom: 10px;")
        layout.addWidget(title)

        content = QTextEdit()
        content.setReadOnly(True)
        content.setHtml("""
        <h2 style="color: #ff9500;">Basic Operations</h2>
        <p>• <b>Addition (+)</b> - Add two numbers<br>
        • <b>Subtraction (-)</b> - Subtract second number from first<br>
        • <b>Multiplication (*)</b> - Multiply two numbers<br>
        • <b>Division (/)</b> - Divide first number by second</p>

        <h2 style="color: #ff9500;">Special Functions</h2>
        <p>• <b>AC (All Clear)</b> - Reset everything to zero<br>
        • <b>+/−</b> - Change the sign of current number<br>
        • <b>%</b> - Calculate percentage of current number</p>

        <h2 style="color: #ff9500;">Tips</h2>
        <p>• Use <b>decimal point (.)</b> for floating point numbers<br>
        • Press <b>=</b> or <b>Enter</b> to get result<br>
        • Press <b>AC</b> or <b>Esc</b> to clear<br>
        • Keyboard shortcuts available - press <b>Ctrl+/</b></p>

        <h2 style="color: #ff9500;">Error Handling</h2>
        <p>• <b>Error</b> appears when dividing by zero<br>
        • Maximum <b>15 digits</b> before using scientific notation<br>
        • Use <b>AC</b> to recover from error state</p>
        """)
        layout.addWidget(content)

        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff9500;
                color: white;
                border: none;
                border-radius: 20px;
                padding: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ffaa33;
            }
            QPushButton:pressed {
                background-color: #cc7700;
            }
        """)
        close_btn.clicked.connect(self.accept)
        layout.addWidget(close_btn)

        self.setLayout(layout)
