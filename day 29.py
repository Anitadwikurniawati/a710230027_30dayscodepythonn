import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class TiktokSalesLink(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        nameLabel = QLabel('Nama Barang:')
        self.nameEdit = QLineEdit()
        
        priceLabel = QLabel('Harga:')
        self.priceEdit = QLineEdit()
        
        linkLabel = QLabel('Link TikTok:')
        self.linkEdit = QLineEdit()
        
        saveButton = QPushButton('Simpan')
        saveButton.clicked.connect(self.saveData)
        
        formLayout = QVBoxLayout()
        formLayout.addWidget(nameLabel)
        formLayout.addWidget(self.nameEdit)
        formLayout.addWidget(priceLabel)
        formLayout.addWidget(self.priceEdit)
        formLayout.addWidget(linkLabel)
        formLayout.addWidget(self.linkEdit)
        
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(saveButton)
        
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(formLayout)
        mainLayout.addLayout(buttonLayout)
        
        self.setLayout(mainLayout)
        
        self.setWindowTitle('Link Penjualan Barang di TikTok')
        self.setGeometry(100, 100, 400, 200)
        self.show()
    
    def saveData(self):
        name = self.nameEdit.text()
        price = self.priceEdit.text()
        link = self.linkEdit.text()
        
        if name and price and link:
            QMessageBox.information(self, 'Data Tersimpan', f'Nama Barang: {name}\nHarga: {price}\nLink TikTok: {link}')
        else:
            QMessageBox.warning(self, 'Data Tidak Lengkap', 'Silakan isi semua kolom.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TiktokSalesLink()
    sys.exit(app.exec_())
