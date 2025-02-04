"""
又有積五十六萬四千七百五十二步四分步之一問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is an area of 564,752 and 1/4 bu².
Question: what is the side length of the square field?

The procedure for square root extraction says: Place the area as the dividend.
Borrow one counting rod for the side length, exceeding one place value.
Estimate the result. Multiply the estimate by 1, and use it as the divisor.
Divide the dividend by the divisor. Double the divisor to set the fixed divisor.
Repeat the division, adjusting the divisor as necessary, and continue until the square root is fully extracted.
If the square root cannot be fully extracted, it is considered "inextractable," and the side length is expressed as an approximation.
If the area has fractions, convert them to a common denominator and treat them as integers for the calculation.
After extraction, divide the result by the denominator.
If the denominator itself cannot be square-rooted, multiply the denominator by the area, extract the square root, and adjust the result accordingly.

Answer: *a* bu.
"""

from fractions import Fraction

# 積五十六萬四千七百五十二步四分步之一
積 = Fraction(564752, 1) + Fraction(1, 4)

# 通分內子為定實
分母 = 積.denominator
定實 = 積.numerator

# 開方術
def 開方(實):
    # Initialize variables
    借算 = 0
    定法 = 0
    剩餘 = 實
    開根 = 0

    while 剩餘 > 0:
        # Borrow one place value
        借算 += 1
        超一等 = 10 ** 借算

        # Estimate the next digit
        for i in range(10):
            if (開根 * 20 + i) * i > 剩餘:
                所得 = i - 1
                break
        else:
            所得 = 9

        # Update the root and divisor
        開根 = 開根 * 10 + 所得
        定法 = 開根 * 2

        # Subtract the square of the current estimate
        剩餘 -= (開根 * 10 + 所得) * 所得

        # If the remainder is zero, break
        if 剩餘 == 0:
            break

    return 開根

# 開定實的平方根
平方根 = 開方(定實)

# 若分母不可開，調整結果
if 分母 != 1:
    分母平方根 = 開方(分母)
    if 分母平方根 ** 2 != 分母:
        分母平方根 = 開方(分母 * 定實)
        平方根 = 分母平方根

# 報除
a = Fraction(平方根, 分母)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1503/2, Actual: 24999"""
