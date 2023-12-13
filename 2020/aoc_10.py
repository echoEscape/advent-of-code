rawData = [int(num) for num in """
114
51
122
26
121
90
20
113
8
138
57
44
135
76
134
15
21
119
52
118
107
99
73
72
106
41
129
83
19
66
132
56
32
79
27
115
112
58
102
64
50
2
39
3
77
85
103
140
28
133
78
34
13
61
25
35
89
40
7
24
33
96
108
71
11
128
92
111
55
80
91
31
70
101
14
18
12
4
84
125
120
100
65
86
93
67
139
1
47
38""".split()]

rawData.append(0)
rawData.sort()
rawData.append(max(rawData)+3)

diffOne = 0
diffThree = 0
diffOneArr = []
diffThreeArr = []
for testNum in rawData:
    if testNum+1 in rawData:
        diffOne += 1
        diffOneArr.append(testNum+1)
    elif testNum+3 in rawData:
        diffThree += 1
        diffThreeArr.append(testNum+3)

'''print(diffOneArr)
print(len(diffOneArr))
print("---")
print(diffThreeArr)
print(len(diffThreeArr))
print("---")
print(len(diffOneArr) + len(diffThreeArr))
print(len(rawData))'''
print(len(diffOneArr) * len(diffThreeArr))

#Recursive function
#Figuring out which next number is valid (creates a branch)
#from that branch you step one further and figure out the next valid paths
#f = open("recusionTest.txt", "w")

#numList = rawData
#counter = 0
#Just one Branch
'''for current in range(len(numList)):                # Current -> "startpoint"/limiter
    for next in range(current+1, len(numList)):       #+1 to "look ahead"
        if numList[next] - numList[current] <= 3:     #e.g. 3-1 = 2 -> Valid path
            counter += 1'''


visited = {} #Memorization of a certain branchpoint/depth -> Allows us to skip the path "to" that point by just continuing from there
#allBranches -> zeigt auf wie viele weitere routen von einem bestimmten punkt (currentBranch) möglich sind
def allBranches(currentBranch):
    if currentBranch == len(rawData)-1:                 #Wenn man am Ende angekommen ist, ist nurnoch eine Möglichkeit übrig, also +1
        return 1

    if currentBranch in visited:                          #STOP IT FROM LOOPING EVEN MORE BY NOT ALLOWING IT TO GET TO THE FOR LOOP BELOW
        return visited[currentBranch]                     #Return the answer I've previously gotten already

    counter = 0
    for n in range(currentBranch+1, len(rawData)):       #+1 to "look ahead", immer zu einem weiteren Pfad gucken, aber nur solange die Differenz <= 3 ist
        if rawData[n] - rawData[currentBranch] <= 3:     #e.g. 3-1 = 2 -> Valid path
            #counter += 1
            counter += allBranches(n)                    #RECURSION POINT -> if visited the if above will run and just return the same as before, a dict will override that entry, the next one in n (for loop) will then find a new path
    
    visited[currentBranch] = counter                       #CurrentBranch -> Depth, counter -> Wie viele weiteren Branches liegen darunter?
    return counter                                       #Collaps all counters together and returns the full on

    '''for i in range(len(rawData)):
        if i+1 in rawData:
            counter += 1
            allBranches(i+1, counter)
        if i+2 in rawData:
            counter += 1
            allBranches(i+2, counter)
        if i+3 in rawData:
            counter += 1
            allBranches(i+3, counter)
    f.write(counter)'''

#f.close()
print(allBranches(0))
print(visited)