input = open('input.txt', 'r')
lines = []
cleaned_lines_pt1 = []
cleaned_lines_pt2 = []
results_pt1 = []
results_pt2 = []
solution_pt1 = 0
solution_pt2 = 0

#Split Lines of Input into its own array and remove "New line" tag
for l in input:
    lines.append(l.replace("\n", ""))

def remove_characters(line):
    letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for letter in letter_list:
        line = line.replace(letter, "")
    return line

def convert_spelling_to_number(line):
    numbername_list = ["one", "1"],["two", "2"], ["three", "3"], ["four", "4"], ["five", "5"], ["six", "6"], ["seven", "7"], ["eight", "8"], ["nine", "9"]
    for spelledNumber in numbername_list:
        line = line.replace(spelledNumber[0], spelledNumber[0]+spelledNumber[1]+spelledNumber[0]) #fixes the twone issue so that two can still be detected even though one gets checked first by re-adding the actual string so that it doesnt get removed
    line = remove_characters(line)
    return line


for line in lines:
    cleaned_lines_pt1.append(remove_characters(line))
    cleaned_lines_pt2.append(convert_spelling_to_number(line))

#Part 1
for number_pt1 in cleaned_lines_pt1:
    results_pt1.append(int(number_pt1 + number_pt1)) if len(number_pt1) == 1 else results_pt1.append(int(number_pt1[0] + number_pt1[-1]))
for result_pt1 in results_pt1:
    solution_pt1 += result_pt1

#Part 2
for number_pt2 in cleaned_lines_pt2:
    results_pt2.append(int(number_pt2 + number_pt2)) if len(number_pt2) == 1 else results_pt2.append(int(number_pt2[0] + number_pt2[-1]))
for result_pt2 in results_pt2:
    solution_pt2 += result_pt2

print(solution_pt1)
print(solution_pt2)
