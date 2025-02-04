"""
今有負籠重一石一十七斤，行七十六步，五十返。今負籠重一石，行百步，問︰返幾何？
荅曰： a返 。
"""

#----- content starts here -----
"""
Suppose there is a load weighing 1 shi and 17 jin, carried for 76 steps, with 50 trips made.
Now, with a load weighing 1 shi, carried for 100 steps, how many trips can be made?

Answer: *a* trips.
"""

# Convert weights to a consistent unit (jin)
# 1 shi = 120 jin
負籠重1 = 1 * 120 + 17  # 1 shi 17 jin
負籠重2 = 1 * 120       # 1 shi

# First case: total work done (weight × distance × trips)
總功1 = 負籠重1 * 76 * 50

# Second case: total work done (weight × distance × trips)
# Let the number of trips be "a"
總功2 = 負籠重2 * 100 * a

# Since total work is the same in both cases:
a = Fraction(總功1, 負籠重2 * 100)

# Result
a#----- content ends here -----

"""
Code error: name 'a' is not defined"""
