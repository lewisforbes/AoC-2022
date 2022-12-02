def score_of_yours(yours, possible="XYZ"):
    for i in range(len(possible)):
        if yours==possible[i]:
            return i+1
    raise Exception()

def find_winner(a_in, b_in):
    def translate(x):
        if x=="X":
            return "A"
        if x=="Y":
            return "B"
        if x=="Z":
            return "C"
        else:
            return x
    
    a = translate(a_in)
    b = translate(b_in)
    
    if a==b:
        return None
    
    if a=="A":
        if b=="B":
            return b_in
        else: # b=="C"
            return a_in
    if a=="B":
        if b=="C":
            return b_in
    return find_winner(b_in, a_in)

f = open("data.txt", "r")
score = 0
for line in f:
    theirs, yours = line.strip().split(" ")
    score += score_of_yours(yours)
    outcome = find_winner(theirs, yours)
    if outcome == theirs:
        score += 0
        continue
    if outcome == yours:
        score += 6
        continue
    if outcome == None:
        score += 3
        continue
    raise Exception

f.close()
print(score)

def score_to_add(theirs, goal):
    if goal=="Y":
        return score_of_yours(theirs, "ABC")+3

    win_loss = [["B", "A"], ["A", "C"], ["C", "B"]]
    if goal=="X":
        for pair in win_loss:
            if pair[0]==theirs:
                return score_of_yours(pair[1], "ABC") # +0
        raise Exception()
    if goal=="Z":
        for pair in win_loss:
            if pair[1]==theirs:
                return score_of_yours(pair[0], "ABC")+6
    raise Exception

f = open("data.txt", "r")
score = 0
for line in f:
    theirs, goal = line.strip().split(" ")
    score += score_to_add(theirs,goal)

print(score)
