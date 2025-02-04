"""
今有縑一丈價直一百二十八。今有縑一匹九尺五寸，問︰得錢幾何？
術曰：以一丈寸數為法，以價錢數乘今有縑寸數為實，實如法得錢數。
荅曰： a(=3168/5)錢 。
"""

"""
Suppose there is silk of 1 zhang, valued at 128 qian.
Now there is silk of 1 pi and 9 chi 5 cun.
Question: how much money is it worth?

The procedure says: Take the number of cun in 1 zhang as the divisor.
Multiply the value in qian by the number of cun in the given silk, obtaining the dividend.
Divide the dividend by the divisor to obtain the amount of qian.

Answer: *a*(=3168/5) qian.
"""

# 縑一丈價直一百二十八
一丈價 = 128

# 一丈寸數為法
一丈寸數 = 10 * 10 # 1 zhang = 10 chi, 1 chi = 10 cun

# 今有縑一匹九尺五寸
今有縑寸數 = (1 * 10 * 10) + (9 * 10) + 5 # 1 pi = 1 zhang = 10 chi, plus 9 chi and 5 cun

# 以價錢數乘今有縑寸數為實
實 = 一丈價 * 今有縑寸數

# 實如法得錢數
a = Fraction(實, 一丈寸數) # 3168/5 qian
"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 1248/5"""
