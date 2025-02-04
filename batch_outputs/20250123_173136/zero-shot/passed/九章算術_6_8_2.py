"""
今有程傳委輸，空車日行七十里，重車日行五十里。今載太倉粟輸上林，五日三返。問︰太倉去上林幾何？
術曰：并空、重里數，以三返乘之，為法。令空、重相乘，又以五日乘之，為實。實如法得一里。
荅曰： a里 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
empty_distance_per_day = 70  # in li
loaded_distance_per_day = 50  # in li
round_trips = 3  # number of round trips in 5 days
total_days = 5  # total days

# Calculation
total_distance_per_day = empty_distance_per_day + loaded_distance_per_day  # combined empty and loaded distance per day
total_distance_all_trips = total_distance_per_day * round_trips  # total distance for 3 round trips
product_of_distances = empty_distance_per_day * loaded_distance_per_day  # product of empty and loaded distances
total_product = product_of_distances * total_days  # product over 5 days

# Distance from 太倉 to 上林
a = Fraction(total_product, total_distance_all_trips)  # distance in li

# Output the result
a


"""


The variable `a` will contain the distance from 太倉 (Taicang) to 上林 (Shanglin) in li.
"""


"""
"""
