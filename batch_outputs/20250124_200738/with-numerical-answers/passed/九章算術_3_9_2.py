"""
今有絲一斤，價直二百四十。今有錢一千三百二十八，問︰得絲幾何？
術曰：以一斤價數為法，以一斤乘今有錢數為實，實如法得絲數。
荅曰： a(=83/15)斤 。
"""

#----- content starts here -----
"""
Suppose there is one jin of silk, priced at 240. Now there are 1328 coins.
Question: how much silk can be obtained?

The procedure says: Take the price of one jin as the divisor.
Multiply one jin by the number of coins currently available, giving the dividend.
Divide the dividend by the divisor, obtaining the amount of silk.

Answer: *a*(=83/15) jin.
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
a = Fraction(實, 法) # 83/15
#----- content ends here -----

"""
"""
