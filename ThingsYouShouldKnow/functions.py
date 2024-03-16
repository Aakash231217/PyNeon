def remaining_fuel(initial, kilometres, ratio):
    return initial-kilometres * ratio

initial = 50
kilometres = 10
ratio = 2 

print(remaining_fuel(initial, kilometres, ratio))