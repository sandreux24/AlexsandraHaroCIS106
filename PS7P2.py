def battingave(hits, turns):
    battingave = hits / turns
    percent = battingave * 100
    
    return battingave

# Main
print("Enter players name: ")
player = input()
print("Enter number of hits: ")
hits = float(input())
print("Enter times at bat: ")
turns = float(input())
battingave(hits, turns)
average = battingave(hits, turns)
percent = average * 100
print("Players name: " + player)
print("Batting average:& " + str(percent))
