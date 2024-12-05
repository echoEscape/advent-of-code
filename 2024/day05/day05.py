input = open('test_01.txt', 'r')
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

# Task 1
# Step 1. Filter
correctRules = []
incorrectRules = []
for pages in pagesList:                                                         # e.g. ['97', '13', '75', '29', '47']
  occurrences = []
  valid = True
  for page in pages:                                                            # e.g. '97'
    for rules in rulesList:                                                     # e.g. ['47', '29'] from 47|29 <- incorrect btw because 29 cannot come before 47
      if page == rules[0] and rules[1] in occurrences:                                                         
          valid = False

    if valid:
       occurrences.append(page)

  if set(pages) == set(occurrences):
      correctRules.append(pages)
  else:
     incorrectRules.append(pages)
   
solutionOne = 0
for rules in correctRules:
   middleIndex = len(rules) // 2
   solutionOne += int(rules[middleIndex])

print(incorrectRules)
        
        