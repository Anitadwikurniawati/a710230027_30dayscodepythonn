import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit

class BaseWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def on_click(self):
        raise NotImplementedError("Subclasses should implement this method")

class LabelWidget(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.label = QLabel("Label Widget", self)

    def on_click(self):
        self.label.setText("Label was clicked!")

class TextEditWidget(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlainText("Text Edit Widget")

    def on_click(self):
        self.text_edit.setPlainText("Text Edit was clicked!")

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.button = QPushButton("Click Me", self)
        self.button.clicked.connect(self.on_button_click)

        self.label_widget = LabelWidget(self)
        self.text_edit_widget = TextEditWidget(self)

        layout.addWidget(self.button)
        layout.addWidget(self.label_widget)
        layout.addWidget(self.text_edit_widget)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 Polymorphism Example')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def on_button_click(self):
        self.label_widget.on_click()
        self.text_edit_widget.on_click()

def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
