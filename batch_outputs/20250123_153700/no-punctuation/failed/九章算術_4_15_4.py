"""
又有積三十九億七千二百一十五萬六百二十五步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

"""
Suppose there is a volume of 3,970,215,625 bu³.
Question: what is the side length of the square field?

The procedure for square root extraction says: Place the volume as the dividend. Borrow one counting rod for the side length, exceeding one rank. Discuss what is obtained. Multiply it by 1, and use the borrowed counting rod as the divisor. Divide it. Double the divisor to form the fixed divisor. Subtract the remainder from the fixed divisor and bring it down. Borrow the counting rod again as before. Discuss what is obtained. Multiply it by 1, add it to the fixed divisor, and divide. Add the obtained result to the fixed divisor. Subtract the remainder and bring it down as before. If the square root cannot be fully extracted, it is considered unsolvable, and the side length is given as the result. If the dividend has fractions, convert them to a common denominator and treat the numerator as the dividend. Extract the square root of the numerator and denominator separately. If the denominator cannot be extracted, multiply the numerator by the denominator and extract the square root again. The result is given as the denominator and 1.

Answer: *a* bu.
"""

# 置積為實
積 = 3970215625

# 開方術
def 開方(實):
    # Initialize variables
    借算步 = 0
    定法 = 0
    剩餘 = 實
    開方結果 = 0

    while 剩餘 > 0:
        # Borrow one counting rod for the side length
        借算步 += 1
        法 = 借算步 * 1  # Multiply by 1 as per the procedure

        # Divide the remaining volume by the divisor
        if 剩餘 < 法:
            break  # If the remainder is less than the divisor, stop
        商 = 剩餘 // 法
        開方結果 = 商

        # Double the divisor to form the fixed divisor
        定法 = 2 * 法

        # Subtract the remainder and bring it down
        剩餘 -= 商 * 法

    return 開方結果

# 計算開方
a = 開方(積)
"""
Variable 'a' has wrong value. Expected: 63025, Actual: 3970215625"""
