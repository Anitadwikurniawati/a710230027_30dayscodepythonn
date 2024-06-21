from collections import Counter

def hitung_angka(data):
    counter = Counter(data)
    
    for angka, jumlah in counter.items():
        print(f"Angka {angka} muncul sebanyak {jumlah} kali")

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]

hitung_angka(data)
