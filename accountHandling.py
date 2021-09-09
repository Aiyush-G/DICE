import re
from colourIDLE import *

# Utilites
class authErr(Exception):
    """This is for a custom auth error, ie when the name is not valid etc... instead of throwing a generic exception by using a custom class the error is given more description."

    Args:
        Exception (none): ...
    """
    pass

def get_users(file_name):
    """The users in file_name are read into a dictionary that strips out the spaces and keeps there usernames and passwords.

    Args:
        file_name (string): this is the file where are all of the users are stored and allows all of the usernames and passwords to be indexed easily.

    Returns:
        dict: this dictionary contains key value pairs where the usernmae and passwords can be retreived.
    """
    line_fmt = re.compile(r'username: (.*) password: (.*)')
    with open(file_name) as f:
        return dict(line_fmt.match(line.strip()).groups() for line in f)

# Main
def loginOrRegister(users, file_name):
    """ This runs right at the start of the control flow and takes th euserinput which then allows the user to decide whether they want to register a new account which then calls register() function within the class or just continues with the default login process.

    Args:
        users (dict): a dictionary of key value pairs containing the username and passwords.
        file_name (string)): this is a file path to the list of users, this could be used with something like the get_users() function.

    Returns:
        expression: this can be evaulated in the main control flow and returns a function: login() or register() depending upon the input.
    """
    lR = input("Login or Register: ").lower().replace(" ", "")
    usernameAfterlR = login(users) if lR=='login' else register(file_name)
    return usernameAfterlR

def register(file_name):
    """Creates a new user with a username and passwords
    | Must be unique
    | Password != Username
    This is then written to file_name

    Args:
        file_name (string): path to a file where the new username and password should be stored, this can then be indexed at a later date.

    Returns:
        [bool, string]: the bool is used to break out of the control flow if a condition is not met, otherwise the user is instantly logged in so that they don't need to type their username and password again which could become tedious, this makes the code procedural and confines to the spec.
    """
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
    """ This indexes the users dictionary that could have been created in the get_users() method of the class, it also has itterates over the question multiple times incase the user gets their username and password wrong multiple times in a row.

    Args:
        users (dict): contains key value pairs of the usernames and passwords of the users.
        max_tries (int, optional): This is how many times the loop should continue if the user keeps getting their usernmae wrong multiple times. Defaults to 3.

    Raises:
        authErr: this is the class that is described at the top of accountHandling.py, it is a custom error so provides a more specific exception to the user.

    Returns:
        string: this is passsed to the main control flow so the program can register which user has been logged in successfully, this is only passed when the username && password are correct, otherwise the authErr is raised.
    """
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
    