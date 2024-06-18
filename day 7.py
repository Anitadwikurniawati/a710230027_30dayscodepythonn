def hitung_huruf(kalimat, huruf):
    """
    Menghitung berapa kali huruf muncul dalam kalimat.
    :param kalimat: Kalimat yang akan dianalisis
    :param huruf: Huruf yang akan dihitung kemunculannya
    :return: Jumlah kemunculan huruf dalam kalimat
    """
    jumlah = kalimat.count(huruf)
    return jumlah

def main():
    print("Selamat datang di permainan tebak huruf!")
    
    kalimat = input("Masukkan sebuah kalimat: ")
    
    while True:
        huruf = input("Masukkan sebuah huruf yang ingin dihitung (atau ketik 'keluar' untuk berhenti): ")
        
        if huruf.lower() == 'keluar':
            print("Terima kasih sudah bermain!")
            break
        
        if len(huruf) != 1:
            print("Harap masukkan satu huruf saja.")
            continue
        
        jumlah = hitung_huruf(kalimat, huruf)
        
        print(f"Huruf '{huruf}' muncul sebanyak {jumlah} kali dalam kalimat.")

if __name__ == "__main__":
    main()
