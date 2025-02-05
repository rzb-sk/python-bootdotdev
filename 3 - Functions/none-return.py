# When no return value is specified in a function, it will automatically return "None".
# For example, maybe a function that prints some text to the console, but doesn't explicitly return a value.

def my_func():
    print("I do nothing!")
    return None

my_func()

def my_func():
    print("I do nothing!")
    return

my_func()

def my_func():
    print("I do nothing!")

my_func()