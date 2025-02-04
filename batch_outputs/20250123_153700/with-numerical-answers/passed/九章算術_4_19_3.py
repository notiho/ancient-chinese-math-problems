"""
今有積一千九百五十三尺、八分尺之一。問︰為立方幾何？
開立方術曰：置積為實。借一算步之，超二等。議所得，以再乘所借一算為法，而除之。除已，三之為定法。復除，折而下。以三乘所得數置中行。復借一算置下行。步之，中超一，下超二等。復置議，以一乘中，再乘下，皆副以加定法。以定法除。除已，倍下、并中從定法。復除，折下如前。開之不盡者，亦為不可開。若積有分者，通分內子為定實。定實乃開之，訖，開其母以報除。若母不可開者，又以母再乘定實，乃開之。訖，令如母而一。
荅曰： a(=25/2)尺 。
"""

"""
Suppose there is a volume of 1953 and 1/8 chi³.
Question: what is the side length of the cube?

The procedure for extracting the cube root says: Place the volume as the dividend. Borrow one counting rod, stepping it, skipping two places. Evaluate the result. Multiply the borrowed counting rod by itself, obtaining the divisor, and divide by it. After dividing, multiply by 3 to obtain the fixed divisor. Divide again, and reduce as before. Multiply the result by 3 and place it in the middle row. Borrow one counting rod again and place it in the bottom row. Step it, skipping one place in the middle and two places in the bottom. Place the evaluation again. Multiply the middle by 1 and the bottom by 2, adding them to the fixed divisor. Divide by the fixed divisor. After dividing, double the bottom and add it to the middle to form the fixed divisor. Divide again, reducing as before. If the cube root cannot be fully extracted, it is considered unsolvable. If the volume has fractions, convert the numerator and denominator into integers as the fixed dividend. Extract the cube root of the numerator, and then extract the cube root of the denominator. If the denominator cannot be extracted, multiply the denominator by itself and the fixed dividend, and then extract the cube root. Finally, adjust the result to match the denominator.

Answer: *a*(=25/2) chi.
"""

from fractions import Fraction

# 積一千九百五十三尺、八分尺之一
積 = Fraction(1953) + Fraction(1, 8)

# 通分內子為定實
定實 = 積

# 開立方
# 開其母以報除
母 = 定實.denominator
子 = 定實.numerator

# 開子
子立方根 = round(子 ** (1 / 3))

# 開母
母立方根 = round(母 ** (1 / 3))

# 若母不可開者，又以母再乘定實，乃開之
if 母立方根 ** 3 != 母:
    母 = 母 * 母
    定實 = 子 * 母
    子立方根 = round(定實 ** (1 / 3))
    母立方根 = round(母 ** (1 / 3))

# 計算結果
a = Fraction(子立方根, 母立方根)  # 25/2

"""
"""
