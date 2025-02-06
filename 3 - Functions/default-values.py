"""
    1. In Python, I can specify a default value for a function argument.
    2. I as the function definer cn specify a specific default value in case the caller doesn't provide one.
    3. The default value is created by using the assignment (=) operator in the function signature.
"""

def get_greeting(email, name="there"):
    print(f"Hello {name}, Welcome! You've been registered your email: {email}")

get_greeting("lane@example.com", "Lane") # name parameter is value is provided
get_greeting("lane@example.com") # name parameter is absent.


"""
    Boot.Dev Assignment
"""
def get_punched(health, armor=0):
    damage = 50 - armor
    new_health = health - damage
    return new_health


def get_slashed(health, armor=0):
    damage = 100 - armor
    new_health = health - damage
    return new_health


# Don't touch below this line


def test(health, armor):
    print(f"Running tests for health {health} and armor {armor}")
    print("========================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("----------------------------------------\n")


test(400, 5)
test(300, 3)
test(200, 1)
