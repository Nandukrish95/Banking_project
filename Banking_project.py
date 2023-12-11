users = {101: {'name': "nandu", "a/c no": 1002, 'balance': 10000, 'idn': 101, 'age': 25, 'psw': 'nan98'},
         102: {'name': "kiran", "a/c no": 1003, 'balance': 15000, 'age': 22, 'psw': 'kr68', 'idn': 102}}
print("Welcome to Online banking")


def login():
    while True:
        global id
        global psw
        if id in users and psw == users[id]['psw']:
            print(f"Login successful, Welcome {users[id]['name']}, your balance is {users[id]['balance']}")
            break
        else:
            print('Invalid id or password!')
            id = int(input('Enter your id: '))
            psw = input('Enter your password: ')


def user_creation():
    name = input("Enter your name: ")
    psw = input("Enter a password: ")
    age = int(input('Enter your age: '))
    global id
    global ac_no
    id = (list((users.keys()))[-1]) + 1
    ac_no = (users[(list((users.keys()))[-1])]['a/c no']) + 1
    dict = {id: {'name': name, "a/c no": ac_no, 'balance': 0, 'age': age, 'idn': id}}
    users.update(dict)
    print(f"Account created, Welcome {users[id]['name']}, Your balance is {users[id]['balance']}")


def deposit(amount):
    users[id]['balance'] = users[id]['balance'] + amount
    print(f"Deposit successful, Your currrent balance is {users[id]['balance']}")


def withdraw(amount):
    if users[id]['balance'] > amount:
        users[id]['balance'] = users[id]['balance'] - amount
        print(f"Withdraw successful, Your currrent balance is {users[id]['balance']}")
    elif amount > users[id]['balance']:
        print(f"Insufficient balance, Your balance is {users[id]['balance']}")


def ac_details():
    print(f"name:{users[id]['name']}\nid:{users[id]['idn']}\na/c no:{users[id]['a/c no']}\nbalance:{users[id]['balance']}")


user_input = int(input("Press 1 to Login or Press 2 to create account: "))
if user_input == 1:
    id = int(input('Enter your id: '))
    psw = input('Enter your password: ')
    login()
elif user_input == 2:
    user_creation()

print("Choose any option")
while True:
    print("Press 1 to Deposit\nPress 2 to Withdraw\nPress 3 to show a/c details\nPress 4 to log out")
    user_option = int(input("Enter your option: "))
    if user_option == 1:
        amount = float(input("Enter the amount to deposit: "))
        deposit(amount)
    elif user_option == 2:
        amount = float(input("Enter the amount to withdraw: "))
        withdraw(amount)
    elif user_option == 3:
        ac_details()
    elif user_option == 4:
        print("logged out\nThank you")
        break
    else:
        print("invalid Input!")