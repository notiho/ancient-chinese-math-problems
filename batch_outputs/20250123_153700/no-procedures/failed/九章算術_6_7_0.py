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

# 負籠重一石一十七斤
initial_weight = 1 * 120 + 17  # Convert to jin (1 shi = 120 jin)

# 行七十六步，五十返
initial_steps = 76
initial_trips = 50

# 負籠重一石
new_weight = 1 * 120  # Convert to jin

# 行百步
new_steps = 100

# The total work done is proportional to weight * steps * trips
# Calculate the total work for the initial case
initial_work = initial_weight * initial_steps * initial_trips

# Calculate the trips in the new case
# total_work = new_weight * new_steps * a
a = Fraction(initial_work, new_weight * new_steps)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 150000/2603, Actual: 2603/60"""
