"""
今有程傳委輸，空車日行七十里，重車日行五十里。今載太倉粟輸上林，五日三返。問︰太倉去上林幾何？
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a transport task. An empty cart travels 70 li per day, while a loaded cart travels 50 li per day.
Now, grain is being transported from Taicang to Shanglin, completing 3 round trips in 5 days.
Question: how far is Taicang from Shanglin?

Answer: *a* li.
"""

# Define the distances traveled per day
empty_cart_speed = 70  # li/day
loaded_cart_speed = 50  # li/day

# Total time for 3 round trips
total_days = 5

# Let the distance between Taicang and Shanglin be "a" li
# For one round trip, the cart travels:
# 2 * a li (one trip loaded and one trip empty)

# In 5 days, the cart completes 3 round trips, so it travels:
# 3 * (2 * a) = 6 * a li in total

# The total distance traveled in 5 days is the sum of the distances traveled loaded and empty:
# (time spent loaded * loaded_cart_speed) + (time spent empty * empty_cart_speed)

# Let t_loaded be the time spent traveling loaded, and t_empty be the time spent traveling empty.
# Since the cart spends equal time traveling loaded and empty for each round trip:
# t_loaded + t_empty = total_days
# t_loaded = t_empty = total_days / 2 = 5 / 2 days

# Total distance traveled:
total_distance = (total_days / 2) * loaded_cart_speed + (total_days / 2) * empty_cart_speed

# Set total_distance equal to 6 * a and solve for a:
a = Fraction(total_distance, 6)

# Result
a  # Distance between Taicang and Shanglin in li#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
