"""
今有絲一斤，耗七兩。今有絲二十三斤五兩，問︰耗幾何？
術曰：以一斤展十六兩為法，以七兩乘今有絲兩數為實，實如法得耗數。
荅曰： a兩 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of silk, and it loses 7 liang during processing.
Now, there are 23 jin and 5 liang of silk.
Question: how much is lost?

The procedure says: Take 1 jin as 16 liang as the divisor.
Multiply 7 liang by the current number of liang of silk to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of loss.

Answer: *a* liang.
"""

# 絲一斤，耗七兩
耗率 = 7

# 一斤展十六兩
一斤 = 16

# 今有絲二十三斤五兩
今有絲 = 23 * 一斤 + 5  # Convert to liang

# 以七兩乘今有絲兩數為實
實 = 耗率 * 今有絲

# 實如法得耗數
a = Fraction(實, 一斤)  # Result in liang#----- content ends here -----

"""
"""
