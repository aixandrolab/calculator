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


class ShortcutsDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Keyboard Shortcuts")
        self.setFixedSize(550, 500)

        if parent and parent.windowIcon():
            self.setWindowIcon(parent.windowIcon())

        self.setStyleSheet("""
            QDialog {
                background-color: #2d2d2d;
            }
            QLabel {
                color: #ffffff;
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

        title = QLabel("⌨️ Keyboard Shortcuts")
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #ff9500; margin-bottom: 10px;")
        layout.addWidget(title)

        content = QTextEdit()
        content.setReadOnly(True)
        content.setHtml("""
        <style>
            .shortcut-table { width: 100%; }
            .shortcut-key { 
                color: #ff9500; 
                font-weight: bold;
                font-family: monospace;
                font-size: 14px;
            }
            .shortcut-desc { color: #ffffff; }
        </style>

        <h3 style="color: #ff9500;">📊 Basic Operations</h3>
        <table class="shortcut-table" cellpadding="8">
            <tr><td class="shortcut-key">0-9</td><td class="shortcut-desc">Numbers</td>\n
            <tr><td class="shortcut-key">. or ,</td><td class="shortcut-desc">Decimal point</td>\n
            <tr><td class="shortcut-key">+ - * /</td><td class="shortcut-desc">Operators</td>\n
            <tr><td class="shortcut-key">Enter or =</td><td class="shortcut-desc">Calculate result</td>\n
        </table>

        <h3 style="color: #ff9500; margin-top: 15px;">⚡ Special Functions</h3>
        <table class="shortcut-table" cellpadding="8">
            <tr><td class="shortcut-key">Esc or Delete</td><td class="shortcut-desc">Clear all (AC)</td>\n
            <tr><td class="shortcut-key">_ or ±</td><td class="shortcut-desc">Change sign (+/-)</td>\n
            <tr><td class="shortcut-key">%</td><td class="shortcut-desc">Percentage</td>\n
        </table>

        <h3 style="color: #ff9500; margin-top: 15px;">🎯 Menu Shortcuts</h3>
        <table class="shortcut-table" cellpadding="8">
            <tr><td class="shortcut-key">Ctrl+Q</td><td class="shortcut-desc">Exit application</td>\n
            <tr><td class="shortcut-key">F1</td><td class="shortcut-desc">Open Help</td>\n
            <tr><td class="shortcut-key">Ctrl+Alt+A</td><td class="shortcut-desc">Show About</td>\n
            <tr><td class="shortcut-key">Ctrl+/</td><td class="shortcut-desc">Show this help</td>\n
        </table>

        <h3 style="color: #ff9500; margin-top: 15px;">💡 Pro Tips</h3>
        <p>• Type directly without clicking buttons<br>
        • Use keyboard for faster calculations<br>
        • Press Enter multiple times to repeat operations<br>
        • Calculator supports up to 15 digits before scientific notation</p>
        """)
        layout.addWidget(content)

        close_btn = QPushButton("Got it!")
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
