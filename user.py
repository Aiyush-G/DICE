from random import randint

class User:
    score = 0
    messageRole = ""
    roled = False

    def __init__(self, username):
        self.username = username

    def increaseScore(self, by = 1):
        self.score += by
    
    
    def calcOddEven(self, roles):
        if (roles[0] + roles[1]) & 1: # bitwise
            self.score -= 5
        else:
            self.score += 10
    
    def calcDouble(self, roles):
        if roles[0] == roles[1]:
            self.increaseScore(int(role(1)[0]))
    
    def checkZero(self):
        self.score = 0 if self.score < 0 else self.score
    
    def calcOverall(self, roles):
        self.calcOddEven(roles)
        self.calcDouble(roles)
        self.checkZero()


def role(num = 2):
    role = lambda: randint(1, 6)
    roles = lambda: [role() for x in range(0,num)]
    return roles() # array of roled numbers

if __name__ == "__main__":
    print ("You are running the wrong code, please run main.py")