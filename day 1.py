class HewanPeliharaan:
    def makan(self):
        raise NotImplementedError

    def suara(self):
        raise NotImplementedError

class Kucing(HewanPeliharaan):
    def makan(self):
        return "Kucing sedang makan ikan"

    def suara(self):
        return "Kucing mengeong: Meow"

class Anjing(HewanPeliharaan):
    def makan(self):
        return "Anjing sedang makan daging"

    def suara(self):
        return "Anjing menggonggong: Woof"

class Burung(HewanPeliharaan):
    def makan(self):
        return "Burung sedang makan biji-bijian"

    def suara(self):
        return "Burung berkicau: Tweet"

class PemilikHewan:
    def __init__(self, nama):
        self.nama = nama
        self.hewan_peliharaan = []

    def tambah_hewan_peliharaan(self, hewan):
        self.hewan_peliharaan.append(hewan)

    def beri_makan_semua(self):
        for hewan in self.hewan_peliharaan:
            print(hewan.makan())

    def dengar_suara_semua(self):
        for hewan in self.hewan_peliharaan:
            print(hewan.suara())

kucing = Kucing()
anjing = Anjing()
burung = Burung()

pemilik = PemilikHewan("Andi")
pemilik.tambah_hewan_peliharaan(kucing)
pemilik.tambah_hewan_peliharaan(anjing)
pemilik.tambah_hewan_peliharaan(burung)

print(f"Pemilik hewan: {pemilik.nama}")
print("Memberi makan semua hewan peliharaan:")
pemilik.beri_makan_semua()  

print("\nMendengar suara semua hewan peliharaan:")
pemilik.dengar_suara_semua() 
