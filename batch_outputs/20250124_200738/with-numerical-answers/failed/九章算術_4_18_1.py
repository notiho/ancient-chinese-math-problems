"""
今有積一百八十六萬八百六十七尺。問︰為立方幾何？
開立方術曰：置積為實。借一算步之，超二等。議所得，以再乘所借一算為法，而除之。除已，三之為定法。復除，折而下。以三乘所得數置中行。復借一算置下行。步之，中超一，下超二等。復置議，以一乘中，再乘下，皆副以加定法。以定法除。除已，倍下、并中從定法。復除，折下如前。開之不盡者，亦為不可開。若積有分者，通分內子為定實。定實乃開之，訖，開其母以報除。若母不可開者，又以母再乘定實，乃開之。訖，令如母而一。
荅曰： a(=123)尺 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 1,860,867 cubic chi.
Question: what is the side length of the cube?

The procedure for extracting the cube root says:
Place the volume as the dividend. Borrow one counting rod and mark it, skipping two places. 
Estimate the result, and multiply the estimate by itself twice to form the divisor, then divide.
After dividing, multiply the result by 3 to form the fixed divisor. Divide again, and reduce the remainder.
Multiply the result by 3 and place it in the middle row. Borrow one counting rod and place it in the bottom row.
Mark it, skipping one place in the middle and two places in the bottom. Estimate again, and multiply the middle by 1 and the bottom by 2, adding these to the fixed divisor.
Divide by the fixed divisor. After dividing, double the bottom and add it to the middle to form the new fixed divisor. Divide again, and reduce the remainder as before.
If the root cannot be fully extracted, it is considered non-extractable. If the volume has fractions, convert the fractions into a common denominator and treat it as the dividend.
After extracting, also extract the cube root of the denominator. If the denominator cannot be extracted, multiply the denominator by itself twice and extract the cube root of the product. Finally, adjust the result to match the denominator.

Answer: *a*(=123) chi.
"""

from fractions import Fraction

# 置積為實
積 = 1860867

# 開立方術
def 開立方(積):
    # Initialize variables
    商 = 0
    餘 = 積
    位 = len(str(積)) // 3  # Determine the number of digits in groups of 3

    while 位 > 0:
        # 超二等 (skip two places)
        當前位 = int(str(餘)[:3]) if len(str(餘)) >= 3 else int(餘)

        # 議所得
        預估 = 0
        while (預估 + 1) ** 3 <= 當前位:
            預估 += 1

        # 再乘所借一算為法
        法 = 預估 ** 2 * 3

        # 除之
        商 = 商 * 10 + 預估
        餘 -= 預估 ** 3 * (10 ** (3 * (位 - 1)))

        # 折而下
        餘 = int(str(餘) + "000") if 位 > 1 else 餘
        位 -= 1

    return 商

# 計算立方根
a = 開立方(積)  # 123
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 123, Actual: 55"""
