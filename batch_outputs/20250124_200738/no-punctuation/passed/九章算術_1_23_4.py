"""
又有田廣十八步七分步之五從二十三步十一分步之六問為田幾何
大廣田術曰分母各乘其全分子從之相乘為實分母相乘為法實如法而一
荅曰 a畝 
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 18 bu and 5/7 bu, and a length of 23 bu and 6/11 bu.
Question: how large of a field does it make?

The procedure for rectangular fields with fractions says: Multiply the denominators of each fraction by their respective whole numbers.
Take the numerators and multiply them accordingly to obtain the dividend.
Multiply the denominators to obtain the divisor.
Divide the dividend by the divisor to obtain the result.

The answer says: *a* mu.
"""

from fractions import Fraction

# 廣 18步 7分步之5
廣 = 18 + Fraction(5, 7)

# 從 23步 11分步之6
從 = 23 + Fraction(6, 11)

# 大廣田術：分母各乘其全，分子從之相乘為實
積 = 廣 * 從

# 畝法二百四十步
畝法 = 240

# 實如法而一
a = Fraction(積, 畝法)#----- content ends here -----

"""
"""
