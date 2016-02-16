romeo = open("romeo", "r")
final = []
for line in romeo:
    newline = line.split()
    for i in newline:
        if i not in final:
            final.append(i)
final.sort()
print final
