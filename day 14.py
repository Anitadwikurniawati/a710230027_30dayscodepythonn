import random

def main():
    while True:
        print("\nSelamat datang di Permainan Tebak Angka!")
        
        try:
            min_range = int(input("Masukkan angka minimum: "))
            max_range = int(input("Masukkan angka maksimum: "))
            
            if min_range >= max_range:
                print("Angka minimum harus lebih kecil dari angka maksimum.")
                continue
        except ValueError:
            print("Input tidak valid. Harap masukkan angka bulat.")
            continue
        
        print(f"Saya memikirkan sebuah angka antara {min_range} dan {max_range}.")
        
        number_to_guess = random.randint(min_range, max_range)
        max_attempts = 10
        attempts = 0
        guess_history = []
        
        while attempts < max_attempts:
            try:
                guess = int(input("Masukkan tebakan Anda: "))
                attempts += 1
                guess_history.append(guess)
                
                if guess < number_to_guess:
                    print("Terlalu rendah! Coba lagi.")
                elif guess > number_to_guess:
                    print("Terlalu tinggi! Coba lagi.")
                else:
                    print(f"Selamat! Anda berhasil menebak angka dalam {attempts} percobaan.")
                    print(f"Riwayat tebakan Anda: {guess_history}")
                    break
                
                if attempts == 5:
                    hint_range = max((max_range - min_range) // 10, 1)
                    hint_min = max(min_range, number_to_guess - hint_range)
                    hint_max = min(max_range, number_to_guess + hint_range)
                    print(f"Petunjuk: Angka yang saya pikirkan ada di antara {hint_min} dan {hint_max}.")
                
            except ValueError:
                print("Input tidak valid. Harap masukkan angka bulat.")
        
        if attempts == max_attempts:
            print(f"Maaf, Anda telah mencapai batas maksimal {max_attempts} percobaan.")
            print(f"Angka yang saya pikirkan adalah {number_to_guess}.")
        
        play_again = input("Apakah Anda ingin bermain lagi? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()
