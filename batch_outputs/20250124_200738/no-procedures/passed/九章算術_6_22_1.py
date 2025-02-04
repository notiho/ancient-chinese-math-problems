"""
今有一人一日矯矢五十，一人一日羽矢三十，一人一日筈矢十五。今令一人一日自矯、羽、筈，問︰成矢幾何？
荅曰： a矢 。
"""

#----- content starts here -----
"""
Suppose one person in one day can straighten 50 arrows, another person in one day can fletch 30 arrows, and another person in one day can notch 15 arrows.
Now, if one person in one day performs all three tasks (straightening, fletching, and notching), how many arrows can they complete?

Answer: *a* arrows.
"""

# 矯矢 (straightening) rate per day
矯矢 = 50

# 羽矢 (fletching) rate per day
羽矢 = 30

# 筈矢 (notching) rate per day
筈矢 = 15

# To find the total number of arrows completed in one day, we calculate the harmonic mean of the rates:
# The time required to complete one arrow for each task is the reciprocal of the rate.
# The total time to complete one arrow is the sum of these times.
# The total number of arrows completed in one day is the reciprocal of the total time.

a = Fraction(1, Fraction(1, 矯矢) + Fraction(1, 羽矢) + Fraction(1, 筈矢))

# The result `a` represents the number of arrows completed in one day by one person performing all three tasks.#----- content ends here -----

"""
"""
