# Copyright (c) 2023-2026, Alexander Suvorov. All rights reserved.
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont


class CalcButton(QPushButton):

    def __init__(self, text, color="#2d2d2d", text_color="#ffffff", size_hint=(1, 1)):
        super().__init__(text)
        self.setFixedSize(80 * size_hint[0], 80)
        self.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: {text_color};
                border: none;
                border-radius: 40px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {self.adjust_brightness(color, 1.2)};
            }}
            QPushButton:pressed {{
                background-color: {self.adjust_brightness(color, 0.8)};
            }}
        """)

    @staticmethod
    def adjust_brightness(hex_color, factor):
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        r = min(255, int(r * factor))
        g = min(255, int(g * factor))
        b = min(255, int(b * factor))
        return f"#{r:02x}{g:02x}{b:02x}"


class NumberButton(CalcButton):

    def __init__(self, text):
        super().__init__(text, color="#333333", text_color="#ffffff")


class OperatorButton(CalcButton):

    def __init__(self, text):
        super().__init__(text, color="#ff9500", text_color="#ffffff")


class FunctionButton(CalcButton):

    def __init__(self, text):
        super().__init__(text, color="#a6a6a6", text_color="#000000")


class EqualsButton(CalcButton):

    def __init__(self):
        super().__init__("=", color="#ff9500", text_color="#ffffff", size_hint=(1, 1))
