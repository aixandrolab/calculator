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
        self.setFixedSize(550, 500)

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

        title = QLabel("📱 Modern Calculator - User Guide")
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #ff9500; margin-bottom: 10px;")
        layout.addWidget(title)

        content = QTextEdit()
        content.setReadOnly(True)
        content.setHtml("""
        <style>
            h2 { 
                color: #ff9500; 
                margin-top: 15px; 
                margin-bottom: 10px;
                font-size: 16px;
            }
            p { 
                margin: 5px 0; 
                line-height: 1.4;
            }
            .note {
                background-color: #1a1a1a;
                border-left: 3px solid #ff9500;
                padding: 8px;
                margin: 10px 0;
                border-radius: 5px;
            }
            .tip {
                color: #ffaa33;
            }
        </style>

        <h2>📊 Basic Operations</h2>
        <p>• <b>Addition (+)</b> - Add two numbers<br>
        • <b>Subtraction (-)</b> - Subtract second number from first<br>
        • <b>Multiplication (*)</b> - Multiply two numbers<br>
        • <b>Division (/)</b> - Divide first number by second</p>

        <h2>⚡ Special Functions</h2>
        <p>• <b>AC (All Clear)</b> - Reset everything to zero<br>
        • <b>+/−</b> - Change the sign of current number<br>
        • <b>%</b> - Calculate percentage of current number</p>

        <h2>💡 Tips</h2>
        <p>• Use <b>decimal point (.)</b> for floating point numbers<br>
        • Press <b>=</b> or <b>Enter</b> to get result<br>
        • Press <b>Backspace</b> to clear single number<br>
        • Press <b>AC</b> or <b>Esc</b> to clear<br>
        • Keyboard shortcuts available - press <b>Ctrl+/</b></p>

        <h2>🖥️ Desktop Integration (Linux Only)</h2>
        <p><b>File → Create Desktop Entry</b> — Create application shortcut in your system menu</p>

        <div class="note">
        <b>📌 Features:</b><br>
        • Choose between <b>Application Menu</b> (~/.local/share/applications/)<br>
        • and/or <b>Desktop</b> (~/Desktop/)<br>
        • Automatic icon integration<br>
        • Support for virtual environments
        </div>

        <div class="note">
        <b>⚠️ Important Notes:</b><br>
        • After creation, you may need to <b>log out and back in</b> for the entry to appear in the menu<br>
        • Desktop shortcuts may show <b>"Unsecured Application Launcher"</b><br>
        • <b>Right-click</b> → <b>"Allow Launching"</b> (one-time only)<br>
        • The shortcut will work immediately after allowing
        </div>

        <h2>❌ Error Handling</h2>
        <p>• <b>Error</b> appears when dividing by zero<br>
        • Maximum <b>15 digits</b> before using scientific notation<br>
        • Use <b>AC</b> to recover from error state</p>

        <h2>🎯 Keyboard Shortcuts</h2>
        <p>• Press <b>F1</b> - Open this help<br>
        • Press <b>Ctrl+/</b> - Show all keyboard shortcuts<br>
        • Press <b>Ctrl+Alt+A</b> - Show about dialog<br>
        • Press <b>Ctrl+Q</b> - Exit application</p>
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
