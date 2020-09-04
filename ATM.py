print('welcome to the **** bank')
balance = 300000

def menu(): 
    print('*** Menu ***')
    print('\n1.Show Balance \n2.Cash Withdrawal \n3.Deposit \n4.Return Card \n5.Change Pin')

def show_balance():
    print('Your Current Balance is :', balance)

def make_withdrawl():
    balance = 30000
    withdrawal = int(input('Enter the amount : '))
    balance = balance - withdrawal
    print('yor current balance is',balance)

def deposit():
    balance = 15000
    deposit = int(input('Enter the amount : '))
    balance = balance + deposit
    print('Yor current balance is',balance)

def return_card():
    print('Thank you')
    exit()

def change_pin():
    new_pin = int(input("Enter your new 4 digit pin here : "))
    pin = new_pin
    print("Now your pin is",pin)

def choice():
    choice = int(input('Enter your Choice'))
    if choice == 1:
        show_balance()
    elif choice == 2:
        make_withdrawl()
    elif choice == 3:
        deposit()
    elif choice == 4:
        return_card()
    elif choice == 5:
        change_pin()
    else:
        print('Invalid Choice')

pin=int(input('Enter your 4 digit pin'))

if pin == 1111:
    menu()
    choice()
else:
    print("Invalid Pin!")
