import typing

from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMainWindow, QStackedWidget


from widgets import GridWidget


class Page(QWidget):

    def __init__(self, name: str):
        super(Page, self).__init__()
        vLayout = QVBoxLayout(self)
        self.btn_page = QPushButton(name, self)
        vLayout.addWidget(self.btn_page)


class Aplication(QMainWindow):

    def __init__(self, *args) -> None:
        super(Aplication, self).__init__()
        self.aplication_widget = QStackedWidget(self)

    def creat_page(self, page: Page):
        self.newPage = page
        self.aplication_widget.addWidget(self.newPage)

    def change_page(self, toPage: Page):
        self.aplication_widget.setCurrentWidget(toPage)
