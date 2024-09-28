import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("Tebak Angka antara 1 sampai 10: ")
    guess = int(guess)

    if guess == num:
        print("Tebakan Kamu Benar!")
        break
    else:
        print("Coba Lagi")