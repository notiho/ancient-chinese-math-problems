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
2. Borrow one counting rod, and step it down by two orders of magnitude to estimate the result.
3. Multiply the borrowed counting rod by itself, and use it as the divisor.
4. Divide the dividend by the divisor, and multiply the result by 3 to establish the fixed divisor.
5. Subtract the result of the division, and bring down the next digit.
6. Multiply the obtained number by 3, and place it in the middle row.
7. Borrow another counting rod, and place it in the lower row, stepping it down by one order of magnitude.
8. Repeat the estimation process, multiplying the middle row by the lower row, and adding it to the fixed divisor.
9. Divide the dividend by the updated divisor, and repeat the process until the cube root is fully extracted.
10. If the division does not terminate, the cube root cannot be extracted exactly.
11. If the volume has a fractional part, convert it into a common fraction and proceed as above.
12. If the denominator of the fraction cannot be cube-rooted, multiply the numerator by the square of the denominator and proceed as above.

Answer: *a* chi.
"""

# Define the volume
積 = 1860867

# Initialize variables
商 = 0  # The result (side length of the cube)
餘 = 積  # Remainder after each step
位 = 0  # Current digit position

# 開立方術
while True:
    # Step 1: Borrow one counting rod, step down by two orders of magnitude
    借 = 1
    while (借 + 1) ** 3 <= 餘:
        借 += 1

    # Step 2: Update 商 and 餘
    商 = 商 * 10 + 借  # Add the borrowed digit to the 商
    餘 -= 借 ** 3  # Subtract the cube of the borrowed digit from the remainder

    # Step 3: Check if the remainder is zero
    if 餘 == 0:
        break

    # Step 4: Bring down the next digit (simulate by multiplying remainder by 1000)
    餘 *= 1000
    位 += 1

# The result is the 商
a = 商
"""
"""
