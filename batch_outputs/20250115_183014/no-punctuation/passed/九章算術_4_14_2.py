"""
又有積五十六萬四千七百五十二步四分步之一問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

"""
Suppose there is an area of 564,752 and 1/4 bu². 
Question: what is the side length of the square field?

The procedure for square root extraction says:
1. Place the given area as the dividend.
2. Borrow a counting rod for the side length, exceeding by one digit. Estimate the result.
3. Multiply the borrowed counting rod by itself to form the divisor, and divide the dividend by this divisor.
4. Double the divisor to form the fixed divisor.
5. Subtract the result of the division from the dividend, and continue the process by reducing the divisor.
6. Place the borrowed counting rod again, as before, and repeat the process.
7. If the square root cannot be extracted exactly, the result is not a perfect square, and the side length should be expressed as a fraction.
8. If the area has a fractional part, convert it to a common fraction and include it in the calculation.
9. Extract the square root of the numerator and denominator separately. If the denominator cannot be extracted, multiply the numerator by the denominator and extract the square root.

The answer says: *a* bu.
"""

from fractions import Fraction

# 積五十六萬四千七百五十二步四分步之一
積 = Fraction(564752, 1) + Fraction(1, 4)

# 開方術
def 開方(積):
    # Step 1: Place the given area as the dividend
    實 = 積

    # Step 2: Borrow a counting rod for the side length, exceeding by one digit
    借算 = 1
    while 借算 * 借算 <= 實:
        借算 += 1
    借算 -= 1

    # Step 3: Multiply the borrowed counting rod by itself to form the divisor
    法 = 借算 * 借算

    # Step 4: Divide the dividend by this divisor
    商 = 實 // 法

    # Step 5: Double the divisor to form the fixed divisor
    定法 = 2 * 借算

    # Step 6: Subtract the result of the division from the dividend
    餘 = 實 - 商 * 法

    # Step 7: If the square root cannot be extracted exactly
    if 餘 != 0:
        # Step 8: Convert the area to a common fraction
        分子 = 積.numerator
        分母 = 積.denominator

        # Step 9: Extract the square root of the numerator and denominator
        分子開方 = int(分子**0.5)
        分母開方 = int(分母**0.5)

        if 分子開方**2 == 分子 and 分母開方**2 == 分母:
            return Fraction(分子開方, 分母開方)
        else:
            分子 = 分子 * 分母
            分母 = 分母 * 分母
            分子開方 = int(分子**0.5)
            if 分子開方**2 == 分子:
                return Fraction(分子開方, 分母)
            else:
                return "不可開"

    return 商

# 計算結果
a = 開方(積)
"""
"""
