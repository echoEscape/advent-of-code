input = open('input_01.txt', 'r')
lines = []
for l in input:
  lines.append(l.replace("\n", ""))

rules = lines[:lines.index("")]
pages = lines[lines.index("")+1:]

rulesList = []
for rule in rules:
  rulesList.append(rule.split("|"))

pagesList = []
for page in pages:
    pagesList.append(page.split(","))


def checkValidity(pages, rulesList):                                            # e.g. ['97', '13', '75', '29', '47'] and ['47', '29']
  occurrences = []
  valid = True
  for page in pages:                                                            # e.g. '97'
    for rules in rulesList:                                                     # e.g. ['47', '29'] from 47|29 <- incorrect btw because 29 cannot come before 47
      if page == rules[0] and rules[1] in occurrences:                                                         
          valid = False

    if valid:
      occurrences.append(page)

  if set(pages) == set(occurrences):
    return True, pages
  else:
    return False, pages
   

def sortOrderOfList(pages, rulesList):
  newOrder = []
  numDict = {}
  for page in pages:
    numDict[page] = 0

  for ID in numDict:
    for rule in rulesList:
      if rule[0] == ID and rule[1] in numDict.keys():
        numDict[ID] += 1

  # Sort desc (first page needs to appear the most, next one less than the first, etc.)
  numDict = dict(sorted(numDict.items(), key=lambda item: item[1], reverse=True))
  for ID in numDict:
    newOrder.append(ID)
  return newOrder


# Task 1
correctRules = []
incorrectRules = []
for pages in pagesList:
  result = checkValidity(pages, rulesList)

  if result[0] == True:
    correctRules.append(result[1])
  elif result[0] == False:
    incorrectRules.append(result[1])


# Task 2
newSortedList = []
for rules in incorrectRules:
  newSortedList.append(sortOrderOfList(rules, rulesList))


# Solution calculation
solutionOne = 0
for pages in correctRules:
  middleIndex = len(pages) // 2
  solutionOne += int(pages[middleIndex])
print(solutionOne)

solutionTwo = 0
for pages in newSortedList:
  middleIndex = len(pages) // 2
  solutionTwo += int(pages[middleIndex])
print(solutionTwo)

        
        