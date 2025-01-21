"""
今有積一百八十六萬八百六十七尺問為立方幾何
開立方術曰置積為實借一算步之超二等議所得以再乘所借一算為法而除之除已三之為定法復除折而下以三乘所得數置中行復借一算置下行步之中超一下超二等復置議以一乘中再乘下皆副以加定法以定法除除已倍下并中從定法復除折下如前開之不盡者亦為不可開若積有分者通分內子為定實定實乃開之訖開其母以報除若母不可開者又以母再乘定實乃開之訖令如母而一
荅曰 a尺 
"""

"""
Suppose there is a volume of 1,860,867 cubic chi.
Question: what is the side length of the cube?

The procedure for extracting the cube root says: Place the volume as the dividend.
Borrow one counting rod, and step through the degrees of excess by 2.
Estimate the result, and multiply the borrowed counting rod by itself to form the divisor.
Divide by the divisor.
Multiply the result by 3 to form the fixed divisor.
Continue dividing, subtracting, and bringing down the next digit.
Multiply the result by 3, and place it in the middle row.
Borrow another counting rod, and place it in the bottom row.
Step through the degrees of excess by 1 and 2.
Estimate again, and multiply the middle row by the bottom row, then multiply by the bottom row again.
Add this to the fixed divisor.
Divide by the fixed divisor.
Continue as before, subtracting and bringing down digits.
If the division does not terminate, the cube root cannot be extracted exactly.
If the volume has fractions, convert them to a common denominator and treat the numerator as the dividend.
Extract the cube root of the numerator, and then extract the cube root of the denominator.
If the denominator cannot be extracted, multiply the numerator by the square of the denominator and extract the cube root of the result.

Answer: *a* chi.
"""

# 置積為實
積 = 1860867

# 開立方術
# Initialize variables
實 = 積
商 = 0  # The result (side length of the cube)
位 = 0  # Current digit position

# Step through the procedure
while 實 > 0:
    # Borrow one counting rod and step through degrees of excess
    借 = 1
    while (借 ** 3) <= 實:
        借 += 1
    借 -= 1

    # Update 商 and 位
    商 = 商 * 10 + 借
    位 += 1

    # Calculate the divisor and subtract
    定法 = 3 * (商 ** 2)
    實 -= 借 ** 3

    # Bring down the next digit (if any)
    實 *= 10 ** 3

# Final result
a = 商
"""
"""
