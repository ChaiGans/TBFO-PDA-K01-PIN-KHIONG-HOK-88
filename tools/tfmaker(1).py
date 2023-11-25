def convert_to_delta(production):
    parts = production.split(' ')
    parts[4] = parts[4].replace("\n","").replace(",","")
    transitionfunction = "δ("+parts[0]+","+parts[1]+","+parts[2]+") = {("+parts[3]+", "+parts[4]+")}"
    return transitionfunction

with open("pdatfonly.txt", 'r') as file:
    linenumber = 1
    for line in file:
        if (line == "\n"):
            continue
        print(convert_to_delta(line))
        linenumber +=1