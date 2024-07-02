import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

class BaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Base Window')
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel('Ini adalah Base Window', self)
        self.label.move(50, 50)

        self.show()

class TextInputWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        super().initUI()
        self.setWindowTitle('Text Input Window')
        self.label.setText('Masukkan teks di bawah:')

        self.text_input = QLineEdit(self)
        self.text_input.move(50, 100)
        
        self.button = QPushButton('Submit', self)
        self.button.move(50, 130)
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        input_text = self.text_input.text()
        self.label.setText(f'Teks yang dimasukkan: {input_text}')

class ComboBoxWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        super().initUI()
        self.setWindowTitle('ComboBox Window')
        self.label.setText('Pilih item dari combo box:')

        self.combo_box = QComboBox(self)
        self.combo_box.addItems(['Item 1', 'Item 2', 'Item 3'])
        self.combo_box.move(50, 100)
        
        self.button = QPushButton('Submit', self)
        self.button.move(50, 130)
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        selected_item = self.combo_box.currentText()
        self.label.setText(f'Item yang dipilih: {selected_item}')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    text_input_window = TextInputWindow()

    combo_box_window = ComboBoxWindow()
    combo_box_window.move(400, 100) 
    
    sys.exit(app.exec_())
