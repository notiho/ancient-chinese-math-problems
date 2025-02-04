"""
今有一人一日矯矢五十，一人一日羽矢三十，一人一日筈矢十五。今令一人一日自矯、羽、筈，問︰成矢幾何？
荅曰： a矢 。
"""

#----- content starts here -----
"""
Suppose one person in one day can straighten 50 arrows, another person in one day can fletch 30 arrows, and another person in one day can attach nocks to 15 arrows.
Now, if one person in one day does all three tasks (straightening, fletching, and attaching nocks), how many arrows can they complete?

Answer: *a* arrows.
"""

# 矯矢速度 (straightening speed): 50 arrows/day
矯矢 = 50

# 羽矢速度 (fletching speed): 30 arrows/day
羽矢 = 30

# 筈矢速度 (nocking speed): 15 arrows/day
筈矢 = 15

# The total number of arrows completed in one day is determined by the slowest task
a = Fraction(1, Fraction(1, 矯矢) + Fraction(1, 羽矢) + Fraction(1, 筈矢))#----- content ends here -----

"""
"""
