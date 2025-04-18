"""
又有田廣七步、四分步之三，從十五步、九分步之五。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a(=1085/9)步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 7 bu and 3/4 bu, and a length of 15 bu and 5/9 bu.
Question: how large of a field does it make?

The procedure for large rectangular fields says: Multiply the denominators of the fractions by their respective integers, and follow the numerators accordingly.
Multiply these together to obtain the dividend.
Multiply the denominators together to obtain the divisor.
Divide the dividend by the divisor to obtain the result.

The answer says: *a*(=1085/9) bu.
"""

from fractions import Fraction

# 廣七步、四分步之三
廣整數 = 7
廣分子 = 3
廣分母 = 4
廣 = 廣整數 + Fraction(廣分子, 廣分母)

# 從十五步、九分步之五
從整數 = 15
從分子 = 5
從分母 = 9
從 = 從整數 + Fraction(從分子, 從分母)

# 分母各乘其全，分子從之，相乘為實
實 = 廣 * 從

# 分母相乘為法
法 = 1  # Since the fractions are already in their simplest form, no need to recompute denominators.

# 實如法而一
a = 實  # 1085/9#----- content ends here -----

"""
"""
