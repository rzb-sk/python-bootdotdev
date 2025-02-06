# Multiple Return Values
# A function can return more than one value by separating them with commas.

# Example
def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana

# receiving multiple values
# When calling a function that returns multiple values, you can assign them to multiple variables

dmg, mana = cast_iceblast(5, 100)
print("\n")
print(f"Damage: {dmg}, Remaining Mana: {mana}")

# The 'damage' and 'new_mana' variables from cast_iceblast function body only exist inside of the function.


"""
    Boot.Dev Assignment:
        Complete the 'become_warrior' function.
"""

def become_warrior(full_name, power):
    title = f"{full_name}, the warrior"
    new_power = power + 1
    return title, new_power

name, power = become_warrior("Frodo", 5)
print(f"{name} has a power level of: {power}")
