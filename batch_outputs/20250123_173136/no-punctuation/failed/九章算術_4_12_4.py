"""
又有積二萬五千二百八十一步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

"""
Suppose there is an area of 25,280 square bu. 
Question: what are the side lengths of the square field?

The procedure for square root extraction says: Place the area as the dividend. Borrow one counting rod column for the side length, exceeding one rank. Discuss the result obtained. Multiply the borrowed one column by itself to form the divisor. Divide the dividend by the divisor. Double the divisor to form the fixed divisor. Subtract the result of the division from the dividend. Place the remainder below. Borrow another column for the side length as before. Discuss the result obtained. Multiply it by itself and add it to the fixed divisor. Divide the new dividend by this updated divisor. Subtract the result of the division from the dividend and repeat as before. If the square root cannot be fully extracted, it is considered unsolvable, and the result should be expressed in terms of the area. If the area has fractions, convert them to a common denominator and extract the square root of the numerator and denominator separately. If the denominator cannot be square-rooted, multiply the numerator by the denominator and extract the square root of the product.

Answer: *a* bu.
"""

from fractions import Fraction

# 積二萬五千二百八十一步
積 = 25280

# 開方術
def 開方(積):
    # Initialize variables
    實 = 積  # Dividend
    定法 = 0  # Fixed divisor
    開得 = 0  # Result of the square root

    while 實 > 0:
        # Borrow one column for the side length
        借算 = 1

        # 議所得 (find the largest number whose square is less than or equal to 實)
        所得 = 0
        while (所得 + 1) ** 2 <= 實:
            所得 += 1

        # Multiply the borrowed column by itself to form the divisor
        法 = (借算 * 所得) ** 2

        # Divide the dividend by the divisor
        商 = 所得

        # Double the divisor to form the fixed divisor
        定法 = 2 * 所得

        # Subtract the result of the division from the dividend
        實 -= 商 ** 2

        # Add the result to the square root
        開得 = 開得 * 10 + 商

        # If the remainder is zero, break
        if 實 == 0:
            break

    return 開得

# Calculate the square root
a = 開方(積)
"""
Variable 'a' has wrong value. Expected: 159, Actual: 1597511"""
