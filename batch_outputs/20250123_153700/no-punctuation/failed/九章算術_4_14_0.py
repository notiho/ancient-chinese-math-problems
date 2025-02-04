"""
又有積五十六萬四千七百五十二步四分步之一問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

"""
Suppose there is an area of 564,752 and 1/4 bu². 
Question: what is the side length of the square field?

The procedure for square root extraction says:
1. Place the area as the dividend.
2. Borrow one counting rod for the side length, exceeding one rank. Discuss the result.
3. Multiply the borrowed counting rod by itself to form the divisor, and divide.
4. Double the divisor to form the fixed divisor.
5. Subtract and continue dividing, adjusting the divisor as necessary.
6. If the square root cannot be extracted exactly, it is considered "incompletely extractable," and the side length is expressed as a fraction.
7. If the area has fractional parts, convert them into a common denominator and include them in the calculation.
8. Extract the square root of the numerator and denominator separately. If the denominator cannot be extracted, multiply the numerator by the denominator and proceed as before.

Answer: *a* bu.
"""

from fractions import Fraction

# 置積為實
積 = Fraction(564752, 1) + Fraction(1, 4)

# 初始化
實 = 積
借算 = 0
面 = 0

# 開方術
while True:
    # 借一算步之超一等議所得
    借算 += 1
    所得 = 借算 ** 2
    if 所得 > 實:
        借算 -= 1
        break

# 以一乘所借一算為法
法 = 借算 * 2

# 以除除已倍法為定法
定法 = 法

# 復除折法而下
實 -= 借算 ** 2

# 繼續開方
while 實 > 0:
    # 借算步之如初
    借算 = 借算 * 10
    實 *= 100

    # 復議一乘之所得副
    所得 = 借算 * 2
    副 = 所得 // 定法

    # 加定法以除
    定法 = 定法 + 副

    # 更新實
    實 -= 副 * 定法

# 若開之不盡者為不可開
if 實 != 0:
    a = Fraction(借算, 定法)
else:
    a = 借算
"""
Code error: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit"""
