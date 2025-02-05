"""
    All functions must be defined before they can be used.
    There's a simple trick to avoid structuring python code hard because the order of the functions needs to be just right.
    Most Python developers solve this problem by defining all the functions in their programs first.
    Then they "call" an "entry point function last.
    Note:
        Conventionally this "entry point" function is usually called "main" to keep things simple and consistent.

"""

def main(health, armor):
    # health = 10
    # armor = 5
    add_armor(health, armor)

def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

def print_health(new_health):
    print(f"The player now has {new_health} health.")

# call entry point last
print("\n")
main(10, 5)
main(20, 10)