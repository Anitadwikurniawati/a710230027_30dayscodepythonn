def hitung_rata_rata(usia_list):
    jumlah = sum(usia_list)
    rata_rata = jumlah / len(usia_list)
    return rata_rata

def main():
    usia_list = []
    
    jumlah_lansia = int(input("Masukkan jumlah lansia yang ingin dihitung rata-rata usianya: "))
    
    for i in range(jumlah_lansia):
        usia = int(input(f"Masukkan usia lansia ke-{i+1}: "))
        usia_list.append(usia)
    
    rata_rata = hitung_rata_rata(usia_list)
    
    print(f"Rata-rata usia dari lansia yang dimasukkan adalah: {rata_rata:.2f} tahun")

if __name__ == "__main__":
    main()
