import sys, copy
p1 = """40
26
44
14
3
17
36
43
47
38
39
41
23
28
49
27
18
2
13
32
29
11
25
24
35""".split("\n")

p2 = """19
15
48
37
6
34
8
50
22
46
20
21
10
1
33
30
4
5
7
31
12
9
45
42
16""".split("\n")

#Normal
p1 = """9
2
6
3
1""".split("\n")

p2 = """5
8
4
7
10""".split("\n")


p1 = list(map(int, p1))
p2 = list(map(int, p2))

#--- Part 1
'''def game():
    while len(p1) != 0 and len(p2) != 0:
        cur1 = p1[0]
        cur2 = p2[0]

        if cur1 > cur2:
            p1.append(cur1)
            p1.append(cur2)
        else:
            p2.append(cur2)
            p2.append(cur1)

        p1.pop(0)
        p2.pop(0)

    if len(p1) == 0:
        winner = p2
    else:
        winner = p1

    return winner


winner = game()
ans = 0
for i in range(len(winner)):
    mult = len(winner)-i
    ans = ans + (winner[i] * mult)
    print(f"{winner[i]} * {mult}")
print(ans)'''


#------- Part 2

def round(p1, p2, r1, r2, gameNr, roundNr):
    while len(p1) != 0 and len(p2) != 0:
        if p1 in r1 or p2 in r2:
            return [], p2, "Player 1 - SameCards"
        else:
            curWinner = "#"
            roundNr += 1
            print(f"-- ROUND {roundNr} (Game {gameNr})--")

            #Save configuration of cards of this round
            r1.append(copy.deepcopy(p1))
            r2.append(copy.deepcopy(p2))

            cur1 = p1[0]
            cur2 = p2[0]

            print(f"Player 1's deck: {p1}")
            print(f"Player 2's deck: {p2}")
            print(f"Player 1 plays: {cur1}")
            print(f"Player 2 plays: {cur2}")

            if cur1 > cur2:
                print(f"Player 1 wins round {roundNr} of game {gameNr}!")
                p1.append(cur1)
                p1.append(cur2)
                curWinner = "P1"
            else:
                print(f"Player 2 wins round {roundNr} of game {gameNr}!")
                p2.append(cur2)
                p2.append(cur1)
                curWinner = "P2"

            p1.pop(0)
            p2.pop(0)

        #Win the entire game
        if len(p1) == 0 or len(p2) == 0:
            if len(p1) == 0:
                winner = "Player 2"
            else:
                winner = "Player 1"
            return p1, p2, winner
        #Start an entirely new game if the value of the pulled card is the same as the amount of cards of the deck
        elif len(p1) >= cur1 and len(p2) >= cur2:
            #Remove the last added card -> won't get used for the next round

            #CHECK POSITION -> needs to be checked before the change of the deck
            print(f"P1 deck: {p1}")
            print(f"Len(p1): {len(p1)}")
            print(f"Val p1: {cur1}")
            print(f"P2 deck: {p2}")
            print(f"Len(p2): {len(p2)}")
            print(f"Val p2: {cur2}")
            if curWinner == 'P1':
                tempP1 = p1[:-2]
            elif curWinner == 'P2':
                tempP2 = p2[:-2]
            #Limit amount of cards to value of the last pulled card, -1 to get no wrong offset. if cardvalue is 1, I have to grab cardindex 0
            tempP1 = copy.deepcopy(p1[:cur1])
            tempP2 = copy.deepcopy(p2[:cur2])
            
            maingame(tempP1, tempP2, gameNr)
        #Else: Just continue playing this round



def maingame(p1, p2, gameNr):
    print(f"=== GAME {gameNr} ===")
    gameNr += 1
    roundNr = 0

    r1 = []
    r2 = []
    while len(p1) != 0 and len(p2) != 0:
        p1, p2, winner = round(p1, p2, r1, r2, gameNr, roundNr)
    print(f"{winner} won Game {gameNr}")


gameNr = 0
maingame(p1, p2, gameNr)

