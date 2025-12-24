# Advent of Code 2025 DAY 7


def calculate_beams(manifold_rows: list[list[str]]) -> int:
    beam_locations: set[int] = set()
    split_count: int = 0

    for index, row in enumerate(manifold_rows):
        if index == 0:
            beam_locations.add(row.index("S"))
            print("".join(row))
        elif index % 2 == 0:
            new_beam_locations: set[int] = set()
            for beam_location in beam_locations:
                if row[beam_location] == "^":
                    new_beam_locations.add(beam_location - 1)
                    new_beam_locations.add(beam_location + 1)
                    split_count += 1
                else:
                    new_beam_locations.add(beam_location)
            beam_locations = new_beam_locations
            print("".join(row))
        else:
            print_cache: list[str] = row
            for beam_location in beam_locations:
                print_cache[beam_location] = "|"
            print("".join(print_cache))

    return split_count


if __name__ == "__main__":
    with open("day7input.txt", "r") as f:
        manifold_rows: list[list[str]] = [list(line.rstrip()) for line in f]

    print(f"{calculate_beams(manifold_rows)} splits")
