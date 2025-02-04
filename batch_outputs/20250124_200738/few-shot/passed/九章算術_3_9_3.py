"""
今有絲一斤，價直二百四十。今有錢一千三百二十八，問︰得絲幾何？
術曰：以一斤價數為法，以一斤乘今有錢數為實，實如法得絲數。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of silk, priced at 240 coins.
Now there are 1328 coins.
Question: how much silk can be obtained?

The procedure says: Take the price of 1 jin as the divisor.
Multiply 1 jin by the number of coins currently available, obtaining the dividend.
Divide the dividend by the divisor to get the amount of silk.

Answer: *a* jin.
"""

# 絲一斤
絲一斤 = 1

# 價直二百四十
一斤價數 = 240

# 今有錢一千三百二十八
今有錢數 = 1328

# 以一斤價數為法
法 = 一斤價數

# 以一斤乘今有錢數為實
實 = 絲一斤 * 今有錢數

# 實如法得絲數
a = Fraction(實, 法)#----- content ends here -----

"""
"""
