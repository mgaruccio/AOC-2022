import string

rucksacks = [x.rstrip() for x in open("./input")]
priorites = sum(
    next(
        (
            string.ascii_letters.index(x) + 1
            for x in rucksack[: int((len(rucksack) / 2) + 1)]
            if x in rucksack[int((len(rucksack) / 2)) :]
        ),
        0,
    )
    for rucksack in rucksacks
)
print(priorites)
