"""
今有田廣三步三分步之一從五步五分步之二問為田幾何
大廣田術曰分母各乘其全分子從之相乘為實分母相乘為法實如法而一
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 3 bu and 1/3 bu, and a length of 5 bu and 2/5 bu.
Question: how large of a field does it make?

The procedure for rectangular fields says: Multiply the denominators of the fractions by their respective whole parts.
Then, multiply the numerators of the fractions by the corresponding terms.
The product becomes the dividend, and the product of the denominators becomes the divisor.
Divide the dividend by the divisor to obtain the result.

The answer says: *a* bu.
"""

from fractions import Fraction

# 田廣三步三分步之一
廣 = 3 + Fraction(1, 3)

# 從五步五分步之二
從 = 5 + Fraction(2, 5)

# 分母各乘其全，分子從之相乘為實
實 = 廣 * 從

# 分母相乘為法
法 = 1  # Since the fractions are already in their simplest form, no need to recompute denominators.

# 實如法而一
a = 實  # The result is already in terms of bu.#----- content ends here -----

"""
"""
