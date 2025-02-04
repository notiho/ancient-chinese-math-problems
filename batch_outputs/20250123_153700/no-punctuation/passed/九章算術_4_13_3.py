"""
又有積七萬一千八百二十四步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

"""
Suppose there is an area of 71824 bu².
Question: what is the side length of the square field?

The procedure for square root extraction says: Place the area as the dividend. Borrow one counting rod to represent the side length, exceeding one place value. Estimate the result. Multiply the borrowed counting rod by itself to form the divisor, and divide. Double the divisor to form the fixed divisor. Continue dividing, reducing the divisor as necessary. Place the borrowed counting rod again as before, and repeat the process. Multiply the estimate by itself, add it to the fixed divisor, and divide. If the square root cannot be exact, the result is incomplete and should be expressed as a fractional side length. If the area has a fractional part, convert it to a common fraction and proceed. If the denominator cannot be square-rooted, multiply the numerator by the denominator and proceed as before.

Answer: *a* bu.
"""

# 置積為實
實 = 71824

# 開方術
def 開方(實):
    # Initialize variables
    借算步 = 0
    定法 = 0
    副 = 0
    while True:
        # 議所得
        所得 = 0
        while (借算步 + 1) ** 2 <= 實:
            借算步 += 1
        所得 = 借算步

        # 所借一算為法
        法 = 所得 ** 2

        # 以除
        剩餘 = 實 - 法

        # 已倍法為定法
        定法 = 2 * 所得

        # 若開之不盡者
        if 剩餘 == 0:
            return 所得

        # 若實有分者
        if 剩餘 < 0:
            break

# Calculate the square root
a = 開方(實)
"""
"""
