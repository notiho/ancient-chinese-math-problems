"""
今有縑一丈價直一百二十八。今有縑一匹九尺五寸，問︰得錢幾何？
術曰：以一丈寸數為法，以價錢數乘今有縑寸數為實，實如法得錢數。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is a piece of silk 1 zhang in length, valued at 128 qian.
Now, there is a piece of silk 1 pi and 9 chi 5 cun in length.
Question: how much money is it worth?

The procedure says: Take the number of cun in 1 zhang as the divisor.
Multiply the price in qian by the number of cun in the given silk to get the dividend.
Divide the dividend by the divisor to get the amount of money.

Answer: *a* qian.
"""

from fractions import Fraction

# 1丈 = 10尺, 1尺 = 10寸
丈寸數 = 10 * 10  # Total cun in 1 zhang

# 1丈價直128錢
價錢數 = 128

# 今有縑1匹9尺5寸
縑寸數 = (1 * 10 * 10) + (9 * 10) + 5  # Convert 1 pi 9 chi 5 cun to total cun

# 以價錢數乘今有縑寸數為實
實 = 價錢數 * 縑寸數

# 實如法得錢數
a = Fraction(實, 丈寸數)

a  # Output the value of a in qian#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 1248/5"""
