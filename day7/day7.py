from json import dumps
import random
import string


def hash_gen():
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(10))


def get_input(input_file="./testinput"):
    with open(input_file) as f:
        return f.read().splitlines()


def parse_input(input):
    parsed_input = []
    for line in input:
        parsed_line = {}
        if line[0] == "$":
            parsed_line["type"] = "command"
        else:
            parsed_line["type"] = "output"

        if parsed_line["type"] == "command":
            parsed_line["command"] = line[2:4]
            if parsed_line["command"] == "cd":
                parsed_line["target"] = line[5:]

        if parsed_line["type"] == "output":
            if line[0:3] == "dir":
                parsed_line["item_type"] = "dir"
                parsed_line["dir_name"] = line[4:]
            else:
                parsed_line["item_type"] = "file"
                parsed_line["file_size"] = int(line[: line.index(" ")])
                parsed_line["file_name"] = line[line.index(" ") + 1 :]

        parsed_input.append(parsed_line)
    return parsed_input


def caclulate_dir_sizes(input):
    directories = {}
    level = 0
    for i, line in enumerate(input):
        start_level = 0
        level = 0
        if i == 1010:
            print(level)
        if line.get("command") == "cd" and line.get("target") != "..":
            dirhash = line["target"] + hash_gen()
            directories[dirhash] = 0
            # print(directories)

            for item in list(input[i + 1 :]):
                if item.get("command") == "cd" and item.get("target") != "..":
                    level += 1
                if item.get("command") == "cd" and item.get("target") == "..":
                    level -= 1

                if level < start_level:
                    break

                if item.get("file_size"):
                    directories[dirhash] += item["file_size"]

    return directories


def main():
    input = get_input("./input")
    parsed_input = parse_input(input)
    dir_sizes = caclulate_dir_sizes(parsed_input)
    print(dumps(dir_sizes, indent=2))
    print(sum(x for x in dir_sizes.values() if x <= 100000))
    total_size = 70000000
    required_space = 30000000
    current_unused = total_size - list(dir_sizes.values())[0]
    needed_space = required_space - current_unused
    print(sorted([x for x in dir_sizes.values() if x >= needed_space])[0])


if __name__ == "__main__":
    main()
