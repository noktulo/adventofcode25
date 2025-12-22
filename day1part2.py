# 24 Days of Code: DAY 1

import math

zeroes: int = 0
position: int = 50
output: str = ""


def turn_dial(inst):
    global position
    global zeroes
    global output

    start_position: int = position

    ## OLD_POSITION CAN NEVER BE NEGATIVE!!

    # Deal with full rotations

    rotations = math.floor(int(inst[1:]) / 100)
    remainder = int(inst[1:]) - rotations * 100

    zeroes += rotations

    # Deal with remaining turn

    match inst[0]:
        case "R":
            position += remainder
        case "L":
            position -= remainder

    if position == 100 or position == -100:
        position = 0

    elif position > 99:
        position -= 100
        if start_position != 0:
            zeroes += 1

    elif position < -100:
        position = 200 - position
        if start_position != 0:
            zeroes += 1

    elif position < 0:
        position = 100 + position
        if start_position > 0:
            zeroes += 1

    if position == 0 and start_position != 0:
        zeroes += 1

    output += f"{inst:>4}: {position:<4} - ZEROES {zeroes}\n"


# Runtime

if __name__ == "__main__":
    # Import instructions from file
    with open("day1input.txt", "r") as f:
        instructions = [line.rstrip() for line in f]

    for instruction in instructions:
        turn_dial(instruction)

    output = f"Total Zeroes: {zeroes}\n" + output

    with open("day1output.txt", "w") as f:
        f.write(output)
