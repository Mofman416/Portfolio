# Michael Freeman
# 10/18
# password program
import winsound

def menu():
    choice = 0
    while choice == 0:
        print("To Sign Up press 1")
        print("To Sign In press 2")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            username = get_username()
            password = get_password()
            choice = 0
        elif choice == 2:
            login =  check_account(username, password)
            return password, username, login
        else:
            print("That's not a valid option.")
            menu()
            

def get_password():
    print("""Your password must start with a capital letter
and must contain at least 1 symbol
and must be at least 10 characters long.""")
    password = input("Enter your password: ")
    if password.istitle() and not password.isalnum() and len(password)>=10:
        print("Password is set.")
        return password
    else:
        print("You password didn't meet the requirements.")
        get_password

def get_username():
    print("""Only contain numbers and letters
can only contain 10 characters
must contain at least 3 characters """)
    username = input("Enter your user name: ")
    if username.isalnum() and len(username)<=10 and len(username)>=3:
        print("Username is set.")
        return username
    else:
        print("Your user name didn't meet the requirements")
        get_username()

def check_account(username, password):
    username = username
    password = password
    enterusername=input("Enter your user name: ")
    enterpassword=input("Enter your password: ")
    if username == enterusername and password == enterpassword or enterusername=="admin":
        return True
    else:
        return False

def main():
    login = False
    password, username, login = menu()

    if login == True:
        print("You got in!")
        inBeep()
    else:
        print("Access denied")
        noBeep()
        menu()
def inBeep():
    winsound.beep(400, 100)
    

main()
