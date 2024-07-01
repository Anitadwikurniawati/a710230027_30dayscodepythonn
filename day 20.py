import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox

class MenyatakanCintaApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Menyatakan Cinta')
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        btn4 = QPushButton('Will you be my partner?', self)
        btn4.clicked.connect(lambda: self.showConfirmation('Will you be my partner?'))
        layout.addWidget(btn4)
        
        self.setLayout(layout)
        
    def showConfirmation(self, message):
        reply = QMessageBox.question(self, 'Menyatakan Cinta', message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, 'Jawaban', 'Ya, saya mau!')
        else:
            QMessageBox.information(self, 'Jawaban', 'Maaf, saya belum siap.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MenyatakanCintaApp()
    ex.show()
    sys.exit(app.exec_())
