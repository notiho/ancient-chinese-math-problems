"""
今有負籠重一石一十七斤，行七十六步，五十返。今負籠重一石，行百步，問︰返幾何？
荅曰： a返 。
"""

#----- content starts here -----
"""
Suppose there is a load weighing 1 shi and 17 jin, carried for 76 steps, with 50 trips (returns).
Now, if the load weighs 1 shi and is carried for 100 steps, how many trips (returns) can be made?

Answer: *a* trips.
"""

# Define the weights in jin (1 shi = 120 jin)
initial_weight = 1 * 120 + 17  # 1 shi 17 jin = 137 jin
new_weight = 1 * 120  # 1 shi = 120 jin

# Define the initial distance and trips
initial_steps = 76
initial_trips = 50

# Define the new distance
new_steps = 100

# Calculate the total work done in the initial case (work = weight * steps * trips)
initial_work = initial_weight * initial_steps * initial_trips

# Calculate the number of trips for the new case (trips = work / (weight * steps))
a = Fraction(initial_work, new_weight * new_steps)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 150000/2603, Actual: 2603/60"""
