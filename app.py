# Copyright (c) 2023-2026, Alexander Suvorov. All rights reserved.
import sys

from PyQt6.QtWidgets import QApplication

from core.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    calculator = MainWindow()
    calculator.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()