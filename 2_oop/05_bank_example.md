# Object Oriented Programming

## Bank Example

In this example, we will use the concepts of **encapsulation**m **private attributes**, and **validations** for these **attributes**.

```python
class BankAccount:

    def __init__(self, account_number: int, balance: float):
        self._acount_number: int = account_number # protected
        self.__balance: float = balance # private

    def get_balance(self) -> float:
        return self.__balance

    def set_balance(self, balance: float) -> None:
        if balance > 0:
            self.__balance = balance
        else:
            print("Invalid balance!")

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdraw amount!")


account: BankAccount = BankAccount("2131313", 100.50)

print(f"Account number: {account._acount_number}")

print(f"Initial balance: {account.get_balance()}")
account.set_balance(500)
print(f"Updated balance: {account.get_balance()}")

account.deposit(100)
print(f"Balance after deposit: {account.get_balance()}")
account.withdraw(50)
print(f"Balance after withdrawal: {account.get_balance()}")

```

In this example, we have **getter method** for the **private attribute**, **setter method** for the **private attribute**, **public method** that uses the **private attribute**.

