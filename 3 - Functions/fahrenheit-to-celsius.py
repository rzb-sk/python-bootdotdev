# A function to change the temperature from Fahrenheit to Celsius

def to_celsius(f):
    celsius = 5 / 9 * (f - 32)
    return celsius

def test(f):
    c = round(to_celsius(f), 2)
    print(f"{f} degrees fahrenheit is {c} degrees celsius.")

print("\n")
test(100)
test(118)
test(80)
test(150)