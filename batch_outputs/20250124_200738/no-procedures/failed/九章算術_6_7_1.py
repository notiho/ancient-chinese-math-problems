"""
今有負籠重一石一十七斤，行七十六步，五十返。今負籠重一石，行百步，問︰返幾何？
荅曰： a返 。
"""

#----- content starts here -----
"""
Suppose there is a load weighing 1 shi and 17 jin. A person carries it for 76 steps and makes 50 trips.
Now, if the load weighs 1 shi and the person walks 100 steps, how many trips can they make?

Answer: *a* trips.
"""

# 負籠重一石一十七斤 (1 shi = 120 jin)
負籠重1 = 120 + 17  # in jin

# 行七十六步，五十返
步數1 = 76
返數1 = 50

# 負籠重一石
負籠重2 = 120  # in jin

# 行百步
步數2 = 100

# Calculate the total work done in the first case (weight * steps * trips)
總功1 = 負籠重1 * 步數1 * 返數1

# Calculate the number of trips in the second case (total work / (weight * steps))
a = Fraction(總功1, 負籠重2 * 步數2)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 150000/2603, Actual: 2603/60"""
