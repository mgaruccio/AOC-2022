import copy


def get_input(input_file="./testinput"):
    with open(input_file) as f:
        lines = f.read().splitlines()
    return [{"direction": x[0], "iterations": int(x[2:])} for x in lines]


def check_positions(h, t):
    hor = int(abs(h[0] - t[0]) > 1)
    ver = int(abs(h[1] - t[1]) > 1)
    if ver and not hor:
        hor = int(h[0] != t[0])
    if hor and not ver:
        ver = int(h[1] != t[1])
    if h[0] < t[0]:
        hor = hor * -1
    if h[1] < t[1]:
        ver = ver * -1
    return {"horizontal": hor, "vertical": ver}


def main():
    input = get_input("./input")
    positions = []

    vertical = ["U", "D"]
    horizontal = ["L", "R"]
    positive = ["R", "U"]
    negative = ["L", "D"]

    tail_knots = [[0, 0] for _ in range(9)]

    h = [0, 0]

    for move in input:
        print(move)
        for step in range(move["iterations"]):
            if move["direction"] in negative:
                i = -1
            else:
                i = 1
            if move["direction"] in horizontal:
                h[0] += i
            else:
                h[1] += i
            knot_ahead = h
            for knot in tail_knots:

                move_required = check_positions(knot_ahead, knot)
                knot[0] += move_required["horizontal"]
                knot[1] += move_required["vertical"]
                knot_ahead = knot
            positions.append((knot[0], knot[1]))

    print(len(set(positions)))


if __name__ == "__main__":
    main()
