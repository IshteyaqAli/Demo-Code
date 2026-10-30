class Atm:

    # Functions VS Methods

# Constructor
    def __init__(self):

        self.__pin = ""  # Now it's partially privatised using "__(Double underscore)"
        self.__balance=0

        self.__menu()
        # to access private obj:

        def get_pin(self):
            return self.__pin

        def set_pin(self,new_pin):
            self.__pin = new_pin
            print("PIN Changed")

    def __menu(self):
        while True:
            user_input=input("""
                        Hello, how would you like to proceed?
                        1. Enter 1 to create your pin
                        2. Enter 2 to deposit
                        3. Enter 3 to withdraw
                        4. Enter 4 to check balance
                        5. ENter 5 to exit
""")
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Bye")
                break
            else:
                print("Invalid option")

    def create_pin(self):
        self.__pin=input("Enter your pin: ")
        print("Pin set successfully")

    def deposit(self):
        temp=input("Enter your pin: ")
        if temp==self.__pin:
            amount=int(input("Enter the amount: "))
            if amount > 0:
                self.__balance += amount
                print("Deposit successful")
            else:
                print("Amount must be positive")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp=input("Enter your pin: ")
        if temp==self.__pin:
            amount=int(input("Enter the amount: "))
            if amount<=self.__balance:
                self.__balance -= amount
                print("Operation Successful")
            else:
                print("Insufficient Funds")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp=input("Enter your pin: ")
        if temp==self.__pin:
            print(f"Your Account Balance : :{self.__balance}")
        else:
            print("Invalid pin")
    
sbi = Atm()
sbi.get_pin()