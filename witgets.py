from PyQt6.QtWidgets import QPushButton, QCheckBox, QLabel, QWidget, QVBoxLayout, QToolBar, QGridLayout, QPushButton
from PyQt6.QtGui import QAction, QPixmap


class FastWitget(QWidget):

    def __init__(self,
                 titleNav: str,
                 width: int = 900,
                 height: int = 400,
                 parent=None):
        super().__init__(parent)
        self.title = titleNav
        self.setWindowTitle(titleNav)
        self.setMinimumSize(width, height)
        # self.resize(width, height)
        print(f"Window size set to {width} x {height}")

    def create_button(self, text, callback: callable, *args):
        button = QPushButton(text)
        button.clicked.connect(lambda _: callback(args))
        return button

    def create_checkbox(self, text, callback: callable):
        checkbox = QCheckBox(text)
        checkbox.stateChanged.connect(callback)
        return checkbox

    def create_label(self, text: str, ejeX: int = 0, ejeY: int = 0):
        label = QLabel(text)
        label.move(ejeX, ejeY)
        return label

    def create_page(self, widgets: list):
        page = QWidget()
        layout = QVBoxLayout()
        for widget in widgets:
            layout.addWidget(widget)
        page.setLayout(layout)
        page.setWindowTitle(self.title)
        return page

    def create_toolbar(self, actions: callable):
        toolbar = QToolBar()
        for action in actions:
            toolbar.addAction(action)
        self.addToolBar(toolbar)
        return toolbar

    def create_nav(self, name: str, callback: callable):
        btn_nav = self.create_button(name, callback)
        self.layout().addWidget(btn_nav)
        btn_nav.clicked.connect(callback)


class GridWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid = QGridLayout()
        self.setLayout(self.grid)

    def add_widget(self, widget, row: int, col: int):
        self.grid.addWidget(widget, row, col)

    def remove_widget(self, widget):
        self.grid.removeWidget(widget)

    def move_widget(self, widget, row: int, col: int):
        self.grid.addWidget(widget, row, col)

    def create_button(self, text, callback: callable, row: int, col: int):
        button = QPushButton(text)
        button.clicked.connect(callback)
        self.add_widget(button, row, col)
        return button
