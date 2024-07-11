import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLineEdit, QPushButton

class HargaHpApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Daftar Pencarian Harga HP")
        self.setGeometry(100, 100, 600, 400)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Masukkan nama HP")
        self.layout.addWidget(self.search_bar)
        
        self.search_button = QPushButton("Cari", self)
        self.search_button.clicked.connect(self.search)
        self.layout.addWidget(self.search_button)
        
        self.table = QTableWidget(self)
        self.table.setRowCount(0)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Nama HP", "Harga"])
        self.layout.addWidget(self.table)
        
        self.data = [
            {"nama": "Samsung Galaxy S21", "harga": "Rp 12.000.000"},
            {"nama": "iPhone 12", "harga": "Rp 15.000.000"},
            {"nama": "Xiaomi Mi 11", "harga": "Rp 9.000.000"},
            {"nama": "Oppo Find X3", "harga": "Rp 10.000.000"},
        ]
        
        self.load_data()
    
    def load_data(self):
        self.table.setRowCount(0)
        for item in self.data:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(item["nama"]))
            self.table.setItem(row_position, 1, QTableWidgetItem(item["harga"]))
    
    def search(self):
        query = self.search_bar.text().lower()
        filtered_data = [item for item in self.data if query in item["nama"].lower()]
        
        self.table.setRowCount(0)
        for item in filtered_data:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(item["nama"]))
            self.table.setItem(row_position, 1, QTableWidgetItem(item["harga"]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HargaHpApp()
    window.show()
    sys.exit(app.exec_())
