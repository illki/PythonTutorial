name_of_units = "hours"
calculation_to_units = 24 * 60


def days_to_units(num_of_days):
    condition_check = num_of_days > 0
    print(type(condition_check))

    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units}{name_of_units}"
    elif num_of_days == 0:
        return "вы ввели нулевое значение, введите целое положительно число"

    else:
        return "you entered a negative value, so no conversion for you"


user_input = input(f"Введите значение дней для перевода в {name_of_units}\n")
if user_input.isdigit():
    user_input_to_number = (int(user_input))
    calculated_value = days_to_units(user_input_to_number)
    print(calculated_value)

print(type(name_of_units))
