"""
又有積二萬五千二百八十一步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

"""
Suppose there is an area of 25,280 square bu. 
Question: what is the side length of the square field?

The procedure for extracting the square root says: Place the area as the dividend. Borrow one counting rod for the side length, exceeding one rank. Discuss the result obtained. Multiply the borrowed counting rod by itself, making the divisor. Divide the dividend by the divisor. Double the divisor, making the fixed divisor. Subtract the remainder from the fixed divisor, and place it below. Borrow another counting rod for the side length as before. Discuss again. Multiply the result obtained by itself, adding to the fixed divisor. Divide again. Repeat the process as before. If the square root cannot be extracted exactly, it is considered unsolvable, and the side length is expressed as a fraction. If the area has a fractional part, normalize it and proceed as before. Extract the square root of the numerator and denominator separately. If the denominator cannot be extracted, multiply the numerator by the denominator and proceed as before.

Answer: *a* bu.
"""

from fractions import Fraction

# 積二萬五千二百八十一步
積 = 25280

# 開方術
def 開方(積):
    # Initialize variables
    定法 = 0  # Fixed divisor
    復 = 0    # Current side length
    實 = 積   # Remaining dividend

    while True:
        # Borrow one counting rod for the side length
        借算步 = 復 * 10

        # Discuss the result obtained
        for i in range(10):
            試 = 借算步 + i
            法 = 試 * 試
            if 法 > 實:
                break
        i -= 1

        # Update the side length
        復 = 借算步 + i

        # Multiply the borrowed counting rod by itself, making the divisor
        法 = 復 * 復

        # Subtract the divisor from the dividend
        實 -= 法

        # Double the divisor, making the fixed divisor
        定法 = 2 * 復

        # If the remainder is zero, the square root is exact
        if 實 == 0:
            return 復

        # If the remainder is less than the fixed divisor, the square root cannot be extracted exactly
        if 實 < 定法:
            return Fraction(復, 10)

# Calculate the side length
a = 開方(積)
"""
Variable 'a' has wrong value. Expected: 159, Actual: 879/10"""
