# Functions can have multiple parameters. parameters = input.
# for example, a "subtract" function that accepts 2 parameters -- a & b.
def subtract(a, b):
    result = a - b
    return result

# The name of a parameter doesn't matter when it comes to which values will be assigned to which parameter.
# It's "position" that matters.

result = subtract(5, 3)
print(result)

print(subtract(5, 3))

# An example with four parameters:
def create_introduction(name, age, height, weight):
    first_part = f"Your name is {name} and you are {age} years old."
    second_part = f"You are {height} meters tall and weigh {weight} kgs."
    full_intro = f"{first_part} {second_part}"
    return full_intro

# call the function
my_name = "Riyaz"
my_age = 30
my_height = 1.8
my_weight = 70

intro = create_introduction(my_name, my_age, my_height, my_weight)
print(intro)


"""
Boot.dev assignment
"""

# defining a triple_attack function

def triple_attack(damage_one, damage_two, damage_three):
    total = damage_one + damage_two + damage_three
    return total

# calling the function

attack_one = 2
attack_two = 4
attack_three = 3
first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

print(f"Getting damage for {attack_one}, {attack_two}, and {attack_three}...")
print(f"{first_triple_attack_damage} points of damage dealt!")
print("=====================================")

attack_four = -1
attack_five = 10
attack_six = 5
second_triple_attack_damage = triple_attack(attack_four, attack_five, attack_six)

print(f"Getting damage for {attack_four}, {attack_five}, and {attack_six}...")
print(f"{second_triple_attack_damage} points of damage dealt!")
print("=====================================")
