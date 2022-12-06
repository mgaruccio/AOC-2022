with open("./input") as f:
    datastream = f.read()


pos = 14

while len(set(datastream[pos - 4 : pos])) < 4:
    pos += 1


print(pos)


pos = 14

while len(set(datastream[pos - 14 : pos])) < 14:
    pos += 1


print(pos)
