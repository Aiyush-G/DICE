import accountHandling as aH
import user
from typingEffect import printt
from time import sleep

file_name = "accountfile.txt"
registered_users = aH.get_users(file_name)
numRounds = 5
sleepDuration = 0.1

    
p1 = aH.loginOrRegister(registered_users, file_name) # returns username if successfull
p2 = aH.loginOrRegister(registered_users, file_name)
p1 = user.User(p1)
p2 = user.User(p2)

enterInput = lambda: input("Click Enter to Role >>> \n")
messageRole = lambda p: print(p1.messageRole) if p == "p1" else print(p2.messageRole)


def turn(sleepDuration):
    """ A single turn function that uses the user object to role 2 random numbers, calculate its' meaning following:
    | if total is even score += 10
    | if total is odd score -= 5
    | if role1 = role2 you can role3
    | score !< 0 at any time

    Args:
        sleepDuration (int): the amount of time between each message displayed on screen.
    """
    p1.roled = user.role()
    p2.roled = user.role()

    p1.calcOverall(p1.roled)
    p2.calcOverall(p2.roled)

    p1.messageRole = f"{p1.username} has rolled: {str(p1.roled)[1:-1]}"
    p2.messageRole = f"{p2.username} has rolled: {str(p2.roled)[1:-1]}"

    messageScore = f"That means {p1.username} has a score of {p1.score} whilst {p2.username} has a score of {p2.score} \n"

    enterInput()
    messageRole("p1")
    sleep(sleepDuration)
    enterInput()
    messageRole("p2 \n")
    sleep(sleepDuration)
    print (messageScore)
    sleep(sleepDuration)

def topScores(score_file):
    """ Opens the score_file with all of the games ever recorded and orders them in terms of their numerical score against the players name and ranks the top scorer ever.

    Args:
        score_file (string): path to txt file where scores should be stored.

    Returns:
        fString: a message with the top scorer and their name
    """
    scores = []

    with open(score_file, 'r') as file:
        data = file.read().replace('\n', '').split(",")
    
    for entry in data:
        score = "".join(filter(str.isdigit, entry))
        scores.append(score)
    index = scores.index(max(scores))
    person = str(data[index]).split("-")[0]
    return f"The top score ever was {scores[index]} by {person}"
    
def winner():
    """ Evaluates the players overall score stored in scores.txt (should be pre-written) and then runs the winner function depending upon who won alongside a message (see result lambda & write lambda)

    """
    score_file = "scores.txt"

    result = lambda p: printt(f"{p1.username} won with score: {p1.score}") if p == "p1" else printt(f"{p2.username} won with score: {p2.score}")
    write = lambda p, f: f.write(f"{p1.username}-{p1.score},") if p == "p1" else f.write(f"{p2.username}-{p2.score},")
    scoreOut = lambda: print(topScores(score_file))

    def writeScore(p, score_file):
        """Writes the score of both players to a file which could be accessed in a later game with the players top scores if they had one of the highscores.

        Args:
            p (User Object): the player object, could be player 1 or 2 in this scenario.
            score_file (string): path to where the score should be written to, this file should already exist.
        """
        with open(score_file, 'a') as f:
            write(p, f)

    if p1.score > p2.score:
        result("p1")
        writeScore("p1", score_file)
        scoreOut()
        return
    elif p1.score == p2.score:
        turn(sleepDuration)
        winner()
        return
    else:
        result("p2")
        writeScore("p2", score_file)
        scoreOut()
        return
        
    

def rounds():
    """A procedural way of running numRounds amount of rounds this avoids hardcoding in a specific number of itterations for the code to loop through.
    """
    for x in range(0, numRounds):
        turn(sleepDuration)
    
    winner()

if __name__ == "__main__":
    rounds()