print("Enter last name")
lastname = input()
print("Enter score from game 1")
gamescore1 = float(input())
print("Enter score from game 2")
gamescore2 = float(input())
print("Enter score from game 3")
gamescore3 = float(input())
totalpoints = gamescore1 + gamescore2 + gamescore3
averagescore = totalpoints / 3
handicap = (200 - averagescore) * 0.9
handicapfinal = averagescore + handicap
print("Bowler's name:" + lastname)
print("Average score: " + str(averagescore))
print("Handicap: " + str(handicap))
print("Average score with handicap: " + str(handicapfinal))
