# Advent of Code DAY 6 PART 2

numbers_array: list[list[str]] = []
operators: list[str] = []
running_total: int = 0


if __name__ == "__main__":
    with open("day6input.txt", "r") as f:
        for line in f:
            line_array: list[str] = line.split()
            if line_array[0].isdigit():
                numbers_array.append(list(map(lambda x: int(x), line_array)))
            else:
                operators: list[str] = line_array

    for i in range(len(operators)):
        operands: list[int] = list(map(lambda x: x[i], numbers_array))
        if operators[i] == "+":
            subtotal: int = 0
            for j in range(len(numbers_array)):
                subtotal += operands[j]
        elif operators[i] == "*":
            subtotal: int = 1
            for j in range(len(numbers_array)):
                subtotal *= operands[j]

        running_total += subtotal

    print(running_total)
