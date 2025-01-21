"""
又有積二萬五千二百八十一步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

"""
Suppose there is an area of 25,280 square bu. 
Question: what is the side length of the square field?

The procedure for extracting the square root says: Place the area as the dividend. Borrow one counting rod for the side length, exceeding one rank. Discuss the result obtained. Multiply the borrowed counting rod by itself to form the divisor, and divide. Double the divisor to form the fixed divisor. Continue dividing, adjusting the divisor downward, and repeat the process. Place the borrowed counting rod again as before, and repeat the discussion. Multiply the result obtained by itself, add it to the fixed divisor, and divide. Continue until the square root is fully extracted. If it cannot be fully extracted, it is considered "not exact" and should be expressed as a fractional side length. If the area has a fractional part, convert it into a common fraction and proceed as before. Extract the square root of the numerator and denominator separately. If the denominator cannot be extracted, multiply the numerator by the denominator and extract the square root, ensuring the denominator remains as it was.

Answer: *a* bu.
"""

# 積二萬五千二百八十一步
積 = 25280

# 開方術
def 開方(積):
    # Initialize variables
    商 = 0  # The side length (result)
    餘數 = 積  # Remainder
    定法 = 0  # Fixed divisor

    while 餘數 > 0:
        # Borrow one counting rod for the side length
        借算 = 商 * 20 + 1  # Double the current 商 and add 1
        法 = 借算  # Temporary divisor

        # Divide to determine the next digit of the side length
        次商 = 餘數 // 法

        # Update 商 and 餘數
        商 = 商 * 10 + 次商
        餘數 -= 次商 * 法

        # Update the fixed divisor
        定法 = 商 * 2

        # If the remainder becomes 0, break
        if 餘數 == 0:
            break

        # Adjust the divisor downward for the next iteration
        法 = 定法

    return 商

# Extract the square root of 積
a = 開方(積)
"""
Variable 'a' has wrong value. Expected: 159, Actual: 25280"""
