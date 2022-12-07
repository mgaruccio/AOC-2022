# got convinced to give this one a shot after complaining that the day6 challenge was too easy
from collections import deque
import time
import sys


def get_input(filepath):
    with open(filepath) as f:
        return [int(x) for x in f.read().split(",")]


def main():
    start = time.perf_counter()
    initial_seed = get_input("./input2021")
    l = [0 for _ in range(0, 9)]
    for i in initial_seed:
        l[i] += 1

    lantern_fish = deque(l)

    for i in range(256):
        x = lantern_fish.popleft()
        lantern_fish.append(x)
        lantern_fish[6] += x

    print(sum(lantern_fish))
    end = time.perf_counter()
    size = sys.getsizeof(lantern_fish)
    print(f"solves in {end - start:0.4f} seconds")
    print(f"uses {size} bytes for calculation")


if __name__ == "__main__":
    main()
