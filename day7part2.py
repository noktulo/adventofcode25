# Advent of Code 2025 DAY 7 PART 2
import time


def count_realities(manifold_rows: list[list[str]]) -> int:
    beam_emitter: int = manifold_rows[0].index("S")
    paths_taken: int = 0

    # Create initial path to iterate from
    current_path: str = ""
    beam_location: int = beam_emitter

    for index, row in enumerate(manifold_rows):
        if index % 2 == 0:
            if row[beam_location] == "^":
                current_path += "L"
                beam_location -= 1

    last_path: str = current_path
    paths_taken += 1

    # Iterate from previous path
    while True:
        # If the all right path has been taken, all paths have been traced
        if "L" not in last_path:
            break

        beam_location: int = beam_emitter

        last_left: int = last_path.rfind("L")
        current_path: str = last_path[:last_left] + "R"

        for index, row in enumerate(manifold_rows):
            if index % 2 == 0:
                i: int = int(index / 2)
                if i < len(current_path):
                    if current_path[i] == "L":
                        beam_location -= 1
                    else:
                        beam_location += 1
                else:
                    if row[beam_location] == "^":
                        current_path += "L"
                        beam_location -= 1
        last_path = current_path
        paths_taken += 1

        if paths_taken % 1000000 == 0:
            now = time.time()
            timedelta = now - start
            hours, remainder = divmod(timedelta, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"{format(paths_taken, ',d')} realities so far")
            print(
                f"{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds so far"
            )
            print(
                f"First right in row {current_path.find('R')} of {int(len(manifold_rows) / 2)}\n"
            )

    return format(paths_taken, ",d")


if __name__ == "__main__":
    start = time.time()
    with open("day7input.txt", "r") as f:
        manifold_rows: list[list[str]] = [list(line.rstrip()) for line in f]

    print(f"{count_realities(manifold_rows)} realities")
    end = time.time()
    timedelta = end - start
    hours, remainder = divmod(timedelta, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(
        f"{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds to calculate"
    )
