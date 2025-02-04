"""
今有絲一斤，耗七兩。今有絲二十三斤五兩，問︰耗幾何？
術曰：以一斤展十六兩為法，以七兩乘今有絲兩數為實，實如法得耗數。
荅曰： a(=2611/16)兩 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of silk, and it loses 7 liang during processing.
Now suppose there are 23 jin and 5 liang of silk.
Question: how much is lost?

The procedure says: Take 1 jin as 16 liang as the divisor.
Multiply 7 liang by the current number of liang of silk, giving the dividend.
Divide the dividend by the divisor, obtaining the amount of loss.

Answer: *a*(=2611/16) liang.
"""

# 一斤展十六兩為法
法 = 16

# 耗七兩
耗率 = 7

# 今有絲二十三斤五兩
絲斤 = 23
絲兩 = 5

# 將絲轉換為總兩數
絲總兩 = (絲斤 * 16) + 絲兩

# 以七兩乘今有絲兩數為實
實 = 耗率 * 絲總兩

# 實如法得耗數
a = Fraction(實, 法) # 2611/16
#----- content ends here -----

"""
"""
