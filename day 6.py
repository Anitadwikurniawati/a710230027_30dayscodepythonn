import random

def get_computer_choice():
    choices = ["kertas", "batu", "gunting"]
    return random.choice(choices)

def get_user_choice():
    choice = input("Masukkan pilihanmu (kertas, batu, gunting): ").lower()
    while choice not in ["kertas", "batu", "gunting"]:
        choice = input("Pilihan tidak valid. Masukkan pilihanmu (kertas, batu, gunting): ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Seri!"
    elif (user_choice == "kertas" and computer_choice == "batu") or \
         (user_choice == "batu" and computer_choice == "gunting") or \
         (user_choice == "gunting" and computer_choice == "kertas"):
        return "Kamu menang!"
    else:
        return "Komputer menang!"

def main():
    print("Selamat datang di permainan Kertas, Batu, Gunting!")
    
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    
    print(f"Komputer memilih: {computer_choice}")
    print(f"Kamu memilih: {user_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
