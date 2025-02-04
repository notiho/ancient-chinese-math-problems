"""
又有田廣七步、四分步之三，從十五步、九分步之五。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 7 bu and 3/4 bu, and a length of 15 bu and 5/9 bu.
Question: how large of a field does it make?

The procedure for large rectangular fields says: Multiply the denominators of the fractions by their respective integers, and the numerators follow accordingly.
Multiply these values to obtain the dividend.
Multiply the denominators to obtain the divisor.
Divide the dividend by the divisor to obtain the result.

The answer says: *a* bu.
"""

from fractions import Fraction

# 田廣七步、四分步之三
廣 = 7 + Fraction(3, 4)

# 從十五步、九分步之五
從 = 15 + Fraction(5, 9)

# 分母各乘其全，分子從之，相乘為實
實 = 廣 * 從

# 分母相乘為法
# (This is already handled by Fraction multiplication internally)

# 實如法而一
a = 實

a#----- content ends here -----

"""
"""
