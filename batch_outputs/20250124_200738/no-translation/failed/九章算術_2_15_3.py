"""
今有粟七斗八升，欲為豉。問︰得幾何？
術曰：以粟求豉，六十三之，五十而一。
荅曰：為豉 a斗 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 粟七斗八升
粟 = 7 * 10 + 8  # 1斗 = 10升, 所以將粟轉換為升

# 以粟求豉，六十三之
豉 = 63 * 粟

# 五十而一
a = Fraction(豉, 50)  # 結果以斗為單位
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 2457/250, Actual: 2457/25"""
