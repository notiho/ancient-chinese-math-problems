"""
今有絲一斤，價直二百四十。今有錢一千三百二十八，問︰得絲幾何？
術曰：以一斤價數為法，以一斤乘今有錢數為實，實如法得絲數。
荅曰： a(=83/15)斤 。
"""

"""
Suppose there is 1 jin of silk, priced at 240. Now there are 1328 coins.
Question: how much silk can be obtained?

The procedure says: Take the price of 1 jin as the divisor. Multiply 1 jin by the number of coins currently available, giving the dividend. Divide the dividend by the divisor to obtain the amount of silk.

Answer: *a*(=83/15) jin.
"""

# 絲一斤價直二百四十
一斤價 = 240

# 今有錢一千三百二十八
錢數 = 1328

# 以一斤價數為法
法 = 一斤價

# 以一斤乘今有錢數為實
實 = 1 * 錢數

# 實如法得絲數
a = Fraction(實, 法) # 83/15

"""
"""
