input = open('input.txt', 'r')
lines = []
for l in input:
    lines.append(l.replace("\n", ""))

#[['Time', ['value', 'value', 'value']], ['Distance', ['value', 'value', 'value']]]
lines[0] = lines[0].split(":")
lines[1] = lines[1].split(":")
lines[0][1] = lines[0][1].strip().split("     ")
lines[1][1] = lines[1][1].strip().split("   ")

