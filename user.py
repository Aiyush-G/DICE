from random import randint

class User:
    """ This is a user class and can be instantiated as many times as needed and is used in the dice calculations as explained in main.py, it allows:
    | Increase in score object
    | Calculates odd / even score 
    | Calculates if the role is a double
    | If the score object is 0
    | Calculate the overall score
    """
    score = 0
    messageRole = ""
    roled = False

    def __init__(self, username):
        """ Sets classes variables

        Args:
            username (string): allows the username to be accessed within __super__ so that it can be used in other methods.
        """
        self.username = username

    def increaseScore(self, by = 1):
        """Increases score and can be seen as an utility function

        Args:
            by (int, optional): amount to increase score by. Defaults to 1.
        """
        self.score += by
    
    
    def calcOddEven(self, roles):
        """If the score is odd then the score -= 5 otherwise += 10

        Args:
            roles ([type]): [description]
        """
        if (roles[0] + roles[1]) & 1: # bitwise
            self.score -= 5
        else:
            self.score += 10
    
    def calcDouble(self, roles):
        """If there is a double their individual calculations are done and then a third role is completed

        Args:
            roles (int): number on the role to check whether they are equal
        """
        if roles[0] == roles[1]:
            self.increaseScore(int(role(1)[0])) # 3rd role
    
    def checkZero(self):
        """Ensures that the score never goes below 0 by checking if it does and then returning it to 0
        """
        self.score = 0 if self.score < 0 else self.score
    
    def calcOverall(self, roles):
        """Utility function that runs all of the calculations

        Args:
            roles (tuple): contains both role values and can be indexed
        """
        self.calcOddEven(roles)
        self.calcDouble(roles)
        self.checkZero()


def role(num = 2):
    """This is the number of roles that should be performed, the only time when != 2 is when the two dice are the same and then a third role is completed.

    Args:
        num (int, optional): Defaults to 2.

    Returns:
        array: array (casted to a tuple in many cases) that contains the scores.
    """
    role = lambda: randint(1, 6)
    roles = lambda: [role() for x in range(0,num)]
    return roles() # array of roled numbers

if __name__ == "__main__":
    print ("You are running the wrong code, please run main.py")