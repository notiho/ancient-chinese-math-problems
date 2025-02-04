"""
今有縑一丈價直一百二十八。今有縑一匹九尺五寸，問︰得錢幾何？
荅曰： a錢 。
"""

"""
Suppose there is a piece of silk 1 zhang (10 chi) in length, valued at 128 qian.
Now, there is another piece of silk 1 pi (9 chi and 5 cun). 
Question: how much money is this piece worth?

Answer: it is worth *a* qian.
"""

from fractions import Fraction

# Value of 1 zhang (10 chi) of silk
value_per_zhang = 128

# Length of 1 zhang in chi
length_per_zhang = 10

# Length of the silk in question: 9 chi and 5 cun (1 chi = 10 cun)
length_of_silk = 9 + Fraction(5, 10)

# Calculate the value of the silk
a = value_per_zhang * length_of_silk / length_per_zhang

a
"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 608/5"""
