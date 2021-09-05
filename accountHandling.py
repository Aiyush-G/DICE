import re
from colourIDLE import *

# Utilites
class authErr(Exception):
    pass

def get_users(file_name):
    line_fmt = re.compile(r'username: (.*) password: (.*)')
    with open(file_name) as f:
        return dict(line_fmt.match(line.strip()).groups() for line in f)

# Main
def loginOrRegister(users, file_name):
    lR = input("Login or Register: ").lower().replace(" ", "")
    usernameAfterlR = login(users) if lR=='login' else register(file_name)
    return usernameAfterlR

def register(file_name):
    # username: mike password: mikey << format
    username = input("Enter your username: ")
    password = input("Enter you password: ")

    if username in get_users(file_name):
        printc (red("Username has been taken already, please choose another one: "))
        register(file_name)
        return False
        
    elif username == password:
        printc (red("Password cannot be same as username!"))
        return False

    with open(file_name, 'a') as f:
        f.write("\n")
        f.write(f"username: {username} password: {password}")
        return username

def login(users, max_tries=3):
    print (users)
    for i in range(max_tries):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if (username in users) and (users[username] == password):
            print("You are logged in as:", username)
            return username
        else:
            print(f"Login failed. You have {max_tries - i - 1} tries left.")
    raise authErr(f"You have been locked out please restart to try again.")


if __name__ == "__main__":
    print ("You are running the wrong code, please run main.py")
    