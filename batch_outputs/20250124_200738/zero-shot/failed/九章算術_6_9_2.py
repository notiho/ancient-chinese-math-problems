"""
今有絡絲一斤為練絲一十二兩，練絲一斤為青絲一斤十二銖。今有青絲一斤，問︰本絡絲幾何？
術曰：以練絲十二兩乘青絲一斤一十二銖為法。以青絲一斤銖數乘練絲一斤兩數，又以絡絲一斤乘之，為實。實如法得一斤。
荅曰： a斤 。
"""

"""
To solve this problem, we will calculate the amount of raw silk (絡絲) required to produce one pound (一斤) of finished silk (青絲). The problem involves converting between different units of weight (斤, 兩, 銖). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Conversion factors
jin_to_liang = 16  # 1 斤 = 16 兩
liang_to_zhu = 24  # 1 兩 = 24 銖

# Given data
lian_silk_per_jin = 12  # 練絲 per 絡絲 (in 兩)
qing_silk_per_jin = Fraction(1, 1) + Fraction(12, liang_to_zhu)  # 青絲 per 練絲 (in 斤)

# Total 銖 in 1 斤 of 青絲
qing_silk_in_zhu = qing_silk_per_jin * jin_to_liang * liang_to_zhu

# Total 銖 in 1 斤 of 練絲
lian_silk_in_zhu = lian_silk_per_jin * liang_to_zhu

# Calculate 絡絲 required
a = qing_silk_in_zhu / lian_silk_in_zhu

# Result
a  # This is the amount of 絡絲 in 斤
#----- content ends here -----


"""


The variable `a` will contain the result in units of 斤.
"""


"""
Variable 'a' has wrong value. Expected: 128/99, Actual: 2"""
