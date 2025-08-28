# python slot machine
import random


def spin_row():
    symbols = ['🕷️', '🦋', '🪱', '🦣', '🪼']

    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" ".join(row))


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🕷️':
            return bet * 3
        elif row[0] == '🦋':
            return bet * 5
        elif row[0] == '🪱':
            return bet * 10
        elif row[0] == '🦣':
            return bet * 20
        elif row[0] == '🪼':
            return bet * 10000

    return 0


def main():
    balance = 100
    print("***********************")
    print("Welcome to python slots")
    print("Symbols: 🕷️ 🦋 🪱 🦣 🪼")
    print("***********************")

    while balance > 0:
        print(f"Current balance:${balance}")

        bet = input("Place your bet: ")
        if not bet.isdigit():
            print("Please enter a valid number: ")
            continue

        bet = int(bet)

        if bet > balance:
            print("Brokie get some money")
            continue

        if bet <= 0:
            print("should be more than 0")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning..../n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won mate ${payout}")
        else:
            print("You lost")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if not play_again == 'Y':
            break

    print(f"Your final balance is ${balance}: ")


if __name__ == '__main__':
    main()
