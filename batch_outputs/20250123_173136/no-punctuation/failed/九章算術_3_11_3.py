"""
今有縑一丈價直一百二十八今有縑一匹九尺五寸問得錢幾何
術曰以一丈寸數為法以價錢數乘今有縑寸數為實實如法得錢數
荅曰 a錢 
"""

"""
Suppose there is a piece of silk 1 zhang long, valued at 128 qian.
Now there is a piece of silk 1 pi, 9 chi, and 5 cun long.
Question: how much money is it worth?

The procedure says: Take the number of cun in 1 zhang as the divisor.
Multiply the price in qian by the number of cun in the current piece of silk, obtaining the dividend.
Divide the dividend by the divisor to get the amount of money.

Answer: *a* qian.
"""

# 縑一丈價直一百二十八
一丈價 = 128

# 一丈寸數為法
一丈寸數 = 10 * 10  # 1 zhang = 10 chi, 1 chi = 10 cun, so 1 zhang = 100 cun
法 = 一丈寸數

# 今有縑一匹九尺五寸
縑匹數 = 1 * 10 * 10  # 1 pi = 1 zhang = 100 cun
縑尺數 = 9 * 10       # 9 chi = 90 cun
縑寸數 = 5            # 5 cun
今有縑寸數 = 縑匹數 + 縑尺數 + 縑寸數

# 以價錢數乘今有縑寸數為實
實 = 一丈價 * 今有縑寸數

# 實如法得錢數
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 1248/5"""
