def get_input(input_file="./testinput"):
    with open(input_file) as f:
        return f.read().splitlines()


def create_grid(input):
    return [[int(y) for y in list(x)] for x in input]


def check_visibility(grid):
    visible_trees = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            tree = grid[x][y]
            if x == 0 or y == 0 or x == len(grid[0]) - 1 or y == len(grid) - 1:
                visible_trees += 1
                continue
            if all(tree > grid[x][i] for i in range(0, y)):
                visible_trees += 1
                continue
            if all(tree > grid[x][i] for i in range(y + 1, len(grid))):
                visible_trees += 1
                continue
            if all(tree > grid[i][y] for i in range(0, x)):
                visible_trees += 1
                continue
            if all(tree > grid[i][y] for i in range(x + 1, len(grid))):
                visible_trees += 1
                continue

    return visible_trees


def find_best_tree(grid):
    scores = []
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            tree = grid[x][y]
            left = 0
            right = 0
            down = 0
            up = 0
            # x = 3
            # y = 2
            # tree = grid[x][y]
            for z in reversed([grid[x][i] for i in range(0, y)]):
                if tree > z:
                    left += 1
                else:
                    left += 1
                    break
            for z in [grid[x][i] for i in range(y + 1, len(grid))]:
                if tree > z:
                    right += 1
                else:
                    right += 1
                    break
            for z in reversed([grid[i][y] for i in range(0, x)]):
                if tree > z:
                    up += 1
                else:
                    up += 1
                    break
            for z in [grid[i][y] for i in range(x + 1, len(grid))]:
                if tree > z:
                    down += 1
                else:
                    down += 1
                    break
            scores.append(left * right * down * up)

    return max(scores)


def main():
    input = get_input("./input")
    grid = create_grid(input)
    print(f"phase 1 - {check_visibility(grid)}")
    print(f"phase 2 - {find_best_tree(grid)}")


if __name__ == "__main__":
    main()
