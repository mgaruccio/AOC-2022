import io
from yaml import load
from math import prod
from collections import deque
import time

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class Monkey(object):
    def __init__(self, monkey_description, number, monkey_ops):
        self.monkey_number = number
        self.items = deque(
            int(x) for x in str(monkey_description["Starting items"]).split(", ")
        )
        self.fast_items = deque(
            [int(x) for _ in range(len(monkey_ops))]
            for x in str(monkey_description["Starting items"]).split(", ")
        )
        self.monkey_ops = monkey_ops
        self.initial = len(self.items)
        operations = monkey_description["Operation"].split(" = ")[1].split(" ")[1:]
        self.operations = {}
        self.operations["operator"] = operations[0]
        self.operations["value"] = (
            int(operations[1]) if operations[1] != "old" else "old"
        )
        # if self.operations["value"] == "old":
        #     self.operations["operator"] = "**"
        self.test = int(monkey_description["Test"].split(" ")[-1])
        ## intentionally inverted boolean values to accomodate modulo comparisons
        self.target_lookup = {
            False: int(monkey_description["If true"].split(" ")[-1]),
            True: int(monkey_description["If false"].split(" ")[-1]),
        }
        self.inspection_count = 0

    def vslow_inspect(self):
        if len(self.items) == 0:
            return False
        self.inspection_count += 1
        item = self.items.popleft()
        if self.operations["value"] == "old":
            value = int(item)
        else:
            value = int(self.operations["value"])
        # inspected_item = int(eval(str(item) + self.operation[0] + value))
        inspected_item = self.op_function(self.operations["operator"], item, value)
        return {
            "target": self.target_lookup[bool(inspected_item % self.test)],
            "item": inspected_item,
        }

    def slow_inspect(self):
        if len(self.items) == 0:
            return False
        self.inspection_count += 1
        item = self.items.popleft()
        # item.append(self.operations)
        processed_item = self.slow_process_item(item)
        # print(processed_item)
        target = self.target_lookup[bool(processed_item % self.test)]
        # print(item)

        return {
            "target": target,
            "item": processed_item,
        }

    def slow_process_item(self, item):
        if type(item) == list:
            item = item[0]
        if self.operations["value"] == "old":
            value = int(item)
        else:
            value = int(self.operations["value"])
        return self.op_function(self.operations["operator"], item, value)

    def inspect(self):
        if len(self.fast_items) == 0:
            return False
        self.inspection_count += 1
        item = self.fast_items.popleft()
        for i, op in enumerate(self.monkey_ops):
            item[i] = self.process_item(item[i], op) % op
        # item.append(self.operations)

        # print(processed_item)
        processed_item = item[self.monkey_number]
        target = self.target_lookup[bool(processed_item)]
        # print(item)
        return {
            "target": target,
            "item": item,
        }

    def process_item(self, item, mod):
        if self.operations["value"] == "old":
            value = int(item)
        else:
            value = int(self.operations["value"])
        return self.op_function(self.operations["operator"], item, value % mod)

    def op_function(self, op, a, b):
        # ops = {"+": operator.add, "*": operator.mul}
        # func = ops[op]
        # return func(a, b)
        if op == "*":
            return a * b
        if op == "**":
            a * a
        return a + b


def get_input(input_file="./input"):
    input = open(input_file).read().splitlines()
    f = io.StringIO("", newline="\n")
    for line in input:
        if "If" in line:
            f.write(line[2:])
        else:
            f.write(line)
        f.write("\n")
    f.seek(0)
    return load(f, Loader=Loader)


def sort_function(x):
    return x.inspection_count


def main():
    input_values = get_input("./input")
    monkeys = [
        Monkey(
            monkey, i, [int(x["Test"].split(" ")[-1]) for x in input_values.values()]
        )
        for i, monkey in enumerate(input_values.values())
    ]

    for i in range(10000):
        print(f"round = {i}")
        for monkey in monkeys:
            item = monkey.inspect()
            while item:
                # monkeys[item["target"]].items.append(item["item"])
                monkeys[item["target"]].fast_items.append(item["item"])
                item = monkey.inspect()
        # print("INSPECTIONS")
        for i, monkey in enumerate(monkeys):
            print(f"Monkey {i} - {monkey.inspection_count}")
        # if not i % 1000:
        #     print(f"round - {i}")
        #     for i, monkey in enumerate(monkeys):
        #         print(f"Monkey {i} - {monkey.inspection_count}")
        #     print("")
        # print("")
        # print(f"mod time - {total_mod_time}")
        # print(f"mul time - {total_mul_time}")

    # for i, monkey in enumerate(monkeys):
    #     print(f"Monkey {i} - {monkey.inspection_count}")

    monkeys.sort(key=sort_function, reverse=True)
    print(prod([x.inspection_count for x in monkeys[:2]]))


if __name__ == "__main__":
    main()
