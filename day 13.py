class TesGulaDarah:
    def __init__(self):
        self.level_gula = None

    def input_gula_darah(self):
        try:
            self.level_gula = float(input("Masukkan level gula darah Anda (mg/dL): "))
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
            self.input_gula_darah()

    def hasil_dan_rekomendasi(self):
        if self.level_gula < 70:
            return "Gula darah rendah (Hipoglikemia). Disarankan untuk segera mengkonsumsi makanan atau minuman yang mengandung gula."
        elif 70 <= self.level_gula < 100:
            return "Gula darah normal. Pertahankan pola makan dan gaya hidup sehat."
        elif 100 <= self.level_gula < 125:
            return "Pra-diabetes. Disarankan untuk menjaga pola makan, olahraga teratur, dan konsultasi dengan dokter."
        else:
            return "Diabetes. Disarankan untuk segera konsultasi dengan dokter untuk mendapatkan penanganan yang tepat."

    def mulai_tes(self):
        print("Selamat datang di tes gula darah!")
        self.input_gula_darah()
        hasil = self.hasil_dan_rekomendasi()
        print(f"Hasil tes gula darah Anda: {self.level_gula} mg/dL")
        print(f"Rekomendasi: {hasil}")

if __name__ == "__main__":
    tes = TesGulaDarah()
    tes.mulai_tes()
