import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class TebakKataGame(QWidget):
    def __init__(self):
        super().__init__()

        self.words = ['python', 'java', 'kotlin', 'javascript', 'swift']
        self.target_word = random.choice(self.words)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tebak Kata')

        self.layout = QVBoxLayout()

        self.instructions = QLabel('Guess the word:')
        self.layout.addWidget(self.instructions)

        self.input_field = QLineEdit(self)
        self.layout.addWidget(self.input_field)

        self.check_button = QPushButton('Check', self)
        self.check_button.clicked.connect(self.check_guess)
        self.layout.addWidget(self.check_button)

        self.result_label = QLabel('')
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)
        self.show()

    def check_guess(self):
        guess = self.input_field.text().strip().lower()

        if guess == self.target_word:
            self.result_label.setText('Congratulations! You guessed the word!')
            self.show_message('Success', 'You guessed the word!')
        else:
            self.result_label.setText('Wrong guess! Try again.')

    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TebakKataGame()
    sys.exit(app.exec_())
