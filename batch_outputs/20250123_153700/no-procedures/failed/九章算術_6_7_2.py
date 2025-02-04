"""
今有負籠重一石一十七斤，行七十六步，五十返。今負籠重一石，行百步，問︰返幾何？
荅曰： a返 。
"""

"""
Suppose there is a load weighing 1 shi and 17 jin. A person walks 76 steps and makes 50 trips (returns).
Now, with a load weighing 1 shi, the person walks 100 steps. 
Question: how many trips (returns) can they make?

Answer: *a* trips.
"""

# Define the weights and distances
initial_weight = 1 * 120 + 17  # 1 shi = 120 jin, so 1 shi 17 jin = 120 + 17 jin
initial_steps = 76
initial_trips = 50

new_weight = 1 * 120  # 1 shi = 120 jin
new_steps = 100

# Calculate the total work done in the initial case (weight * steps * trips)
initial_work = initial_weight * initial_steps * initial_trips

# Calculate the number of trips in the new case (work = weight * steps * trips)
a = Fraction(initial_work, new_weight * new_steps)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 150000/2603, Actual: 2603/60"""
