"""
又有田廣七步、四分步之三，從十五步、九分步之五。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 7 bu and 3/4 bu, and a length of 15 bu and 5/9 bu.
Question: how large is the field?

The procedure for rectangular fields says: Multiply the denominators of the fractions by their respective integers, and keep the numerators as they are. Multiply these together to obtain the dividend. Multiply the denominators together to obtain the divisor. Divide the dividend by the divisor to obtain the result.

Answer: *a* bu.
"""

from fractions import Fraction

# 田廣七步、四分步之三
廣 = 7 + Fraction(3, 4)

# 從十五步、九分步之五
從 = 15 + Fraction(5, 9)

# 分母各乘其全，分子從之，相乘為實
實 = 廣 * 從

# 分母相乘為法
# 实际上，分母已经被处理在 Fraction 类中，不需要手动计算。

# 實如法而一
a = 實

a  # Output the result in bu#----- content ends here -----

"""
"""
