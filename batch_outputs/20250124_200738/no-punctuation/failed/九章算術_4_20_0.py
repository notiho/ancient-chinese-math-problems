"""
今有積六萬三千四百一尺五百一十二分尺之四百四十七問為立方幾何
開立方術曰置積為實借一算步之超二等議所得以再乘所借一算為法而除之除已三之為定法復除折而下以三乘所得數置中行復借一算置下行步之中超一下超二等復置議以一乘中再乘下皆副以加定法以定法除除已倍下并中從定法復除折下如前開之不盡者亦為不可開若積有分者通分內子為定實定實乃開之訖開其母以報除若母不可開者又以母再乘定實乃開之訖令如母而一
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a volume of 63,401 chi and 447/512 chi³.
Question: what is the cube root of this volume?

The procedure for extracting cube roots says:
1. Place the volume as the dividend (實).
2. Borrow one counting rod (算) and step it to exceed by two orders of magnitude (步之超二等). Discuss the result obtained.
3. Multiply the borrowed counting rod by itself, and multiply it again to form the divisor (法). Divide the dividend by this divisor.
4. After dividing, multiply the result by three to form the fixed divisor (定法). Subtract the remainder and bring it down.
5. Multiply the obtained number by three and place it in the middle row (中行). Borrow another counting rod and place it in the lower row (下行). Step it to exceed by one order of magnitude (超一下) and then by two orders of magnitude (超二等). Discuss again.
6. Multiply the middle row by the lower row, and multiply the lower row by itself. Add these results to the fixed divisor (定法).
7. Divide the dividend by the fixed divisor. After dividing, double the lower row and add it to the middle row. Use the fixed divisor to divide again, bringing down the remainder as before.
8. If the division does not terminate, the cube root cannot be extracted exactly.
9. If the volume has fractions, convert them into a common fraction and treat the numerator as the dividend (定實). Extract the cube root of the numerator. Then extract the cube root of the denominator and adjust accordingly. If the denominator cannot be extracted, multiply the numerator by the square of the denominator and extract the cube root.

Answer: *a* chi.
"""

from fractions import Fraction

# 積六萬三千四百一尺五百一十二分尺之四百四十七
積 = Fraction(63401 * 512 + 447, 512)

# Step 1: Initialize variables
實 = 積  # Dividend
商 = 0  # Quotient (cube root result)
餘 = 實  # Remainder

# Step 2: Iteratively extract the cube root
while True:
    # Borrow one counting rod and step it
    借 = 商 + 1
    法 = 借**2 * 3  # Compute the divisor

    # Check if the divisor exceeds the remainder
    if 法 > 餘:
        break

    # Perform the division
    餘 -= 法
    商 += 1

# 商 is the integer part of the cube root
整數部分 = 商

# Step 3: Handle fractional part if remainder exists
if 餘 > 0:
    # Convert the remainder into a fraction
    分子 = 餘.numerator
    分母 = 餘.denominator

    # Extract the cube root of the numerator and denominator
    分子立方根 = round(分子**(1/3))
    分母立方根 = round(分母**(1/3))

    # Adjust if the denominator cannot be exactly extracted
    if 分母立方根**3 != 分母:
        分子 *= 分母**2
        分母立方根 = 分母

    分數部分 = Fraction(分子立方根, 分母立方根)
else:
    分數部分 = 0

# Combine the integer and fractional parts
a = 整數部分 + 分數部分#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 319/8, Actual: 409/8"""
