# ДЗ: Наследование, Полиморфизм, Инкапсуляция 2

class BankAccount:

    def __init__(self, balance=0.0):
        self.__balance__ = round(balance, 2)
        self.__account_id__ = id(self)
        self.__currency__ = 'USD'

    def deposit(self, amount: float):
        if amount <= 0:
            print("\nError, cannot deposit negative amount.")
            return
        self.__balance__ += round(amount, 2)
        print(f"\nSuccessfully deposit {round(amount, 2)} to ID{self.__account_id__} account.")

    def withdrawal(self, amount: float):
        if amount <= 0:
            print("\nError, cannot withdraw negative amount.")
            return
        elif self.__balance__ < round(amount, 2):
            print("\nError, Not sufficient funds to withdraw.")
            return
        self.__balance__ -= round(amount, 2)
        print(f"\nSuccessfully withdraw {round(amount, 2)} from ID{self.__account_id__} account.")

    def check_balance(self):
        print(f"Current balance of account ID{self.__account_id__} is: {self.__balance__:0.2f} {self.__currency__}")


def main():
    denys_account = BankAccount(1000)
    denys_account.check_balance()
    katya_account = BankAccount(0)
    katya_account.check_balance()
    try:
        denys_account.deposit(100.15999)
        denys_account.withdrawal(1100.16)
        katya_account.withdrawal(1000)
    except (ValueError, TypeError):
        print("Incorrect value")
    denys_account.check_balance()
    katya_account.check_balance()


if __name__ == '__main__':
    main()
