import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')

        self.layout = QVBoxLayout()

        self.result = QLineEdit()
        self.layout.addWidget(self.result)

        self.buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in self.buttons:
            hbox = QHBoxLayout()
            for button in row:
                btn = QPushButton(button)
                btn.clicked.connect(self.on_click)
                hbox.addWidget(btn)
            self.layout.addLayout(hbox)

        self.setLayout(self.layout)

    def on_click(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == '=':
            try:
                expression = self.result.text()
                result = eval(expression)
                self.result.setText(str(result))
            except Exception as e:
                self.result.setText('Error')
        else:
            current_text = self.result.text()
            new_text = current_text + button_text
            self.result.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
