'''
How this code demonstrates all OOP concepts:

1) Encapsulation: Private attributes, accessed via methods.

2) Inheritance: SavingsAccount and CurrentAccount inherit from Account.

3) Polymorphism: withdraw behaves differently in subclasses.

4) Abstraction: AbstractAccount defines a common interface.

EXTRA) Association/Composition: Bank class manages multiple accounts in a collection.

'''


############################################# PYTHON CODE #######################################3
# STEP 1: Encapsulation
# OOP Concept: Encapsulation means keeping sensitive data private inside a class and only allowing access through methods.
# What to Do: Define private fields for account details and provide public methods to access or modify them.

class Account:
    def __init__(self, account_number, owner, initial_balance=0):
        # Private attributes (by convention, use underscore)
        self._account_number = account_number
        self._owner = owner
        self._balance = initial_balance

    # Public getter for balance
    def get_balance(self):
        return self._balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")

    # Public method to get account info
    def get_account_info(self):
        return f"Account: {self._account_number}, Owner: {self._owner}, Balance: {self._balance}"

# STEP 2: Inheritance
# OOP Concept: Inheritance allows us to create new classes based on existing ones.
# What to Do: Create subclasses for specific account types (e.g., SavingsAccount).

class SavingsAccount(Account):
    def __init__(self, account_number, owner, initial_balance=0, interest_rate=0.02):
        super().__init__(account_number, owner, initial_balance)
        self._interest_rate = interest_rate

    # Overriding method to add interest
    def add_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        print(f"Interest added: {interest}. New balance: {self._balance}")

# STEP 3: Polymorphism
# OOP Concept: Polymorphism lets us use the same method name, but have different behavior in subclasses.
# What to Do: Override methods in subclasses as needed.

class CurrentAccount(Account):
    def withdraw(self, amount):
        # Current accounts allow overdraft up to 500
        overdraft_limit = 500
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self._balance - amount < -overdraft_limit:
            print("Overdraft limit exceeded.")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")

# STEP 4: Abstraction
# OOP Concept: Abstraction means defining a common interface for different account types.
# What to Do: Use an abstract base class or interface for core operations.

from abc import ABC, abstractmethod

class AbstractAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

# STEP 5: Association & Composition
# OOP Concept: Association/Composition means a Bank "has" many Accounts.
# What to Do: The Bank class manages multiple Account objects.

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}  # Dictionary to store accounts by account number

    def add_account(self, account):
        self.accounts[account._account_number] = account
        print(f"Account {account._account_number} added to bank.")

    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} removed from bank.")
        else:
            print("Account not found.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, from_acct_no, to_acct_no, amount):
        from_account = self.get_account(from_acct_no)
        to_account = self.get_account(to_acct_no)
        if from_account and to_account:
            if from_account.get_balance() >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Transferred {amount} from {from_acct_no} to {to_acct_no}")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("One or both accounts not found.")

# Example usage:
if __name__ == "__main__":
    # Create bank
    my_bank = Bank("MyBank")

    # Create accounts
    acc1 = SavingsAccount("SB1001", "Alice", 1000)
    acc2 = CurrentAccount("CA1002", "Bob", 500)

    # Add accounts to bank
    my_bank.add_account(acc1)
    my_bank.add_account(acc2)

    # Deposit and withdraw
    acc1.deposit(200)
    acc2.withdraw(700)  # Allowed up to overdraft

    # Add interest to savings
    acc1.add_interest()

    # Transfer funds
    my_bank.transfer("SB1001", "CA1002", 300)

    # Show account info
    print(acc1.get_account_info())
    print(acc2.get_account_info())