# Advent of Code 2025 DAY 7 PART 2
import time


def count_realities(manifold_rows: list[list[str]]) -> int:
    paths_taken: int = 0
    manifold_rows.append(["."] * 141)  # Add final row to receive final counts

    # Create dictionaries for each node
    nodes: list[list[dict(int, bool)]] = []
    for row_num, row in enumerate(manifold_rows):
        if row_num % 2 == 0 or row_num == len(manifold_rows):
            curr_row: list[dict(int, bool)] = []
            for node in row:
                is_splitter: bool = True if node == "^" else False
                input: int = 1 if node == "S" else 0
                curr_row.append(dict(input=input, splitter=is_splitter))
            nodes.append(curr_row)

    # Iterate through all nodes
    for row_num, row in enumerate(nodes):
        if row_num + 1 == len(nodes):
            break
        for col_num, node in enumerate(row):
            if node["input"] == 0:
                continue
            if node["splitter"]:
                nodes[row_num + 1][col_num - 1]["input"] += node["input"]
                nodes[row_num + 1][col_num + 1]["input"] += node["input"]
            else:
                nodes[row_num + 1][col_num]["input"] += node["input"]

    # Sum final row
    for node in nodes[-1]:
        paths_taken += node["input"]

    return format(paths_taken, ",d")


if __name__ == "__main__":
    start = time.perf_counter()
    with open("day7input.txt", "r") as f:
        manifold_rows: list[list[str]] = [list(line.rstrip()) for line in f]

    print(f"{count_realities(manifold_rows)} realities")
    end = time.perf_counter()

    print(f"{end - start} seconds to calculate")
