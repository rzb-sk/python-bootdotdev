# Functions Quiz

def calculate_damage(opening_attack, core_damage, finishing_move):
    total = opening_attack + core_damage + finishing_move
    return total

def to_celsius(f):
    c = 5 / 9 * (f - 32)
    return c

damage1 = calculate_damage(10, 20, 30)
damage2 = calculate_damage(5, 10, 15)

temp1 = to_celsius(32)
temp2 = to_celsius(212)