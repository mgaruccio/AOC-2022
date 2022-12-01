r = sorted(
    [
        sum([eval(y) for y in x.split("\n")])
        for x in open("./day1/inputs").read().split("\n\n")
    ],
    reverse=True,
)
print(f"{r[0]} - {sum(r[0:3])}")
