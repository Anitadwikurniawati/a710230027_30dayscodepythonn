class Khodam:
    def __init__(self, name, element, description, type):
        self.name = name
        self.element = element
        self.description = description
        self.type = type
    
    def get_info(self):
        return f"Nama Khodam: {self.name}\nElemen: {self.element}\nJenis: {self.type}\nDeskripsi: {self.description}"

khodam_list = [
    Khodam("Khodam Api Pelindung", "Api", "Khodam pelindung yang berhubungan dengan elemen api, sangat kuat dalam melindungi pemiliknya dari bahaya.", "Pelindung"),
    Khodam("Khodam Air Pembimbing", "Air", "Khodam pembimbing yang berhubungan dengan elemen air, dikenal bijaksana dan penuh ketenangan, membantu dalam pengambilan keputusan.", "Pembimbing"),
    Khodam("Khodam Tanah Penyembuh", "Tanah", "Khodam penyembuh yang berhubungan dengan elemen tanah, mampu memberikan energi penyembuhan dan stabilitas.", "Penyembuh"),
    Khodam("Khodam Angin Pengawal", "Angin", "Khodam pengawal yang berhubungan dengan elemen angin, cepat dan lincah dalam melindungi pemiliknya dari ancaman.", "Pengawal"),
    Khodam("Khodam Api Pembakar", "Api", "Khodam yang memiliki kekuatan api, mampu menghanguskan halangan yang ada di hadapan pemiliknya.", "Pembakar"),
    Khodam("Khodam Air Penyucian", "Air", "Khodam yang menggunakan elemen air untuk menyucikan dan membersihkan energi negatif di sekitarnya.", "Penyucian"),
    Khodam("Khodam Tanah Pembangun", "Tanah", "Khodam yang membantu dalam pembangunan dan penciptaan fondasi yang kuat.", "Pembangun"),
    Khodam("Khodam Angin Pengembara", "Angin", "Khodam yang berkelana dan membawa pesan serta inspirasi dari berbagai penjuru.", "Pengembara")
]

def find_khodam(description):
    for khodam in khodam_list:
        if khodam.element.lower() in description.lower() or khodam.type.lower() in description.lower():
            return khodam.get_info()
    return "Deskripsi tidak sesuai dengan jenis khodam yang diketahui."

description = input("Masukkan deskripsi khodam: ")

khodam_info = find_khodam(description)
print(khodam_info)
