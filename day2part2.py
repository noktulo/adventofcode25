# 24 Days of Code: DAY 2 PART 2

invalid_total: int = 0


def split_number(number, chunk_length):
    chunks = []
    index = 0

    for i in range(int(len(str(number)) / chunk_length)):
        chunks.append(str(number)[index : index + chunk_length])
        index += chunk_length

    return chunks


def find_invalid(selected_range: str):
    global invalid_total

    # Split array into start and end values
    range_bounds = selected_range.split("-")

    # Iterate through each number in the range
    for i in range(int(range_bounds[0]), int(range_bounds[1]) + 1):
        digits = len(str(i))

        for j in range(
            1, int(digits / 2 + 1)
        ):  # For each length of substring up to half of the full string
            if digits % j != 0:  # If substring can't repeat perfectly
                continue

            chunks = split_number(i, j)  # Create list of equal-length chunks

            if chunks.count(chunks[0]) == len(
                chunks
            ):  # Check if all chunks are the same
                invalid_total += i
                break  # Stop processing this number if it's a repeater


# RUNTIME

if __name__ == "__main__":
    with open("day2input.txt", "r") as f:
        ranges = f.read().split(",")

    for selected_range in ranges:
        find_invalid(selected_range)

    print(invalid_total)
