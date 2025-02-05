"""
    1. Where to declare functions?
    2. As I learned that a variable needs to be declared before it's used.
    3. Code executes in order from TOP to BOTTOM, so a variable needs to be created before it can be used.
    4. That means if I define a function, I can't call that function until after the definition (def).

"""

"""
    Boo.dev assignment --> Debugging
"""

# main()


# def main():
#     print("Fantasy Quest is booting up...")
#     print("Game is running!")

# def should be before the main().
# definition should be before calling the function.
print("\n") # for some space at the top
      
def booting():
    print("Fantasy Quest is booting up....")
    print("Please be patient....")
    print("We appreciate your patience....")
    print("Welcome to Fantasy Quest! \nAre you read start your Quest? Glory & Fame awaits you!")

booting()


