# 24 Days of Code: DAY 1

zeroes: int = 0
position: int = 50
output: str = ""


def turn_dial(inst):
    global position
    global zeroes
    global output

    match inst[0]:
        case "R":
            position += int(inst[1:])
        case "L":
            position -= int(inst[1:])

    if position > 0:
        position = position % 100
    elif position < 0:
        position = 100 - abs(position) % 100

    if position == 100 or position == -100:
        position = 0

    if position == 0:
        zeroes += 1
        output += f"{inst}: {position} - ZEROES {zeroes}\n"
    else:
        output += f"{inst}: {position}\n"


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
