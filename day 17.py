import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Input Example'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 400, 200)

        # Create layout
        layout = QVBoxLayout()

        # Create a label
        self.label = QLabel('Enter your name:', self)
        layout.addWidget(self.label)

        # Create a line edit
        self.line_edit = QLineEdit(self)
        layout.addWidget(self.line_edit)

        # Create a button
        self.button = QPushButton('Show Name', self)
        self.button.clicked.connect(self.show_name)
        layout.addWidget(self.button)

        # Set layout
        self.setLayout(layout)

        self.show()

    def show_name(self):
        name = self.line_edit.text()
        self.label.setText(f'Hello, {name}!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
