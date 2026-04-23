# Copyright (c) 2023-2026, Alexander Suvorov. All rights reserved.
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFrame,
    QDialog,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class AboutDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Calculator")
        self.setFixedSize(500, 600)

        if parent and parent.windowIcon():
            self.setWindowIcon(parent.windowIcon())

        self.setStyleSheet("""
            QDialog {
                background-color: #2d2d2d;
            }
            QLabel {
                color: #ffffff;
            }
        """)

        layout = QVBoxLayout()

        if parent and parent.windowIcon():
            icon_label = QLabel()
            icon_label.setPixmap(parent.windowIcon().pixmap(64, 64))
            icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(icon_label)

        title = QLabel("Calculator")
        title.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #ff9500;")
        layout.addWidget(title)

        version = QLabel("Version 1.0.1")
        version.setFont(QFont("Segoe UI", 12))
        version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        version.setStyleSheet("color: #a6a6a6;")
        layout.addWidget(version)

        desc = QLabel(
            "A beautiful and functional calculator\n"
            "built with PyQt6\n\n"
            "Features:\n"
            "• Linux desktop entry creation\n"
            "• Modern dark theme\n"
            "• Keyboard shortcuts\n"
            "• Scientific notation\n"
            "• Error handling"
        )
        desc.setFont(QFont("Segoe UI", 11))
        desc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        desc.setStyleSheet("color: #ffffff; line-height: 1.5;")
        layout.addWidget(desc)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet("background-color: #444444; max-height: 1px; margin: 10px 0;")
        layout.addWidget(separator)

        links_label = QLabel("Connect with us:")
        links_label.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        links_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        links_label.setStyleSheet("color: #ff9500; margin-top: 5px;")
        layout.addWidget(links_label)

        github_btn = QPushButton("🔗 GitHub Repository")
        github_btn.setFont(QFont("Segoe UI", 10))
        github_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        github_btn.setStyleSheet("""
            QPushButton {
                background-color: #333333;
                color: #ff9500;
                border: 1px solid #ff9500;
                border-radius: 20px;
                padding: 8px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff9500;
                color: #ffffff;
                border-color: #ff9500;
            }
            QPushButton:pressed {
                background-color: #cc7700;
            }
        """)
        github_btn.clicked.connect(self.open_github)
        layout.addWidget(github_btn)

        profile_btn = QPushButton("👤 Developer Profile")
        profile_btn.setFont(QFont("Segoe UI", 10))
        profile_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        profile_btn.setStyleSheet("""
            QPushButton {
                background-color: #333333;
                color: #ff9500;
                border: 1px solid #ff9500;
                border-radius: 20px;
                padding: 8px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff9500;
                color: #ffffff;
                border-color: #ff9500;
            }
            QPushButton:pressed {
                background-color: #cc7700;
            }
        """)
        profile_btn.clicked.connect(self.open_profile)
        layout.addWidget(profile_btn)

        social_label = QLabel("Social:")
        social_label.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        social_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        social_label.setStyleSheet("color: #ff9500; margin-top: 5px;")
        layout.addWidget(social_label)

        website_btn = QPushButton("🌐 Website")
        website_btn.setFont(QFont("Segoe UI", 10))
        website_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        website_btn.setStyleSheet("""
            QPushButton {
                background-color: #333333;
                color: #ff9500;
                border: 1px solid #ff9500;
                border-radius: 20px;
                padding: 8px;
                font-size: 12px;
                font-weight: bold;
                min-width: 150px;
            }
            QPushButton:hover {
                background-color: #ff9500;
                color: #ffffff;
                border-color: #ff9500;
            }
            QPushButton:pressed {
                background-color: #cc7700;
            }
        """)
        website_btn.clicked.connect(self.open_website)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(website_btn)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        copyright_label = QLabel("© 2026 Alexander Suvorov. All rights reserved.")
        copyright_label.setFont(QFont("Segoe UI", 10))
        copyright_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        copyright_label.setStyleSheet("color: #666666; margin-top: 15px;")
        layout.addWidget(copyright_label)

        self.setLayout(layout)

    def open_github(self):
        import webbrowser
        webbrowser.open("https://github.com/aixandrolab/calculator")

    def open_profile(self):
        import webbrowser
        webbrowser.open("https://github.com/aixandrolab")

    def open_website(self):
        import webbrowser
        webbrowser.open("https://aixandrolab.ru")
