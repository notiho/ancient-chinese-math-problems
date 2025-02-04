"""
今有積六萬三千四百一尺五百一十二分尺之四百四十七問為立方幾何
開立方術曰置積為實借一算步之超二等議所得以再乘所借一算為法而除之除已三之為定法復除折而下以三乘所得數置中行復借一算置下行步之中超一下超二等復置議以一乘中再乘下皆副以加定法以定法除除已倍下并中從定法復除折下如前開之不盡者亦為不可開若積有分者通分內子為定實定實乃開之訖開其母以報除若母不可開者又以母再乘定實乃開之訖令如母而一
荅曰 a尺 
"""

"""
Suppose there is a volume of 63,401 chi and 447/512 chi³.
Question: what is the cube root of this volume?

The procedure for extracting cube roots says:
1. Place the volume as the dividend.
2. Borrow one counting rod, and step through the digits, skipping two places each time. Discuss the resulting number.
3. Multiply the borrowed counting rod by itself, and then multiply by 2, to form the divisor.
4. Divide the dividend by the divisor. After dividing, multiply the result by 3 to form the fixed divisor.
5. Subtract the result, and bring down the next digits.
6. Multiply the result by 3, and place it in the middle row. Borrow one counting rod again, and place it in the bottom row. Step through the middle row, skipping one place, and skipping two places in the bottom row.
7. Discuss the resulting number. Multiply the middle row by 1, and then multiply the bottom row by itself. Add these to the fixed divisor.
8. Divide by the fixed divisor. After dividing, double the bottom row, add it to the middle row, and divide by the fixed divisor again. Subtract the result, and bring down the next digits as before.
9. If the division does not terminate, the root cannot be extracted exactly.
10. If the volume has fractions, convert the entire volume into a single fraction as the dividend. Extract the cube root of the numerator and denominator separately. If the denominator cannot be extracted, multiply the denominator by itself and the numerator, and extract the cube root again.

Answer: *a* chi.
"""

from fractions import Fraction

# 積六萬三千四百一尺五百一十二分尺之四百四十七
積 = Fraction(63401) + Fraction(447, 512)

# 通分內子為定實
定實 = 積

# 開立方
def 開立方(定實):
    # 初始值
    商 = 0
    剩餘 = 定實
    位數 = 0

    # 確定初始位數
    while 剩餘 >= 1:
        剩餘 /= 10
        位數 += 1

    # 開始逐位開立方
    剩餘 = 定實
    while 位數 > 0:
        位數 -= 3  # 每次處理三位數
        商 += 1
        if 商 ** 3 > 定實:
            商 -= 1
            break

    return 商

# 計算結果
a = 開立方(定實)
"""
Variable 'a' has wrong value. Expected: 319/8, Actual: 2"""
