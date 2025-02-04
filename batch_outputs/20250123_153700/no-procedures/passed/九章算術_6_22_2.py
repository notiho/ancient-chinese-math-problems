"""
今有一人一日矯矢五十，一人一日羽矢三十，一人一日筈矢十五。今令一人一日自矯、羽、筈，問︰成矢幾何？
荅曰： a矢 。
"""

"""
Suppose one person in one day can straighten (矯) 50 arrows, one person in one day can fletch (羽) 30 arrows, and one person in one day can attach nocks (筈) to 15 arrows.
Now, if one person in one day performs all three tasks (straightening, fletching, and nocking), how many arrows can they complete?

Answer: *a* arrows.
"""

# 矯矢 (straightening) rate per day
矯_rate = 50

# 羽矢 (fletching) rate per day
羽_rate = 30

# 筈矢 (nocking) rate per day
筈_rate = 15

# The total number of arrows completed in one day is limited by the slowest task
a = Fraction(1, Fraction(1, 矯_rate) + Fraction(1, 羽_rate) + Fraction(1, 筈_rate))  # Harmonic sum of rates

a
"""
"""
