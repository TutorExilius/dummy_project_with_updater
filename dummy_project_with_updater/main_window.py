from pathlib import Path

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from pip._vendor import requests


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        """Initialise the MainWindow widget."""

        super().__init__()
        uic.loadUi(Path(__file__).parent / "ui" / "main_window.ui", self)

        # connections
        self.actionUpdate.triggered.connect(self.check_update)

    def check_update(self):
        result = QMessageBox.question(
            self,
            "Update",
            "Check for updates?")

        if result == QMessageBox.Yes:
            r = requests.get(
                'https://github.com/TutorExilius/dummy_project_with_updater/currentverison')
            print(r.content)

