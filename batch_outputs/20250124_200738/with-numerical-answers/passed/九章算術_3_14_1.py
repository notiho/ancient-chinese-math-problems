"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
術曰：以一十四斤兩數為法，以一十斤乘今有絲兩數為實，實如法得縑數。
荅曰： a(=65/2)斤 。
"""

#----- content starts here -----
"""
Suppose 14 jin of silk is given to someone, and it is agreed to obtain 10 jin of silk fabric in return.
Now, if 45 jin and 8 liang of silk are given, how much silk fabric will be obtained?

The procedure says: Take the numbers of 14 jin as the divisor. 
Multiply the 10 jin by the current number of silk (in liang) to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of silk fabric.

Answer: *a*(=65/2) jin.
"""

# 與人絲一十四斤
絲_原 = 14

# 約得縑一十斤
縑_原 = 10

# 今與人絲四十五斤八兩
絲_今 = 45 + Fraction(8, 16)  # Convert 8 liang to jin (16 liang = 1 jin)

# 以一十四斤兩數為法
法 = 絲_原

# 以一十斤乘今有絲兩數為實
實 = 縑_原 * 絲_今

# 實如法得縑數
a = Fraction(實, 法)  # 65/2 jin#----- content ends here -----

"""
"""
