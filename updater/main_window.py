from pathlib import Path

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        """Initialise the MainWindow widget."""

        super().__init__()
        uic.loadUi(Path(__file__).parent / "ui" / "main_window.ui", self)
