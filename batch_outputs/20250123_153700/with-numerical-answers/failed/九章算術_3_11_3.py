"""
今有縑一丈價直一百二十八。今有縑一匹九尺五寸，問︰得錢幾何？
術曰：以一丈寸數為法，以價錢數乘今有縑寸數為實，實如法得錢數。
荅曰： a(=3168/5)錢 。
"""

"""
Suppose there is silk, one zhang in length, worth 128 qian.
Now there is a piece of silk 1 pi 9 chi 5 cun in length.
Question: how much money is it worth?

The procedure says: Take the number of cun in one zhang as the divisor.
Multiply the price in qian by the number of cun in the given silk, obtaining the dividend.
Divide the dividend by the divisor to obtain the amount of money.

Answer: *a*(=3168/5) qian.
"""

# 一丈價直一百二十八
一丈價 = 128

# 一丈寸數為法
一丈寸數 = 10 * 10 # 1 zhang = 10 chi, 1 chi = 10 cun

# 今有縑一匹九尺五寸
縑長度 = 1 * 10 * 10 + 9 * 10 + 5 # Convert 1 pi 9 chi 5 cun to cun

# 以價錢數乘今有縑寸數為實
實 = 一丈價 * 縑長度

# 實如法得錢數
a = Fraction(實, 一丈寸數) # 3168/5 qian
"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 1248/5"""
