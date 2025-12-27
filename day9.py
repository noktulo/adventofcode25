# Advent of Code 2025 DAY 9

type coordinates = tuple[int, int]


def calculate_rect(tile_a: coordinates, tile_b: coordinates) -> int:
    return abs(tile_a[0] - tile_b[0] + 1) * abs(tile_a[1] - tile_b[1] + 1)


def get_biggest_rect(red_tiles: list[coordinates]) -> int:
    biggest_rect: int = 0

    for index_a, tile_a in enumerate(red_tiles):
        for tile_b in red_tiles[index_a + 1 :]:
            rect_size: int = calculate_rect(tile_a, tile_b)
            biggest_rect: int = rect_size if rect_size > biggest_rect else biggest_rect
            # print(f"{tile_a} to {tile_b} is {rect_size}")

    return biggest_rect


if __name__ == "__main__":
    with open("day9input.txt", "r") as f:
        red_tiles: list[coordinates] = [
            tuple(list(map(int, line.rstrip().split(",")))) for line in f
        ]

    print(f"The largest rectangle is {get_biggest_rect(red_tiles)} units.")
