# 24 Days of Code: DAY 2

invalid_total: int = 0


def find_invalid(selected_range: str):
    global invalid_total

    # Split array into start and end values
    range_bounds = selected_range.split("-")

    for i in range(int(range_bounds[0]), int(range_bounds[1]) + 1):
        digits = len(str(i))

        if digits % 2 != 0:  # If there are an odd number of digits
            continue

        half = int(digits / 2)

        if str(i)[:half] == str(i)[half:]:
            invalid_total += i


# RUNTIME

if __name__ == "__main__":
    with open("day2input.txt", "r") as f:
        ranges = f.read().split(",")

    for selected_range in ranges:
        find_invalid(selected_range)

    print(invalid_total)
