"""
又有積五十六萬四千七百五十二步四分步之一問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is an area of 564,752 and 1/4 bu². 
Question: what is the side length of the square field?

The procedure for square root extraction says:
Place the area as the dividend. Borrow one counting rod for the side length, exceeding one rank. 
Estimate the result. Multiply the estimate by 1, and use it as the divisor. Divide the dividend by the divisor.
Double the divisor to determine the fixed divisor. Continue dividing, adjusting the divisor as needed.
If the square root cannot be fully extracted, it is considered unsolvable, and the result should be expressed in terms of the side length.
If the area has fractions, convert it into a single fraction and treat it as the new dividend. Extract the square root of the numerator and denominator separately.
If the denominator cannot be square-rooted, multiply the numerator by the denominator and extract the square root again.

Answer: *a* bu.
"""

from fractions import Fraction

# 積五十六萬四千七百五十二步四分步之一
積 = Fraction(564752, 1) + Fraction(1, 4)

# 開方術
def 開方(積):
    # 通分內子為定實
    定實 = 積

    # 開平方根
    def 開平方根(數):
        # 逐步逼近平方根
        根 = 0
        while 根 * 根 <= 數:
            根 += 1
        根 -= 1
        return 根

    # 開分子平方根
    分子平方根 = 開平方根(定實.numerator)

    # 開分母平方根
    分母平方根 = 開平方根(定實.denominator)

    # 若分母不可開，重新處理
    if 分母平方根 * 分母平方根 != 定實.denominator:
        分子平方根 = 開平方根(定實.numerator * 定實.denominator)
        分母平方根 = 定實.denominator

    # 返回結果
    return Fraction(分子平方根, 分母平方根)

# 計算結果
a = 開方(積)
#----- content ends here -----

"""
"""
