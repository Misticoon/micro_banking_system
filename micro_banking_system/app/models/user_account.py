# user_account.py

import random
import string

class UserAccount():
    def __init__(self, first_name, last_name, username, password, balance=0, bank_account_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.balance = balance
        self.bank_account_id = bank_account_id if bank_account_id else self.generate_bank_account_id()

    def generate_bank_account_id(self):
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        numbers = ''.join(random.choices(string.digits, k=3))
        return numbers + letters
