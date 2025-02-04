"""
又有積二萬五千二百八十一步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is an area of 25281 bu. 
Question: what is the side length of the square field?

The procedure for square root extraction says: Place the area as the dividend.
Borrow one counting rod, and determine the approximate value of the square root by finding the largest number whose square does not exceed the area.
Multiply this borrowed number by itself, and use it as the divisor.
Divide the area by this divisor to get the quotient.
Double the divisor to form the "fixed divisor."
If there is a remainder, continue the process by subtracting the square of the quotient from the area, and repeat the steps.
If the square root cannot be extracted exactly, express the result as a fraction.
If the area has a fractional part, adjust the calculation accordingly.

Answer: *a* bu.
"""

from fractions import Fraction

# 積二萬五千二百八十一步
積 = 25281

# 開方術
def 開方(積):
    # Initialize variables
    定法 = 0  # Fixed divisor
    借算 = 0  # Borrowed number (approximate square root)
    餘數 = 積  # Remainder

    while True:
        # Find the largest number whose square does not exceed the remainder
        借算 += 1
        if 借算 ** 2 > 積:
            借算 -= 1
            break

    # Compute the fixed divisor
    定法 = 2 * 借算

    # Compute the remainder
    餘數 = 積 - 借算 ** 2

    # If there is no remainder, return the result
    if 餘數 == 0:
        return 借算

    # If there is a remainder, express the result as a fraction
    分母 = 定法
    分子 = 餘數
    return 借算 + Fraction(分子, 分母)

# Calculate the side length
a = 開方(積)#----- content ends here -----

"""
"""
