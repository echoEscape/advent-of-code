'''
CARD STRENGTHS (strongest to weakest)
    A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2

RULE - Primary
    Five of a kind, where all five cards have the same label: AAAAA
    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    High card, where all cards' labels are distinct: 23456

RULE - Secondary
    If two hands have the same type, a second ordering rule takes effect. 
    Start by comparing the first card in each hand. If these cards are different, 
    the hand with the stronger first card is considered stronger. 
    If the first card in each hand have the same label, however, 
    then move on to considering the second card in each hand. 
    If they differ, the hand with the higher second card wins; otherwise, 
    continue with the third card in each hand, then the fourth, then the fifth.

RANK ORDERING
    This example shows five hands; each hand is followed by its bid amount. 
    Each hand wins an amount equal to its bid multiplied by its rank, 
    where the weakest hand gets rank 1, the second-weakest hand gets rank 2, 
    and so on up to the strongest hand. Because there are five hands in this example, 
    the strongest hand will have rank 5 and its bid will be multiplied by 5.
'''

input = open('test_input.txt', 'r')
lines = []
for l in input:
    lines.append(l.replace("\n", ""))

'''
Todo:
Overarching goal: Sort the inputlist by rank and cardcombinations
1. Rank the hands by sorting them from weakest (1) to highest (len(lines))
2. Build something to detect the kinds/pairs/full house/high card and sort them to the front (so that the cards without a cardcompination are already sorted and stay in the back)
3. go through new sorted input list and multiply by bid and rank
4. results
'''