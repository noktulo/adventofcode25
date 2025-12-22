# 24 Days of Code: DAY 3


def max_joltage(battery_bank) -> int:
    batteries: list[int] = []
    index: int = 0

    for i in range(len(battery_bank)):
        batteries.append(int(battery_bank[index : index + 1]))
        index += 1

    num_batteries: int = len(battery_bank)
    joltage: int = 0

    for i in range(12):
        num_batteries = len(batteries)
        curr_digit = max(batteries[: num_batteries - 11 + i])
        batteries = batteries[batteries.index(curr_digit) + 1 :]
        if i != 11:
            joltage += curr_digit * 10 ** (11 - i)
        else:
            joltage += curr_digit

    return joltage


if __name__ == "__main__":
    total_joltage: int = 0

    with open("day3input.txt", "r") as f:
        battery_banks: list[str] = [line.rstrip() for line in f]

    for battery_bank in battery_banks:
        total_joltage += max_joltage(battery_bank)

    print(f"Total joltage: {total_joltage}")
