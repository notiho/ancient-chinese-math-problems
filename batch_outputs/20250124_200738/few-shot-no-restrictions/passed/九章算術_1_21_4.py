"""
今有田廣三步、三分步之一，從五步、五分步之二。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 3 bu and 1/3 bu, and a length of 5 bu and 2/5 bu.
Question: how large is the field?

The procedure for rectangular fields says: Multiply the denominators of the fractions by their respective whole numbers, and the numerators follow along. Multiply these together to obtain the dividend. Multiply the denominators together to obtain the divisor. Divide the dividend by the divisor to obtain the result.

Answer: *a* bu.
"""

from fractions import Fraction

# 田廣三步、三分步之一
廣 = 3 + Fraction(1, 3)

# 從五步、五分步之二
從 = 5 + Fraction(2, 5)

# 分母各乘其全，分子從之，相乘為實
實 = 廣 * 從

# 分母相乘為法
# 实际上，Python 的 Fraction 类已经自动处理分母和分子的乘法和约分，因此无需手动计算分母。
a = 實

# Answer
a#----- content ends here -----

"""
"""
