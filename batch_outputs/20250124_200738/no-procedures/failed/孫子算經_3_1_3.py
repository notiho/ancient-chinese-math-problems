"""
今有丁一千五百萬，出兵四十萬。問：幾丁科一兵？
答曰： a 丁 b分 。
"""

#----- content starts here -----
"""
Suppose there are 15,000,000 adult males (丁), and 400,000 soldiers are to be conscripted.
Question: how many adult males are required to provide one soldier?

Answer: *a* adult males and *b* fractional parts.
"""

# Total adult males
total_ding = 15000000

# Total soldiers
total_soldiers = 400000

# Calculate how many adult males are required for one soldier
ratio = Fraction(total_ding, total_soldiers)

# Extract the integer part and fractional part
a = ratio.numerator // ratio.denominator  # Integer part
b = Fraction(ratio.numerator % ratio.denominator, ratio.denominator)  # Fractional part#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 5, Actual: 1/2"""
