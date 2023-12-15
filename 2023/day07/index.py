import operator
from collections import Counter

# Second rule takes effect for decks with the same pull-type
# Sort by strength of first card pulled, then second card, then third,...
def sort_deck_strength_of_type(card_list):
    ''' CARD STRENGTHS (Weakest to Strongest)
        2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A ''' 
    new_card_list = []
    print(card_list)
    return new_card_list

# Multiply Rank (position in list+1) with bid amount of puzzle input
# Weakest Rank = 1, strongest rank = len(puzzleinput)
def calculate_bid_amount():
    pass

# ---------
# Creating the basis of the list to be worked on
input = open('test_input.txt', 'r')
lines = []
for l in input:
    lines.append(l.replace("\n", ""))

initInput = []
for line in lines:
    initInput.append(line.split(" "))
    
for cardID in range(len(initInput)):
    letterCount = dict(Counter(initInput[cardID][0]))
    initInput[cardID].append(letterCount)
# -----

# Detect settype and add to list
# Weakest to Strongest
error_list = []         # Debug
highCard_list = []      # ABCDE
onePair_list = []       # AABCD
twoPair_list = []       # AABBC
threeOfKinds_list = []  # AAABC
fullHouse_list = []     # AAABB
fourOfKinds_list = []   # AAAAB
fiveOfKinds_list = []   # AAAAA
for cardID in range(len(initInput)):
    # --- DIVIDE ALL TYPES OF LISTS ---
    # That way they can be sorted in "strength level" on their own in the second step
    # Grab the amounts a letter is mentioned which is necessary to determine the pull-type/hand-type
    amount_list = list(initInput[cardID][2].values())
    amount_list.sort(reverse = True)

    firstOccurance = amount_list[0]
    secondOccurance = amount_list[1]
    keyLength = len(amount_list)

    if keyLength == 5:                                                          # High card -> All 5 different
        highCard_list.append(initInput[cardID])
    elif firstOccurance == 2 and keyLength == 4:                                # One Pair -> 4 total, index 0: Two occurances
        onePair_list.append(initInput[cardID])
    elif firstOccurance == 2 and secondOccurance == 2 and keyLength == 3:       # Two Pair -> 3 total, index 0 and 1: Two occurances
        twoPair_list.append(initInput[cardID])
    elif firstOccurance == 3 and keyLength == 3:                                # Three of kinds -> 3 total, index 0: Three occurances
        threeOfKinds_list.append(initInput[cardID])
    elif firstOccurance == 3 and secondOccurance == 2 and keyLength == 2:       # Full House -> 2 total, index 0: 3 occurances, index 1: 2 occurances
        fullHouse_list.append(initInput[cardID])
    elif firstOccurance == 4 and keyLength == 2:                                # Four of kinds -> 2 total, index 0: 4 occurances
        fourOfKinds_list.append(initInput[cardID])
    elif firstOccurance == 5:                                                   # Five of kinds -> 1 total, index 0: 5 occurances
        fiveOfKinds_list.append(initInput[cardID])
    else:                                                                       # Error
        error_list.append(initInput[cardID])


# --- SORT EACH CARDTYPE BY VALUE
#highCard_list = sort_deck_strength_of_type(highCard_list)
#onePair_list = sort_deck_strength_of_type(onePair_list)
twoPair_list = sort_deck_strength_of_type(twoPair_list)
'''threeOfKinds_list = sort_deck_strength_of_type(threeOfKinds_list)
fullHouse_list = sort_deck_strength_of_type(fullHouse_list)
fourOfKinds_list = sort_deck_strength_of_type(fourOfKinds_list)
fiveOfKinds_list = sort_deck_strength_of_type(fiveOfKinds_list)'''