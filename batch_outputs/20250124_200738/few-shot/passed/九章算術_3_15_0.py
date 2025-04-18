"""
今有絲一斤，耗七兩。今有絲二十三斤五兩，問︰耗幾何？
術曰：以一斤展十六兩為法，以七兩乘今有絲兩數為實，實如法得耗數。
荅曰： a兩 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of silk, and 7 liang are wasted. Now there are 23 jin and 5 liang of silk.
Question: how much is wasted?

The procedure says: Take 1 jin as 16 liang as the divisor. Multiply 7 liang by the current number of liang of silk to get the dividend. Divide the dividend by the divisor to obtain the amount of waste.

Answer: *a* liang.
"""

# 絲一斤，耗七兩
耗 = 7

# 一斤展十六兩為法
法 = 16

# 今有絲二十三斤五兩
今有絲_斤 = 23
今有絲_兩 = 5

# 將絲的總量轉換為兩
今有絲_總兩 = (今有絲_斤 * 法) + 今有絲_兩

# 以七兩乘今有絲兩數為實
實 = 耗 * 今有絲_總兩

# 實如法得耗數
a = Fraction(實, 法)#----- content ends here -----

"""
"""
