# 24 Days of Code: DAY 3


def max_joltage(battery_bank):

    batteries = []
    index: int = 0

    for i in range(len(battery_bank)):
        batteries.append(int(battery_bank[index:index+1]))
        index += 1

    first_digit: int = max(batteries[:len(battery_bank)-1])
    first_digit_pos: int = batteries.index(first_digit)

    remaining_batteries = batteries[first_digit_pos+1:]

    second_digit: int = max(remaining_batteries)
    
    joltage: int = first_digit * 10 + second_digit

    print(joltage)
    return(joltage)

    

if __name__ == "__main__":

    total_joltage: int = 0

    with open('day3input.txt','r') as f:
        battery_banks = [line.rstrip() for line in f]

    for battery_bank in battery_banks:
        total_joltage += max_joltage(battery_bank)

    print(f'Total joltage: {total_joltage}')