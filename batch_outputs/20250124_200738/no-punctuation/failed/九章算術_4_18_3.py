"""
今有積一百八十六萬八百六十七尺問為立方幾何
開立方術曰置積為實借一算步之超二等議所得以再乘所借一算為法而除之除已三之為定法復除折而下以三乘所得數置中行復借一算置下行步之中超一下超二等復置議以一乘中再乘下皆副以加定法以定法除除已倍下并中從定法復除折下如前開之不盡者亦為不可開若積有分者通分內子為定實定實乃開之訖開其母以報除若母不可開者又以母再乘定實乃開之訖令如母而一
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a volume of 1,860,867 cubic chi.
Question: how many chi is the cube root of this volume?

The procedure for extracting the cube root says:
1. Place the volume as the dividend.
2. Borrow one counting rod and step it, exceeding by two ranks. Discuss the result.
3. Multiply the borrowed counting rod by itself, obtaining the divisor.
4. Divide the dividend by the divisor. After dividing, multiply the result by 3, obtaining the fixed divisor.
5. Subtract the result from the dividend, and bring down the next digit.
6. Multiply the result by 3, placing it in the middle row.
7. Borrow one counting rod and place it in the lower row. Step it, exceeding by one rank, then exceeding by two ranks. Discuss the result.
8. Multiply the middle row by the lower row, then multiply the lower row by itself. Add these to the fixed divisor.
9. Divide the new dividend by the updated divisor. After dividing, double the lower row and add it to the middle row.
10. Repeat the process, subtracting, bringing down digits, and updating the divisor until the cube root is fully extracted.
11. If the volume cannot be fully extracted, it is considered not extractable.
12. If the volume has fractions, convert them to a common denominator and treat the numerator as the dividend. Extract the cube root of the numerator and denominator separately. If the denominator cannot be extracted, multiply it by itself and proceed as before.

Answer: *a* chi.
"""

from fractions import Fraction

# Initial volume
積 = 1860867

# Step 1: Place the volume as the dividend
實 = 積

# Initialize variables
商 = 0  # Cube root result
定法 = 0  # Fixed divisor

# Step 2: Borrow one counting rod and step it, exceeding by two ranks
while 實 > 0:
    # Step 3: Multiply the borrowed counting rod by itself, obtaining the divisor
    法 = (3 * 商**2 + 3 * 商 + 1)

    # Step 4: Divide the dividend by the divisor
    商下一位 = 實 // 法

    # Step 5: Subtract the result from the dividend, and bring down the next digit
    實 -= 法 * 商下一位

    # Update 商
    商 = 商 * 10 + 商下一位

# Final result
a = 商#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 123, Actual: 1860867"""
