"""
    'print()' is a function that:
        1. Prints a value to a console
        2. Does not return a value
    
    'return' is a keyword that:
        1. Ends the current function's execution
        2. Provides a value (or values) back to the caller of the function
        3. Does not print anything to the console, unless the return value is later printed.
"""

"""
    Printing values and running the code is a great way to debug the code.
    I can see what values are stores in various variables, find the mistakes and fix them.
    Add print statements and run the code as you go.
    In the real world it's rare to leave print() statements in the code when I'm done debugging.
"""

"""
    Boot.dev assignment
"""

# A function to get a title
def get_title(first_name, last_name, job):
    title = f"{first_name} {last_name}, the {job}."
    return title

# testing the function if it's working correctly
def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")
    print(f"Job: {job}")
    print(f"Title: {title}")
    print("=================================================")

# giving some test inputs
test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")