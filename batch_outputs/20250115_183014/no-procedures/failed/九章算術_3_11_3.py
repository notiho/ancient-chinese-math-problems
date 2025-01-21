"""
今有縑一丈價直一百二十八。今有縑一匹九尺五寸，問︰得錢幾何？
荅曰： a錢 。
"""

"""
Suppose there is a piece of silk 1 zhang long, valued at 128 qian.
Now, there is a piece of silk 1 pi (9 chi and 5 cun) long.
Question: how much is it worth?

Answer: it is worth *a* qian.
"""

from fractions import Fraction

# 1 zhang = 10 chi
丈長 = 10  # in chi
丈價 = 128  # in qian

# 1 pi = 9 chi + 5 cun (1 chi = 10 cun)
匹長 = 9 + Fraction(5, 10)  # in chi

# Calculate the price per chi
每尺價 = 丈價 / 丈長

# Calculate the price of the silk piece
a = 每尺價 * 匹長

a  # The value in qian
"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 121.60000000000001"""
