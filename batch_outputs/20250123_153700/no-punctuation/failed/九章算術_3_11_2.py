"""
今有縑一丈價直一百二十八今有縑一匹九尺五寸問得錢幾何
術曰以一丈寸數為法以價錢數乘今有縑寸數為實實如法得錢數
荅曰 a錢 
"""

"""
Suppose there is a piece of silk 1 zhang in length, valued at 128 qian.
Now there is a piece of silk 1 pi 9 chi 5 cun in length.
Question: how much money is it worth?

The procedure says: Take the number of cun in 1 zhang as the divisor.
Multiply the price in qian by the number of cun in the given piece of silk, obtaining the dividend.
Divide the dividend by the divisor to get the amount of qian.

Answer: *a* qian.
"""

# 縑一丈價直一百二十八
一丈價 = 128

# 一丈寸數為法 (1 zhang = 10 chi = 100 cun)
一丈寸數 = 100

# 今有縑一匹九尺五寸
縑匹寸數 = 9 * 10 + 5  # Convert 9 chi 5 cun to total cun

# 以價錢數乘今有縑寸數為實
實 = 一丈價 * 縑匹寸數

# 實如法得錢數
a = Fraction(實, 一丈寸數)  # Divide by the number of cun in 1 zhang
"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 608/5"""
