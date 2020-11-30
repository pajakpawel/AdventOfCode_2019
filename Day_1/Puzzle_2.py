def recursive_fuel_calculate(mass: int) -> int:
    fuel = (mass // 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + recursive_fuel_calculate(fuel)


def calculate_entire_fuel_required(modules_masses: list) -> int:
    entire_fuel_required = 0
    for mass in modules_masses:
        entire_fuel_required += recursive_fuel_calculate(mass)

    return entire_fuel_required


if __name__ == '__main__':
    dataset = []
    with open("puzzle_input.txt") as puzzle_input:
        for number in puzzle_input.readlines():
            dataset.append(int(number))

    print("Solution for dataset included in './puzzle_input.txt' is equal to ", calculate_entire_fuel_required(dataset))
