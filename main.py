import accountHandling as aH
import user
from typingEffect import printt
from time import sleep

file_name = "accountfile.txt"
registered_users = aH.get_users(file_name)
numRounds = 1
sleepDuration = 0.1
    
p1 = aH.loginOrRegister(registered_users, file_name) # returns username if successfull
p2 = aH.loginOrRegister(registered_users, file_name)
p1 = user.User(p1)
p2 = user.User(p2)

enterInput = lambda: input("Click Enter to Role >>> \n")
messageRole = lambda p: print(p1.messageRole) if p == "p1" else print(p2.messageRole)


def turn(sleepDuration):
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
    score_file = "scores.txt"

    result = lambda p: printt(f"{p1.username} won with score: {p1.score}") if p == "p1" else printt(f"{p2.username} won with score: {p2.score}")
    write = lambda p, f: f.write(f"{p1.username}-{p1.score},") if p == "p1" else f.write(f"{p2.username}-{p2.score},")
    scoreOut = lambda: print(topScores(score_file))

    def writeScore(p, score_file):
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
    for x in range(0, numRounds):
        turn(sleepDuration)
    
    winner()

if __name__ == "__main__":
    rounds()