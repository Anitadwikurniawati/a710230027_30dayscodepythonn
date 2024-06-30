import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class BirthdayApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Happy Birthday")

        self.birthday_label = QLabel("Happy Birthday!", self)
        self.birthday_label.setFont(QFont('Arial', 40))
        self.birthday_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.birthday_label)

        self.setLayout(layout)

        self.resize(400, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BirthdayApp()
    window.show()
    sys.exit(app.exec_())
