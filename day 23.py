import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QPushButton, QFormLayout, QComboBox

class BiodataForm(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QFormLayout()

        self.nameLabel = QLabel('Nama:')
        self.nameEdit = QLineEdit()
        
        self.addressLabel = QLabel('Alamat:')
        self.addressEdit = QTextEdit()
        
        self.phoneLabel = QLabel('Telepon:')
        self.phoneEdit = QLineEdit()
        
        self.emailLabel = QLabel('Email:')
        self.emailEdit = QLineEdit()
        
        self.genderLabel = QLabel('Jenis Kelamin:')
        self.genderCombo = QComboBox()
        self.genderCombo.addItems(['Laki-laki', 'Perempuan', 'Lainnya'])
        
        self.hobbiesLabel = QLabel('Hobi:')
        self.hobbiesEdit = QTextEdit()
        
        self.submitButton = QPushButton('Submit')
        self.submitButton.clicked.connect(self.submitForm)

        layout.addRow(self.nameLabel, self.nameEdit)
        layout.addRow(self.addressLabel, self.addressEdit)
        layout.addRow(self.phoneLabel, self.phoneEdit)
        layout.addRow(self.emailLabel, self.emailEdit)
        layout.addRow(self.genderLabel, self.genderCombo)
        layout.addRow(self.hobbiesLabel, self.hobbiesEdit)
        layout.addRow(self.submitButton)

        self.setLayout(layout)
        self.setWindowTitle('Formulir Biodata Diri')
        self.show()

    def submitForm(self):
        name = self.nameEdit.text()
        address = self.addressEdit.toPlainText()
        phone = self.phoneEdit.text()
        email = self.emailEdit.text()
        gender = self.genderCombo.currentText()
        hobbies = self.hobbiesEdit.toPlainText()

        print(f'Nama: {name}')
        print(f'Alamat: {address}')
        print(f'Telepon: {phone}')
        print(f'Email: {email}')
        print(f'Jenis Kelamin: {gender}')
        print(f'Hobi: {hobbies}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = BiodataForm()
    sys.exit(app.exec_())
