"""
今有三女，長女五日一歸，中女四日一歸，少女三日一歸。問：三女幾何日相會？
答曰： a日 。
"""

#----- content starts here -----
"""
Suppose there are three daughters. The eldest daughter returns home every 5 days, the middle daughter every 4 days, and the youngest daughter every 3 days.
Question: after how many days will all three daughters meet at home?

Answer: *a* days.
"""

# 長女五日一歸
長女 = 5

# 中女四日一歸
中女 = 4

# 少女三日一歸
少女 = 3

# Find the least common multiple (LCM) of the three periods
# LCM is the smallest number divisible by all three periods
a = 長女 * 中女 * 少女 // (Fraction(長女, 中女).denominator * Fraction(長女, 少女).denominator)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60, Actual: 5"""
