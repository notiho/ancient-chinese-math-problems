"""
又有田廣七步、四分步之三，從十五步、九分步之五。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 7 bu and 3/4 bu, and a length of 15 bu and 5/9 bu.
Question: how large is the area of the field?

The procedure for large rectangular fields says:
For fractions, multiply the denominators by their respective integers, and the numerators follow along.
Multiply these together to obtain the dividend.
Multiply the denominators together to obtain the divisor.
Divide the dividend by the divisor to obtain the result.

The answer says: *a* bu.
"""

from fractions import Fraction

# 田廣 7步、4分步之3
廣 = 7 + Fraction(3, 4)

# 從 15步、9分步之5
從 = 15 + Fraction(5, 9)

# 分母各乘其全，分子從之，相乘為實
實 = 廣 * 從

# 分母相乘為法
# Since we are working with fractions, the denominators are already handled internally.

# 實如法而一
a = 實

a#----- content ends here -----

"""
"""
