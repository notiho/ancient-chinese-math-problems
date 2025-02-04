"""
今有縑一丈價直一百二十八。今有縑一匹九尺五寸，問︰得錢幾何？
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is a piece of silk 1 zhang (10 chi) long, valued at 128 qian.
Now, there is another piece of silk 1 pi (9 chi and 5 cun) long.
Question: how much money is this piece worth?

Answer: it is worth *a* qian.
"""

from fractions import Fraction

# Given values
縑一丈 = 10  # 1 zhang = 10 chi
價值一丈 = 128  # 1 zhang is worth 128 qian
縑一匹 = 9 + Fraction(5, 10)  # 1 pi = 9 chi and 5 cun (1 cun = 1/10 chi)

# Calculate the value of 1 chi of silk
價值一尺 = Fraction(價值一丈, 縑一丈)

# Calculate the value of 1 pi of silk
a = 縑一匹 * 價值一尺

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 608/5"""
