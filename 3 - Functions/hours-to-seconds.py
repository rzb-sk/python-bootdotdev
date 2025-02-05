# Convert hours to seconds and return the result

def hrs_to_secs(hrs):
    total_secs = hrs * 60 * 60
    return total_secs

def test(hrs):
    secs = hrs_to_secs(hrs)
    print(f"{hrs} hours is {secs} seconds.")

print("\n")
test(10)
test(1)
test(25)
test(100)
test(33)