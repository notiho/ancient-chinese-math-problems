"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
術曰：以一十四斤兩數為法，以一十斤乘今有絲兩數為實，實如法得縑數。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose 14 jin of silk is given to someone, and it is agreed to obtain 10 jin of silk fabric in return.
Now, 45 jin and 8 liang of silk is given. 
Question: how much silk fabric is obtained?

The procedure says: Take the 14 jin as the divisor. 
Multiply the 10 jin by the current amount of silk (in liang), obtaining the dividend.
Divide the dividend by the divisor to get the amount of silk fabric.

Answer: *a* jin.
"""

# 與人絲一十四斤
絲_原 = 14

# 約得縑一十斤
縑_原 = 10

# 今與人絲四十五斤八兩
絲_今_斤 = 45
絲_今_兩 = 8

# 轉換絲為兩 (1 斤 = 16 兩)
絲_今_兩數 = (絲_今_斤 * 16) + 絲_今_兩

# 以一十四斤兩數為法
法 = 絲_原 * 16  # 將 14 斤轉換為兩

# 以一十斤乘今有絲兩數為實
實 = 縑_原 * 16 * 絲_今_兩數  # 將 10 斤轉換為兩

# 實如法得縑數
縑_兩數 = Fraction(實, 法)

# 將縑數轉換回斤
a = Fraction(縑_兩數, 16)  # 1 斤 = 16 兩#----- content ends here -----

"""
"""
