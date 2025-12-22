# Advent of Code 2025 DAY 4

import numpy as np


# Turn list of strings into array
def make_array(warehouse_aisles: list[str]):
    bool_aisles: list[list[bool]] = []

    for warehouse_aisle in warehouse_aisles:
        bool_aisle: list[bool] = list(map(lambda x: x == "@", warehouse_aisle))
        bool_aisles.append(bool_aisle)

    return np.array(bool_aisles)


# Check if paper is movable
def move_roll(roll_location):
    warehouse_slice = warehouse_array[
        max(0, roll_location[0] - 1) : roll_location[0] + 2,
        max(0, roll_location[1] - 1) : roll_location[1] + 2,
    ]

    moved: bool = np.count_nonzero(warehouse_slice) < 5

    return moved


if __name__ == "__main__":
    moved_rolls: int = 0
    roll_count: int = 0

    with open("day4input.txt", "r") as f:
        warehouse_aisles: list[str] = [line.rstrip() for line in f]

    warehouse_array = make_array(warehouse_aisles)

    roll_locations = np.argwhere(warehouse_array).tolist()
    roll_count: int = len(roll_locations)
    last_roll_count: int = 0

    while True:
        for roll_location in roll_locations:
            if move_roll(roll_location):
                warehouse_array[roll_location[0], roll_location[1]] = False
                moved_rolls += 1

        roll_locations = np.argwhere(warehouse_array).tolist()
        roll_count = len(roll_locations)
        if roll_count == last_roll_count:
            break
        last_roll_count = roll_count

    print(f"Total rolls moved: {moved_rolls}")
