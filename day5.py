# Advent of Code 2025 DAY 5

fresh_ingredients: int = 0
check_ranges: list[list[int]] = []
check_numbers: list[int] = []
output_buffer: str = ""


def check_in_range(check_number: int, check_ranges: list[list[int]]):
    global fresh_ingredients
    global output_buffer
    for check_range in check_ranges:
        if check_number < check_range[0]:
            output_buffer += f"{check_number:<18}Bad \n"
            continue
        elif check_number <= check_range[1]:
            fresh_ingredients += 1
            output_buffer += f"{check_number:<18}Fresh {fresh_ingredients} \n"
            break


if __name__ == "__main__":
    with open("day5input.txt", "r") as f:
        for line in f:
            if line.find("-") >= 0:
                split_range: list[int] = list(map(lambda x: int(x), line.split("-")))
                check_ranges.append(split_range)
            elif len(line.rstrip()) > 0:
                check_numbers.append(int(line.rstrip()))

    for check_number in check_numbers:
        check_in_range(check_number, check_ranges)

    with open("day5output.txt", "w") as f:
        f.write(output_buffer)

    print(f"{fresh_ingredients} fresh ingredients out of {len(check_numbers)}")
