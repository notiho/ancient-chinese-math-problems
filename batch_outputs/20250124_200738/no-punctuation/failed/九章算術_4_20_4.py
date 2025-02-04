"""
今有積六萬三千四百一尺五百一十二分尺之四百四十七問為立方幾何
開立方術曰置積為實借一算步之超二等議所得以再乘所借一算為法而除之除已三之為定法復除折而下以三乘所得數置中行復借一算置下行步之中超一下超二等復置議以一乘中再乘下皆副以加定法以定法除除已倍下并中從定法復除折下如前開之不盡者亦為不可開若積有分者通分內子為定實定實乃開之訖開其母以報除若母不可開者又以母再乘定實乃開之訖令如母而一
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a volume of 63401 chi and 447/512 chi³.
Question: what is the cube root of this volume?

The procedure for extracting cube roots says:
1. Place the volume as the dividend.
2. Borrow one counting rod and step it to the second position (i.e., divide the number into groups of three digits from right to left).
3. Discuss the largest number whose cube is less than or equal to the first group, and place this number as the quotient.
4. Multiply the quotient by itself and then by the borrowed counting rod to form the divisor.
5. Divide the dividend by the divisor, and the result is the preliminary quotient.
6. Multiply the preliminary quotient by 3 to form the fixed divisor.
7. Subtract the result from the dividend and bring down the next group of digits.
8. Multiply the preliminary quotient by 3 and place it in the middle row.
9. Borrow another counting rod and step it to the next position.
10. Repeat the process as before, adjusting the divisor and quotient iteratively.
11. If the volume has fractions, convert it to a common fraction and treat it as the dividend.
12. Extract the cube root of the numerator and denominator separately.
13. If the denominator is not a perfect cube, multiply it by itself and the numerator, then extract the cube root again.

Answer: *a* chi.
"""

from fractions import Fraction

# 積六萬三千四百一尺五百一十二分尺之四百四十七
積 = Fraction(63401 * 512 + 447, 512)

# 開立方術
def 開立方(積):
    # 通分內子為定實
    定實 = 積

    # 初始值
    商 = 0
    商步 = 1
    while 商步 ** 3 <= 定實:
        商 = 商步
        商步 += 1

    # 初步商
    商 -= 1

    # 開其母以報除
    return 商

# 計算立方根
a = 開立方(積)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 319/8, Actual: 38"""
