"""
今有縑一丈價直一百二十八。今有縑一匹九尺五寸，問︰得錢幾何？
術曰：以一丈寸數為法，以價錢數乘今有縑寸數為實，實如法得錢數。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is one zhang of silk, valued at 128 qian.
Now, there is a piece of silk measuring 1 pi, 9 chi, and 5 cun.
Question: how much money is it worth?

The procedure says: Take the number of cun in one zhang as the divisor.
Multiply the price in qian by the number of cun in the given piece of silk, obtaining the dividend.
Divide the dividend by the divisor to get the amount of qian.

Answer: it is worth *a* qian.
"""

from fractions import Fraction

# 一丈價直一百二十八
丈價 = 128

# 一丈等於 10 尺，每尺等於 10 寸
一丈寸數 = 10 * 10

# 今有縑一匹九尺五寸
匹 = 1
尺 = 9
寸 = 5

# 將縑的總寸數計算出來
縑寸數 = (匹 * 一丈寸數) + (尺 * 10) + 寸

# 以價錢數乘今有縑寸數為實
實 = 丈價 * 縑寸數

# 實如法得錢數
a = Fraction(實, 一丈寸數)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 1248/5"""
