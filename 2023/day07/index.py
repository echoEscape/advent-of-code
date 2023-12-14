# All five cards have the same label: 
# AAAAA
def check_five_of_kind():
    pass

# Four cards have the same label and one card has a different label: 
# AA8AA
def check_four_of_kind():
    pass
# Three cards have the same label, and the remaining two cards share a different label: 
# 23332

def check_full_house():
    pass

# Three cards have the same label, and the remaining two cards are each different from any other card in the hand: 
# TTT98
def check_three_of_kind():
    pass

# Two cards share one label, two other cards share a second label, and the remaining card has a third label: 
# 23432
def check_two_pair():
    pass

# Two cards share one label, and the other three cards have a different label from the pair and each other: 
# A23A4
def check_one_pair():
    pass

# All cards' labels are distinct: 
# 23456
def check_high_card():
    pass

# Second rule takes effect when decks have the same type
# Sort by strength of first card pulled, then second card, then third,...
def sort_deck_strength_of_type():
    ''' CARD STRENGTHS (strongest to weakest)
        A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2 ''' 
    pass

# Multiply Rank (position in list+1) with bid amount of puzzle input
# Weakest Rank = 1, strongest rank = len(puzzleinput)
def calculate_bid_amount():
    pass

# ---------

input = open('test_input.txt', 'r')
lines = []
for l in input:
    lines.append(l.replace("\n", ""))

print(lines)


'''
Todo:
Overarching goal: Sort the inputlist by rank and Cardcombinations/Pull-type
1. Build something to detect the kinds/pairs/full house/high card and sort them to the front (so that the cards without a cardcompination are already sorted and stay in the back)
2. Rank the hands by sorting them from weakest (1) to highest (len(lines)) based on pull-type
3. Go through new sorted input list and multiply by bid and rank
4. results
'''