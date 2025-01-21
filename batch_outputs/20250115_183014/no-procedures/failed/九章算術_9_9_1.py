"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
荅曰： a丈 。
"""

"""
Suppose there is a door. When opened, the distance from the door to the lintel (閫) is 1 chi, and when closed, it does not fully meet by 2 cun.
Question: how wide is the door?

Answer: the door is *a* zhang wide.
"""

# 開門去閫一尺 (distance when opened)
開門距離 = 1  # in chi

# 不合二寸 (gap when closed)
不合距離 = Fraction(2, 10)  # 2 cun = 2/10 chi

# The total width of the door is the sum of the two distances
門廣 = 開門距離 + 不合距離

# Convert the width into zhang (1 zhang = 10 chi)
a = Fraction(門廣, 10)  # in zhang
"""
Variable 'a' has wrong value. Expected: 101/100, Actual: 3/25"""
