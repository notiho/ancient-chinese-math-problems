"""
今有積一百八十六萬八百六十七尺問為立方幾何
開立方術曰置積為實借一算步之超二等議所得以再乘所借一算為法而除之除已三之為定法復除折而下以三乘所得數置中行復借一算置下行步之中超一下超二等復置議以一乘中再乘下皆副以加定法以定法除除已倍下并中從定法復除折下如前開之不盡者亦為不可開若積有分者通分內子為定實定實乃開之訖開其母以報除若母不可開者又以母再乘定實乃開之訖令如母而一
荅曰 a尺 
"""

"""
Suppose there is a volume of 1,860,867 cubic chi.
Question: what is the side length of the cube?

The procedure for extracting the cube root says:
1. Place the volume as the dividend.
2. Borrow one counting rod and estimate the side length by trial, ensuring the cube of the estimate does not exceed the volume.
3. Multiply the estimate by itself, then multiply by 3, and use this as the divisor.
4. Divide the volume by the divisor to obtain the next digit of the side length.
5. Multiply the obtained digit by 3, and add it to the divisor for the next iteration.
6. Repeat the process until the volume is fully divided or it is determined that the cube root cannot be extracted exactly.
7. If the volume has a fractional part, convert it to a common fraction and proceed as above.
8. If the denominator of the fraction cannot be cube-rooted, multiply the numerator by the square of the denominator and proceed as above.

Answer: *a* chi.
"""

# 積一百八十六萬八百六十七尺
積 = 1860867

# Initialize variables
實 = 積
商 = 0  # The result (side length)
位 = 0  # Current digit position

# 開立方術
while 實 > 0:
    # Step 1: Borrow one counting rod and estimate the next digit
    借 = 1
    while (商 + 借) ** 3 <= 積:
        借 += 1
    借 -= 1  # Step back to the valid estimate

    # Step 2: Update the side length
    商 += 借 * (10 ** 位)

    # Step 3: Calculate the divisor
    定法 = 3 * (商 ** 2)

    # Step 4: Subtract the cube of the current estimate from the volume
    實 -= 借 * 定法 * (10 ** (2 * 位))

    # Step 5: Move to the next digit position
    位 += 1

# The result is the cube root
a = 商
"""
"""
