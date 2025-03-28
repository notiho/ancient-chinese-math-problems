"""
今有一人一日矯矢五十，一人一日羽矢三十，一人一日筈矢十五。今令一人一日自矯、羽、筈，問︰成矢幾何？
荅曰： a矢 。
"""

"""
Suppose one person in one day can straighten 50 arrows, another person in one day can fletch 30 arrows, and another person in one day can attach nocks to 15 arrows.
Now, if one person in one day does all three tasks (straightening, fletching, and nocking), how many arrows can they complete?

Answer: *a* arrows.
"""

# 矯矢 (straightening) rate per day
矯矢_rate = 50

# 羽矢 (fletching) rate per day
羽矢_rate = 30

# 筈矢 (nocking) rate per day
筈矢_rate = 15

# To determine how many arrows can be completed in one day, we take the reciprocal of the total time required for all three tasks
a = Fraction(1, Fraction(1, 矯矢_rate) + Fraction(1, 羽矢_rate) + Fraction(1, 筈矢_rate))
"""
"""
