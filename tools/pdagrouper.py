
groups = {}
statelist = []

with open("pdatfonly.txt", 'r') as file:
    totalline = 0
    for line in file:
        parts = line.split(' ')
        parts[4] = parts[4].replace("\n","")
        state = parts[3]
        if state not in groups:
            groups[state] = []
            statelist.append(state)
        groups[state].append(line)
        totalline +=1
    print(totalline)

for i in range(len(statelist)):
    print(statelist[i])
# with open('pdagrouped.txt', 'w') as file:
#     for state, lines in groups.items():
#         for line in lines:
#             file.write(line)