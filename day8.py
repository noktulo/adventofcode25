# Advent of Code 2025 DAY 8

from numpy import sqrt

type coordinates = tuple[int, int, int]
type point_pair = tuple[int, int, float]


def calc_distances(input_points: list[coordinates]) -> list[point_pair]:
    point_pairs: list[point_pair] = []

    for start_point_index, start_point in enumerate(input_points):
        for end_point_index, end_point in enumerate(input_points):
            if end_point_index <= start_point_index:
                continue
            distance: float = sqrt(
                (start_point[0] - end_point[0]) ** 2
                + (start_point[1] - end_point[1]) ** 2
                + (start_point[2] - end_point[2]) ** 2
            )
            point_pairs.append((start_point_index, end_point_index, float(distance)))

    point_pairs.sort(key=lambda tup: tup[2])

    return point_pairs


def create_circuits(point_pairs: list[point_pair], pair_count: int) -> list[set[int]]:
    circuits: list[set[int]] = []

    # Create first circuit
    circuits.append({point_pairs[0][0], point_pairs[0][1]})

    # Create remaining circuits
    for pair in point_pairs[1:pair_count]:
        a_location: int = -1
        b_location: int = -1

        for circuit_index, circuit in enumerate(circuits):
            if pair[0] in circuit:
                a_location = circuit_index
            if pair[1] in circuit:
                b_location = circuit_index
            if a_location >= 0 and b_location >= 0:  # If both already found
                break

        # If neither exist, create new circuit
        if a_location < 0 and b_location < 0:
            circuits.append({pair[0], pair[1]})

        # If one exists, add other to same circuit
        elif b_location < 0:
            circuits[a_location].add(pair[1])
        elif a_location < 0:
            circuits[b_location].add(pair[0])

        # If both exist in separate circuits, combine circuits
        elif a_location != b_location:
            circuits[a_location] |= circuits[b_location]
            del circuits[b_location]

        # If both exist in same circuit, do nothing

    circuits.sort(key=lambda el: len(el), reverse=True)
    return circuits


def calc_answer(circuits: list[set[int]], num_circuits: int) -> str:
    output_string: str = ""
    mult_output: int = 1

    for index, circuit in enumerate(circuits[:num_circuits]):
        output_string += str(len(circuit))
        mult_output *= len(circuit)
        if index + 1 == num_circuits:
            output_string += f" = {mult_output}"
        else:
            output_string += " * "

    return output_string


if __name__ == "__main__":
    with open("day8input.txt", "r") as f:
        input_points: list[coordinates] = [
            tuple(list(map(int, line.rstrip().split(",")))) for line in f
        ]

    point_pairs: list[point_pair] = calc_distances(input_points)

    circuits: list[set[int]] = create_circuits(point_pairs, 1000)

    print(calc_answer(circuits, 3))
