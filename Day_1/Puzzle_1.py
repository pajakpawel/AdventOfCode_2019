def calculate_fuel_required(modules_masses: list) -> int:
    fuel_required = 0

    for mass in modules_masses:
        fuel_required += (mass // 3) - 2

    return fuel_required


if __name__ == '__main__':
    calculate_fuel_required([10])
