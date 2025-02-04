"""
今有絲一斤價直二百四十今有錢一千三百二十八問得絲幾何
術曰以一斤價數為法以一斤乘今有錢數為實實如法得絲數
荅曰 a斤 
"""

"""
Suppose there is 1 jin of silk worth 240 qian. Now, there are 1328 qian.
Question: how much silk can be obtained?

The procedure says: Take the price of 1 jin as the divisor.
Multiply 1 jin by the current amount of qian to obtain the dividend.
Divide the dividend by the divisor to get the amount of silk.

Answer: *a* jin.
"""

# 絲一斤價直二百四十
一斤價 = 240

# 今有錢一千三百二十八
今有錢數 = 1328

# 以一斤價數為法
法 = 一斤價

# 以一斤乘今有錢數為實
實 = 1 * 今有錢數

# 實如法得絲數
a = Fraction(實, 法)
"""
"""
