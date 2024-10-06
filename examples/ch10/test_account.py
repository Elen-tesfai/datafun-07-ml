from account import Account
from decimal import Decimal

def test_account():
    account = Account('John Doe', Decimal('100.00'))
    print(f'Account created: {account.name} with balance {account.balance}')

    account.deposit(Decimal('50.00'))
    print(f'After deposit: {account.balance}')

    try:
        account.deposit(Decimal('-10.00'))
    except ValueError as e:
        print(f'Error: {e}')

    try:
        Account('Jane Doe', Decimal('-50.00'))
    except ValueError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    test_account()