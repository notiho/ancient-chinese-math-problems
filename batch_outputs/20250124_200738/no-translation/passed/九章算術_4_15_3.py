"""
又有積三十九億七千二百一十五萬六百二十五步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
This is a classic square root extraction problem from ancient Chinese mathematics. The procedure described is essentially a manual method for calculating the square root of a number. Below is the Python implementation of the procedure:


"""

#----- content starts here -----

from fractions import Fraction

# 置積為實
積 = 3972150625

# 開方術
def 開方(積):
    # 初始值
    借算步 = 0
    while (借算步 + 1) ** 2 <= 積:
        借算步 += 1

    # 初步所得
    定法 = 借算步
    剩餘 = 積 - 借算步 ** 2

    # 若開之不盡者，當以面命之
    if 剩餘 == 0:
        return 借算步  # 完全平方數

    # 若實有分者，通分內子為定實
    分子 = 剩餘
    分母 = 2 * 借算步

    # 通分內子
    定實 = Fraction(分子, 分母)

    # 開其母報除
    母 = 定實.denominator
    子 = 定實.numerator

    # 若母不可開者，又以母乘定實，乃開之
    母平方根 = int(母 ** 0.5)
    if 母平方根 ** 2 != 母:
        子 *= 母
        母平方根 = int(母 ** 0.5)

    # 最終結果
    return 借算步 + Fraction(子, 母平方根)

# 計算結果
a = 開方(積)
print(f"a步 = {a}")
#----- content ends here -----


"""


### Explanation:
1. **Initial Setup**: The problem starts by determining the largest integer (`借算步`) whose square is less than or equal to the given number (`積`).
2. **Exact Square Check**: If the number is a perfect square, the square root is returned directly.
3. **Fractional Part**: If the number is not a perfect square, the remaining part (`剩餘`) is used to calculate the fractional part of the square root.
4. **Simplification**: The fractional part is simplified and, if necessary, adjusted to ensure the denominator is a perfect square.
5. **Final Result**: The integer part and the fractional part are combined to give the final square root.

### Example Output:
For the given input `積 = 3972150625`, the output will be the square root in terms of steps (`a步`).
"""


"""
"""
