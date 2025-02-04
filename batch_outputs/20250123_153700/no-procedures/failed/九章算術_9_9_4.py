"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
荅曰： a丈 。
"""

"""
Suppose there is a door that opens outward, leaving a gap of 1 chi from the threshold, and does not close by 2 cun.
Question: how wide is the door?

Answer: the width of the door is *a* zhang.
"""

# 開門去閫一尺 (gap from the threshold)
gap_from_threshold = 1  # in chi

# 不合二寸 (does not close by 2 cun)
does_not_close = Fraction(2, 10)  # convert 2 cun to chi (1 chi = 10 cun)

# The total width of the door is the sum of the two
a = gap_from_threshold + does_not_close  # in chi

# Convert chi to zhang (1 zhang = 10 chi)
a = Fraction(a, 10)  # in zhang
"""
Variable 'a' has wrong value. Expected: 101/100, Actual: 3/25"""
