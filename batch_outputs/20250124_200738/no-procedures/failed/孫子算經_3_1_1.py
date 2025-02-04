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

# 丁總數
丁總數 = 15000000

# 出兵數
出兵數 = 400000

# Calculate how many adult males are required for one soldier
每兵需丁 = Fraction(丁總數, 出兵數)

# Extract the integer part (a) and fractional part (b)
a = 每兵需丁.numerator // 每兵需丁.denominator
b = 每兵需丁 - a

# Final result
a, b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 5, Actual: 1/2"""
