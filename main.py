# Function to find mid-point of a range
def find_midpoint(lower_limit, upper_limit):
    num_range = upper_limit - lower_limit
    range_midpoint = num_range / 2
    return lower_limit + range_midpoint


name = str(input("Enter name: "))
print("Hello", name)
print("Let's guess your age in 7 steps!")
low_age = 1
high_age = 100
for i in range(7):
    mid_age = find_midpoint(low_age, high_age)
    a1 = str(input("Are you older than %s? Enter (Y/N): " % mid_age))
    if a1 == "Y" or a1 == "y":
        low_age = mid_age
    else:
        high_age = mid_age
print("My guess is you're %s years old." % round(find_midpoint(low_age, high_age)))