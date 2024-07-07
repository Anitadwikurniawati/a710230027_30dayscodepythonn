import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class GuessingGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Guess the Final Score")
        self.setGeometry(100, 100, 300, 200)

        self.target_score = random.randint(1, 100)

        self.layout = QVBoxLayout()

        self.label = QLabel("Guess the final score (between 1 and 100):")
        self.layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        self.layout.addWidget(self.input_field)

        self.submit_button = QPushButton("Submit Guess", self)
        self.submit_button.clicked.connect(self.check_guess)
        self.layout.addWidget(self.submit_button)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def check_guess(self):
        try:
            guess = int(self.input_field.text())
            if guess == self.target_score:
                self.result_label.setText(f"Correct! The score was {self.target_score}.")
                QMessageBox.information(self, "Result", f"Correct! The score was {self.target_score}.")
                self.reset_game()
            elif guess < self.target_score:
                self.result_label.setText("Too low! Try again.")
            else:
                self.result_label.setText("Too high! Try again.")
        except ValueError:
            self.result_label.setText("Please enter a valid number.")

    def reset_game(self):
        self.target_score = random.randint(1, 100)
        self.input_field.clear()

def main():
    app = QApplication(sys.argv)
    game = GuessingGame()
    game.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
