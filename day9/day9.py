import copy


def get_input(input_file="./testinput"):
    with open(input_file) as f:
        lines = f.read().splitlines()
    return [{"direction": x[0], "iterations": int(x[2:])} for x in lines]


def build_graph(x, y):
    return [["." for _ in range(x)] for _ in range(y)]


def draw_graph(h, t, graph):
    # tgraph = copy.deepcopy(graph)
    for i, y in enumerate(graph):
        for k, x in enumerate(graph[i]):
            if x == "H":
                graph[i][k] = "."
            if x == "T":
                graph[i][k] = "#"
    graph[t[1] + 5][t[0] + 10] = "T"
    graph[h[1] + 5][h[0] + 10] = "H"

    return graph


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

    h = [0, 0]
    t = [0, 0]

    graph = build_graph(20, 20)

    for idx, move in enumerate(input):
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
            move_required = check_positions(h, t)
            t[0] += move_required["horizontal"]
            t[1] += move_required["vertical"]
            positions.append((t[0], t[1]))
            print(f"{h} - {t}")
            # tgraph = draw_graph(h, t, graph)
            # [print(x) for x in tgraph]
            print("")
        print(len(set(positions)))

        print("")

    print(len(set(positions)))


if __name__ == "__main__":
    main()
