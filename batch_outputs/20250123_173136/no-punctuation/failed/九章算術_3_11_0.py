"""
今有縑一丈價直一百二十八今有縑一匹九尺五寸問得錢幾何
術曰以一丈寸數為法以價錢數乘今有縑寸數為實實如法得錢數
荅曰 a錢 
"""

"""
Suppose there is a bolt of silk 1 zhang long, priced at 128 qian.
Now, there is a piece of silk 1 pi 9 chi 5 cun long.
Question: how much money is it worth?

The procedure says: Take the number of cun in 1 zhang as the divisor.
Multiply the price in qian by the number of cun in the given silk to get the dividend.
Divide the dividend by the divisor to get the amount of qian.

Answer: *a* qian.
"""

# 一丈價直一百二十八
價錢數 = 128

# 一丈寸數為法 (1丈 = 10尺, 1尺 = 10寸)
一丈寸數 = 10 * 10

# 今有縑一匹九尺五寸
縑寸數 = (1 * 10 * 10) + (9 * 10) + 5  # Convert 1匹9尺5寸 to total寸

# 以價錢數乘今有縑寸數為實
實 = 價錢數 * 縑寸數

# 實如法得錢數
a = Fraction(實, 一丈寸數)  # Divide by the number of寸 in 1丈
"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 1248/5"""
