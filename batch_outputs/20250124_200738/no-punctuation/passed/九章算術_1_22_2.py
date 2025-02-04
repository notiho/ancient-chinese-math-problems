"""
又有田廣七步四分步之三從十五步九分步之五問為田幾何
大廣田術曰分母各乘其全分子從之相乘為實分母相乘為法實如法而一
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 7 bu and 3/4 bu, and a length of 15 bu and 5/9 bu.
Question: how large of a field does it make?

The procedure for large rectangular fields says: Multiply the denominators of the fractions by their respective integers.
Multiply the numerators of the fractions by their respective integers.
The products are the dividend.
The denominators are multiplied together to form the divisor.
Divide the dividend by the divisor to obtain the result.

The answer says: *a* bu.
"""

from fractions import Fraction

# 田廣七步四分步之三
廣 = 7 + Fraction(3, 4)

# 從十五步九分步之五
從 = 15 + Fraction(5, 9)

# 分母各乘其全，分子從之相乘為實
實 = 廣 * 從

# 分母相乘為法
法 = 1  # Since the fractions are already combined, no need to recompute denominators.

# 實如法而一
a = 實  # The result is already in terms of bu.#----- content ends here -----

"""
"""
