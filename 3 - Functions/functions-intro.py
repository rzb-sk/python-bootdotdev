# Functions allow us to reuse and organize code.
# for example,
radius = 5
area = 3.14 * radius * radius
print(area)

# To calculate for a single area of a single circle is okay.
# what if we wanted to calculate the area of thousands of circles??
# that's why using a function will help. We will just reuse that function.

# we can define a new function called "area_of_circle" using the def keyword:
def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result

# r = parameter or argument
# return - returns a single value i.e. the output of the function.
# In this case, it's the value stored in the "result" variable.

# To call this function
area = area_of_circle(5)
print(area)

area = area_of_circle(6)
print(area)

area = area_of_circle(7)
print(area)

"""
Boot.dev assignment
"""

sword_length = 1.0
spear_length = 2.0

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters.")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters.")