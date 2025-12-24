# Advent of Code DAY 6 PART 2

import numpy as np

input_list: list[list[str]] = []
grouped_operands: list[list[int]] = []
operators: list[str] = []
running_total: int = 0


def get_grouped_operands(input_list: list[list[str]]) -> list[list[int]]:
    input_array = np.array(input_list, np.str_)
    input_array = np.transpose(input_array)
    raw_operands: list[str] = []
    for row in input_array:
        raw_operands.append("".join(row))
    grouped_operands: list[list[int]] = []
    working_group: list[int] = []
    for row in raw_operands:
        if "".join(row).strip().isdigit():
            working_group.append(int(row))
        elif not "".join(row).isdigit() and len(working_group) > 0:
            grouped_operands.append(working_group)
            working_group: list[int] = []
    return grouped_operands


def run_operations(grouped_operands: list[list[int]], operators: list[str]) -> int:
    grand_total: int = 0
    for index, operand_group in enumerate(grouped_operands):
        if operators[index] == "+":
            for operand in operand_group:
                grand_total += operand
        elif operators[index] == "*":
            subtotal: int = 1
            for operand in operand_group:
                subtotal *= operand
            grand_total += subtotal
    return grand_total


if __name__ == "__main__":
    with open("day6input.txt", "r") as f:
        for line in f:
            line_array: list[str] = line.split()
            if line_array[0].isdigit():
                input_list.append(list(line))
            else:
                operators: list[str] = line_array

        grouped_operands: list[list[int]] = get_grouped_operands(input_list)

    print(run_operations(grouped_operands, operators))
