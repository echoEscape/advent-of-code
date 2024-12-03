import re

input = open('input_01.txt', 'r')
lines = []
for l in input:
  lines.append(l)

def filter_one(lines):
  tempList = []
  for line in lines:
    tempList.extend(re.findall(r"mul\(\d{1,3},\d{1,3}\)", line))
  return tempList

def filter_two(lines):
  tempList = []
  for line in lines:
    tempEntry = re.findall(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))", line)
    # This is ugly and we all know it and I know I should learn list comprehensions
    for command in tempEntry:
      for ele in command:
        if ele:
          tempList.append(ele)
  return tempList

def clean_mul(lines):
  tempList = []
  for line in lines:
    if line.startswith("mul("):
      tempList.append(line.replace('mul(', '').replace(')', '').split(','))
    else:
      tempList.append(line)
  return tempList

def calc_one(cleanLines):
  solution = 0
  for command in cleanLines:
    solution = solution + (int(command[0]) * int(command[1]))
  return solution

def calc_two(cleanLines):
  solution = 0
  calc = True

  for line in cleanLines:
    if calc and len(line) == 2:
      solution = solution + (int(line[0]) * int(line[1]))
    else:
      if line == "do()":
        calc = True
      elif line == "don't()":
        calc = False
  return solution


mulList = filter_one(lines)
cleanMulList = clean_mul(mulList)
solutionOne = calc_one(cleanMulList)
print(solutionOne)

commandList = filter_two(lines)
cleanCommandList = clean_mul(commandList)
solutionTwo = calc_two(cleanCommandList)
print(solutionTwo)