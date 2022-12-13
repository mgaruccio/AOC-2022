from collections import deque


def get_input(input_file="./input"):
    operation_cycle_lookup = {"addx": 2, "noop": 1}
    with open(input_file) as f:
        lines = f.read().splitlines()
    return deque(
        {
            "command": line[:4],
            "value": int(line[5:]) if len(line) > 5 else None,
            "cycles": 1 if line[:4] == "noop" else 2,
        }
        for line in lines
    )


def main():
    input = get_input("./testinput")
    total_cycle_count = 1
    x = 1
    operation = input.popleft()
    important_cycle_values = []
    relevance_counter = 19
    row_counter = 0
    while len(input) > 0:
        sprite_distance = abs(row_counter - x)
        if abs(row_counter - x) <= 1:
            print("#", end="")
        else:
            print(".", end="")
        if row_counter == 39:
            print("\n")
            row_counter = 0
        if relevance_counter == 0:
            important_cycle_values.append(x * total_cycle_count)
            relevance_counter = 40

        operation["cycles"] -= 1
        total_cycle_count += 1
        relevance_counter -= 1
        row_counter += 1
        if operation["cycles"] == 0:
            if operation["command"] == "addx":
                x += operation["value"]
            operation = input.popleft()

    print(sum(important_cycle_values))


if __name__ == "__main__":
    main()
