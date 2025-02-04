"""
今有縑一丈價直一百二十八。今有縑一匹九尺五寸，問︰得錢幾何？
術曰：以一丈寸數為法，以價錢數乘今有縑寸數為實，實如法得錢數。
荅曰： a錢 。
"""

"""
Suppose there is a bolt of silk 1 zhang in length, valued at 128 qian.
Now there is a piece of silk 1 pi 9 chi 5 cun in length.
Question: how much money is it worth?

The procedure says: Take the number of cun in 1 zhang as the divisor.
Multiply the price in qian by the number of cun in the given silk to get the dividend.
Divide the dividend by the divisor to get the amount of money.

Answer: *a* qian.
"""

# 一丈價直一百二十八
一丈價 = 128

# 一丈寸數為法 (1丈 = 10尺, 1尺 = 10寸, so 1丈 = 100寸)
一丈寸數 = 10 * 10

# 今有縑一匹九尺五寸 (1匹 = 9尺5寸 = 9*10 + 5 = 95寸)
今有縑寸數 = 9 * 10 + 5

# 以價錢數乘今有縑寸數為實
實 = 一丈價 * 今有縑寸數

# 實如法得錢數
a = Fraction(實, 一丈寸數)
"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 608/5"""
