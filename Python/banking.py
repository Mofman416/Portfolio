class Bank_acc(object):
    def __init__(self):
        self.name=""
        self.balance=0
        self.pin = 1234
        self.inrate = 0.06
        self.acc_num = 123456789
    def credit_acc(self):
        ammount = float(input("Enter your deposit. "))
        self.balance+=ammount
    def debit_acc(self):
        get_pin = int(input("What is your pin? "))
        if get_pin != self.pin:
            print("That's not correct. Hear that police siren?\nIt's for you")
        else:
            ammount = float(input("Enter your deposit. "))
            self.balance-=ammount

mike_acc = Bank_acc()
mike_acc.name = "Mike"
print(mike_acc)
mike_acc.credit_acc()
print(mike_acc.balance)
mike_acc.debit_acc()
print(mike_acc.balance)