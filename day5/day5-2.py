from queue import LifoQueue


def get_input(input_file="./testinput"):
    with open(input_file) as input_file:
        input = input_file.read()
    stacks = input.split("\n\n")[0].split("\n")
    instructions = input.split("\n\n")[1].split("\n")
    return {"stacks": stacks, "instructions": instructions}


class Stacks(object):
    def __init__(self, stack_drawing):
        self.stacks = self.parse_stacks(stack_drawing)

    def parse_stacks(self, stack_drawing):
        stack_drawing.pop()  # remove the numbers from the drawing, we don't need them
        stack_drawing.reverse()
        move = 4
        stacks = []  # start with an empty list to simplify things later
        i = 0
        while i <= len(stack_drawing[0]):
            stacks.append(LifoQueue())
            i += move

        for row in stack_drawing:
            position = 1
            i = 0
            while position <= len(row):
                if row[position] != " ":
                    stacks[i].put(row[position])
                position += move
                i += 1
        return stacks

    def parse_instruction(self, instruction):
        relevant_numbers = [int(x) for x in instruction.split() if x.isdigit()]
        return {
            "count": relevant_numbers[0],
            "source": relevant_numbers[1] - 1,
            "target": relevant_numbers[2] - 1,
        }

    def process_instructions(self, instructions):
        for instruction in instructions:
            instruction = self.parse_instruction(instruction)
            crane_stack = [
                self.stacks[instruction["source"]].get()
                for _ in range(instruction["count"])
            ]
            crane_stack.reverse()
            for item in crane_stack:
                self.stacks[instruction["target"]].put(item)

    def view_top_of_stacks(self):
        return "".join([stack.get() for stack in self.stacks])


def main():
    input = get_input("./input")
    stack_drawing = input["stacks"]
    instructions = input["instructions"]
    stacks = Stacks(stack_drawing)

    stacks.process_instructions(instructions)
    print(stacks.view_top_of_stacks())


if __name__ == "__main__":
    main()
