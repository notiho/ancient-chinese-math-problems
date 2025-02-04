"""
今有絲一斤，耗七兩。今有絲二十三斤五兩，問︰耗幾何？
術曰：以一斤展十六兩為法，以七兩乘今有絲兩數為實，實如法得耗數。
荅曰： a兩 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of silk, and it loses 7 liang during processing.
Now, there is 23 jin and 5 liang of silk.
Question: how much is lost?

The procedure says: Take 1 jin as 16 liang as the divisor.
Multiply 7 liang by the total number of liang in the given silk, obtaining the dividend.
Divide the dividend by the divisor to get the amount of loss.

Answer: *a* liang.
"""

from fractions import Fraction

# 1斤 = 16兩
一斤 = 16

# 耗七兩
耗 = 7

# 今有絲二十三斤五兩
絲_斤 = 23
絲_兩 = 5

# 將絲的總量轉換為兩
絲_總兩 = (絲_斤 * 一斤) + 絲_兩

# 以七兩乘今有絲兩數為實
實 = 耗 * 絲_總兩

# 實如法得耗數
a = Fraction(實, 一斤)

a  # 答案以兩為單位#----- content ends here -----

"""
"""
