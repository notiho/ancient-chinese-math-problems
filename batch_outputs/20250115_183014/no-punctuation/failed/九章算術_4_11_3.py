"""
今有積五萬五千二百二十五步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

"""
Suppose there is an area of 55225 bu².
Question: what is the side length of the square field?

The procedure for square root extraction says: Place the area as the dividend.
Borrow one counting rod to represent the square root's digits, exceeding one place.
Estimate the first digit of the root. Multiply it by itself to form the divisor.
Divide the dividend by the divisor, and double the divisor to form the new divisor.
Continue dividing, adjusting the divisor by adding the doubled root digit.
If the square root cannot be extracted exactly, represent the result as a side length with a remainder.
If the area has fractional parts, convert them to a common denominator and proceed as before.
If the denominator cannot be square-rooted, multiply the numerator by the denominator and proceed.

Answer: *a* bu.
"""

# 積五萬五千二百二十五步
積 = 55225

# 開方術
def 開方(積):
    # Initialize variables
    借算 = 0  # Represents the current digit of the root
    定法 = 0  # Represents the divisor
    根 = 0    # Represents the square root being constructed

    while 積 > 0:
        # Step 1: Borrow one digit (shift left by one place)
        積 *= 100 if 借算 > 0 else 1  # Only shift for subsequent iterations
        借算 += 1

        # Step 2: Estimate the next digit of the root
        for i in range(9, -1, -1):  # Try digits from 9 to 0
            試法 = 定法 * 10 + i * i
            if 試法 <= 積:
                根 = 根 * 10 + i
                積 -= 試法
                定法 = 2 * 根
                break

    return 根

# Calculate the square root
a = 開方(積)
"""
Timed out"""
