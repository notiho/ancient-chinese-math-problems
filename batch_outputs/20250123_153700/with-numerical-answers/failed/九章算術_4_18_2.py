"""
今有積一百八十六萬八百六十七尺。問︰為立方幾何？
開立方術曰：置積為實。借一算步之，超二等。議所得，以再乘所借一算為法，而除之。除已，三之為定法。復除，折而下。以三乘所得數置中行。復借一算置下行。步之，中超一，下超二等。復置議，以一乘中，再乘下，皆副以加定法。以定法除。除已，倍下、并中從定法。復除，折下如前。開之不盡者，亦為不可開。若積有分者，通分內子為定實。定實乃開之，訖，開其母以報除。若母不可開者，又以母再乘定實，乃開之。訖，令如母而一。
荅曰： a(=123)尺 。
"""

"""
Suppose there is a volume of 1,860,867 cubic chi.
Question: what is the side length of the cube?

The procedure for extracting the cube root says:
1. Place the volume as the dividend.
2. Borrow one counting rod, step it, and skip two places.
3. Estimate the result, and multiply the estimate by itself twice to form the divisor, then divide.
4. After dividing, multiply the result by 3 to form the fixed divisor.
5. Divide again, truncate the remainder, and bring it down.
6. Multiply the result by 3 and place it in the middle row.
7. Borrow one counting rod and place it in the lower row.
8. Step it, skip one place in the middle row, and skip two places in the lower row.
9. Place the estimate again, multiply the middle row by 1 and the lower row by 2, add these to the fixed divisor.
10. Divide by the fixed divisor.
11. After dividing, double the lower row and add it to the middle row to form the new fixed divisor.
12. Divide again, truncate the remainder as before.
13. If the division does not terminate, the root cannot be extracted exactly.
14. If the volume has a fractional part, convert it to a common fraction and treat it as the dividend.
15. Extract the root of the numerator, then extract the root of the denominator.
16. If the denominator cannot be extracted, multiply the denominator by itself twice and treat it as the new dividend, then extract the root.
17. Ensure the result is in the same unit as the denominator.

Answer: *a*(=123) chi.
"""

from fractions import Fraction

# 置積為實
實 = 1860867

# 開立方術
def 開立方(實):
    # Initialize variables
    商 = 0
    餘 = 實
    位 = len(str(實)) // 3  # Determine the number of groups of three digits

    while 位 > 0:
        # Step 1: Extract the first group of three digits
        當前 = int(str(餘)[:3])
        餘 = int(str(餘)[3:]) if len(str(餘)) > 3 else 0

        # Step 2: Estimate the root for the current group
        根 = 0
        while (根 + 1) ** 3 <= 當前:
            根 += 1

        # Step 3: Update 商 and 餘
        商 = 商 * 10 + 根
        當前 -= 根 ** 3
        餘 = 當前 * 1000 + 餘

        # Reduce 位
        位 -= 1

    return 商

# 計算立方根
a = 開立方(實)  # 123 chi
"""
Variable 'a' has wrong value. Expected: 123, Actual: 58"""
