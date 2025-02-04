"""
今有縑一丈價直一百二十八。今有縑一匹九尺五寸，問︰得錢幾何？
術曰：以一丈寸數為法，以價錢數乘今有縑寸數為實，實如法得錢數。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is silk 1 zhang in length, valued at 128 qian.
Now there is silk 1 pi (9 chi and 5 cun in length).
Question: how much money is it worth?

The procedure says: Take the number of cun in 1 zhang as the divisor.
Multiply the price in qian by the number of cun in the given silk to get the dividend.
Divide the dividend by the divisor to get the amount of money.

Answer: *a* qian.
"""

from fractions import Fraction

# 1 丈 = 10 尺 = 100 寸
一丈寸數 = 100

# 1 丈價值
一丈價值 = 128

# 今有縑 1 匹 = 9 尺 5 寸
今有縑寸數 = 9 * 10 + 5  # Convert to cun

# 以價錢數乘今有縑寸數為實
實 = 一丈價值 * 今有縑寸數

# 實如法得錢數
a = Fraction(實, 一丈寸數)

a  # Output the value in qian#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 608/5"""
