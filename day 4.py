class ProgramStudi:
    def __init__(self, nama, jenjang):
        self.nama = nama
        self.jenjang = jenjang

    def deskripsi(self):
        return f"{self.nama} ({self.jenjang})"

class FakultasTeknik(ProgramStudi):
    def __init__(self, nama, jenjang):
        super().__init__(nama, jenjang)

    def deskripsi(self):
        return f"Fakultas Teknik: {super().deskripsi()}"

class FakultasEkonomi(ProgramStudi):
    def __init__(self, nama, jenjang):
        super().__init__(nama, jenjang)

    def deskripsi(self):
        return f"Fakultas Ekonomi: {super().deskripsi()}"

class FakultasIlmuKomputer(ProgramStudi):
    def __init__(self, nama, jenjang):
        super().__init__(nama, jenjang)

    def deskripsi(self):
        return f"Fakultas Ilmu Komputer: {super().deskripsi()}"

teknik_informatika = FakultasTeknik("Teknik Informatika", "S1")
teknik_sipil = FakultasTeknik("Teknik Sipil", "S1")

manajemen = FakultasEkonomi("Manajemen", "S1")
akuntansi = FakultasEkonomi("Akuntansi", "S1")

sistem_informasi = FakultasIlmuKomputer("Sistem Informasi", "S1")
ilmu_komputer = FakultasIlmuKomputer("Ilmu Komputer", "S1")

print(teknik_informatika.deskripsi())  
print(teknik_sipil.deskripsi())
print(manajemen.deskripsi())           
print(akuntansi.deskripsi())           
print(sistem_informasi.deskripsi())    
print(ilmu_komputer.deskripsi())       