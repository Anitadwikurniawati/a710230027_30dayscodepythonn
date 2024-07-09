import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox, QHeaderView, QFileDialog

class StokBarangApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Stok Barang")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Nama Barang", "Jumlah", "Harga"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        self.form_layout = QHBoxLayout()
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nama Barang")
        self.form_layout.addWidget(self.name_input)
        
        self.quantity_input = QLineEdit()
        self.quantity_input.setPlaceholderText("Jumlah")
        self.form_layout.addWidget(self.quantity_input)
        
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Harga")
        self.form_layout.addWidget(self.price_input)
        
        self.add_button = QPushButton("Tambah Barang")
        self.add_button.clicked.connect(self.add_item)
        self.form_layout.addWidget(self.add_button)
        
        self.edit_button = QPushButton("Edit Barang")
        self.edit_button.clicked.connect(self.edit_item)
        self.form_layout.addWidget(self.edit_button)
        
        self.delete_button = QPushButton("Hapus Barang")
        self.delete_button.clicked.connect(self.delete_item)
        self.form_layout.addWidget(self.delete_button)
        
        self.layout.addLayout(self.form_layout)
        
        self.save_button = QPushButton("Simpan ke CSV")
        self.save_button.clicked.connect(self.save_to_csv)
        self.layout.addWidget(self.save_button)
        
        self.load_button = QPushButton("Muat dari CSV")
        self.load_button.clicked.connect(self.load_from_csv)
        self.layout.addWidget(self.load_button)

    def add_item(self):
        name = self.name_input.text()
        quantity = self.quantity_input.text()
        price = self.price_input.text()

        if name and quantity and price:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(name))
            self.table.setItem(row_position, 1, QTableWidgetItem(quantity))
            self.table.setItem(row_position, 2, QTableWidgetItem(price))
            
            self.name_input.clear()
            self.quantity_input.clear()
            self.price_input.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Semua kolom harus diisi")

    def edit_item(self):
        current_row = self.table.currentRow()
        if current_row >= 0:
            name = self.name_input.text()
            quantity = self.quantity_input.text()
            price = self.price_input.text()

            if name and quantity and price:
                self.table.setItem(current_row, 0, QTableWidgetItem(name))
                self.table.setItem(current_row, 1, QTableWidgetItem(quantity))
                self.table.setItem(current_row, 2, QTableWidgetItem(price))
                
                self.name_input.clear()
                self.quantity_input.clear()
                self.price_input.clear()
            else:
                QMessageBox.warning(self, "Input Error", "Semua kolom harus diisi")
        else:
            QMessageBox.warning(self, "Selection Error", "Pilih barang yang ingin diedit")

    def delete_item(self):
        current_row = self.table.currentRow()
        if current_row >= 0:
            self.table.removeRow(current_row)
        else:
            QMessageBox.warning(self, "Selection Error", "Pilih barang yang ingin dihapus")

    def save_to_csv(self):
        path, _ = QFileDialog.getSaveFileName(self, "Simpan ke CSV", "", "CSV Files (*.csv)")
        if path:
            data = []
            for row in range(self.table.rowCount()):
                row_data = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                data.append(row_data)
            df = pd.DataFrame(data, columns=["Nama Barang", "Jumlah", "Harga"])
            df.to_csv(path, index=False)

    def load_from_csv(self):
        path, _ = QFileDialog.getOpenFileName(self, "Muat dari CSV", "", "CSV Files (*.csv)")
        if path:
            df = pd.read_csv(path)
            self.table.setRowCount(0)
            for i, row in df.iterrows():
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                self.table.setItem(row_position, 0, QTableWidgetItem(row["Nama Barang"]))
                self.table.setItem(row_position, 1, QTableWidgetItem(str(row["Jumlah"])))
                self.table.setItem(row_position, 2, QTableWidgetItem(str(row["Harga"])))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StokBarangApp()
    window.show()
    sys.exit(app.exec_())
