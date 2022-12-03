import string

rucksacks = [x.rstrip() for x in open("./input")]
print(
    sum(
        next(
            next(
                string.ascii_letters.index(x) + 1
                for x in rucksack
                # if x in group[0] and x in group[1] and x in group[2]
                if all(x in item for item in group)
            )
            for rucksack in group
        )
        for group in [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]
    )
)
