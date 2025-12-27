# Advent of Code 2025 DAY 9 PART 2

import shapely
from shapely import Polygon

type coordinates = tuple[int, int]


def get_biggest_rect(red_tiles: list[coordinates]) -> int:
    outer_boundary: Polygon = Polygon(red_tiles)

    biggest_rect: int = 0

    for index_a, tile_a in enumerate(red_tiles):
        for tile_b in red_tiles[index_a + 1 :]:
            this_rect: Polygon = Polygon(
                [
                    (tile_a[0], tile_a[1]),
                    (tile_a[0], tile_b[1]),
                    (tile_b[0], tile_b[1]),
                    (tile_b[0], tile_a[1]),
                ]
            )
            if shapely.area(shapely.difference(this_rect, outer_boundary)) < 1:
                this_rect_size: int = abs(tile_a[0] - tile_b[0] + 1) * abs(
                    tile_a[1] - tile_b[1] + 1
                )
                if this_rect_size > biggest_rect:
                    biggest_rect: int = this_rect_size
                    print(f"{str(tile_a):<15} -> {str(tile_b):<15} = {this_rect_size}")
                biggest_rect: int = (
                    this_rect_size if this_rect_size > biggest_rect else biggest_rect
                )
            # print(f"{tile_a} to {tile_b} is {rect_size}")

    return biggest_rect


if __name__ == "__main__":
    with open("day9input.txt", "r") as f:
        red_tiles: list[coordinates] = [
            tuple(list(map(int, line.rstrip().split(",")))) for line in f
        ]

    print(f"The largest rectangle is {get_biggest_rect(red_tiles)} units.")
