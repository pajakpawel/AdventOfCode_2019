def calculate_fuel_required(modules_masses: list) -> int:
    fuel_required = 0

    for mass in modules_masses:
        fuel_required += (mass // 3) - 2

    return fuel_required


if __name__ == '__main__':
    dataset = []
    with open("puzzle_input.txt") as puzzle_input:
        for number in puzzle_input.readlines():
            dataset.append(int(number))

    print("Solution for dataset included in './puzzle_input.txt' is equal to ", calculate_fuel_required(dataset))
