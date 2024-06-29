import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QDateEdit
from PyQt5.QtCore import QDate

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Form Input Data")
        self.setGeometry(100, 100, 400, 400)

        self.name_label = QLabel("Nama:", self)
        self.name_input = QLineEdit(self)

        self.place_label = QLabel("Tempat Lahir:", self)
        self.place_input = QLineEdit(self)

        self.date_label = QLabel("Tanggal Lahir:", self)
        self.date_input = QDateEdit(self)
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.display_data)

        self.text_display = QTextEdit(self)
        self.text_display.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.place_label)
        layout.addWidget(self.place_input)
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.text_display)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def display_data(self):
        name = self.name_input.text()
        place = self.place_input.text()
        date = self.date_input.date().toString("dd-MM-yyyy")

        message = f"Nama: {name}\nTempat Lahir: {place}\nTanggal Lahir: {date}"
        self.text_display.setText(message)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
