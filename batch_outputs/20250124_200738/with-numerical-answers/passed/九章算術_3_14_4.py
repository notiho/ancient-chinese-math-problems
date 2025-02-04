"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
術曰：以一十四斤兩數為法，以一十斤乘今有絲兩數為實，實如法得縑數。
荅曰： a(=65/2)斤 。
"""

#----- content starts here -----
"""
Suppose 14 jin of silk is given to someone, and it is agreed that 10 jin of silk fabric will be obtained.
Now, if 45 jin and 8 liang of silk are given, how much silk fabric will be obtained?

The procedure says: Take the 14 jin (converted to liang) as the divisor.
Multiply the 10 jin (converted to liang) by the current amount of silk (converted to liang) to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of silk fabric.

Answer: *a*(=65/2) jin.
"""

# 與人絲一十四斤
絲_原 = 14

# 約得縑一十斤
縑_原 = 10

# 斤轉換為兩 (1 斤 = 16 兩)
絲_原_兩 = 16 * 絲_原
縑_原_兩 = 16 * 縑_原

# 今與人絲四十五斤八兩
絲_今_斤 = 45
絲_今_兩 = 8
絲_今 = 16 * 絲_今_斤 + 絲_今_兩

# 以一十四斤兩數為法
法 = 絲_原_兩

# 以一十斤乘今有絲兩數為實
實 = 縑_原_兩 * 絲_今

# 實如法得縑數
縑_今_兩 = Fraction(實, 法)

# 轉換回斤
a = Fraction(縑_今_兩, 16)  # 65/2 (32.5 斤)#----- content ends here -----

"""
"""
