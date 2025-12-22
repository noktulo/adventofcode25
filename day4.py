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
def check_movable(roll_location):
    warehouse_slice = warehouse_array[
        max(0, roll_location[0] - 1) : roll_location[0] + 2,
        max(0, roll_location[1] - 1) : roll_location[1] + 2,
    ]

    print(warehouse_slice)

    is_movable: bool = np.count_nonzero(warehouse_slice) < 5
    print(f"{np.count_nonzero(warehouse_slice)}: {is_movable}")
    return is_movable


if __name__ == "__main__":
    movable_rolls: int = 0

    with open("day4input.txt", "r") as f:
        warehouse_aisles: list[str] = [line.rstrip() for line in f]

    warehouse_array = make_array(warehouse_aisles)
    movable_array = warehouse_array

    roll_locations = np.argwhere(warehouse_array).tolist()

    for roll_location in roll_locations:
        print(roll_location)
        if check_movable(roll_location):
            movable_rolls += 1

    print(movable_rolls)
