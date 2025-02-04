"""
又有積三十九億七千二百一十五萬六百二十五步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
This is a classic square root extraction problem from ancient Chinese mathematics. The procedure described is essentially a manual method for extracting the square root of a number, which involves iterative approximation and refinement. Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# 積三十九億七千二百一十五萬六百二十五步
積 = 3972150625

# 開方術
def 開方(積):
    # 置積為實
    實 = 積

    # 借一算步之，超一等
    借算 = 0
    while (借算 + 1) ** 2 <= 實:
        借算 += 1

    # 議所得，以一乘所借一算為法，而以除
    法 = 借算 * 2
    商 = 實 // 借算

    # 除已，倍法為定法
    定法 = 法 * 2

    # 其復除。折法而下
    餘數 = 實 - 商 * 借算

    # 復置借算步之如初，以復議一乘之
    while 餘數 > 0:
        借算 = 0
        while (借算 + 1) ** 2 <= 餘數:
            借算 += 1

        # 所得副，以加定法，以除
        副 = 借算
        定法 += 副
        商 = 餘數 // 定法

        # 以所得副從定法。復除折下如前
        餘數 = 餘數 - 商 * 定法

    # 若開之不盡者為不可開，當以面命之
    if 餘數 != 0:
        return "不可開"

    # 若實有分者，通分內子為定實
    # (This part is not applicable here as the input is an integer.)

    # 荅曰：a步
    return 借算

a = 開方(積)
print(f"荅曰：{a}步。")


"""


### Explanation of the Code:
1. **Initialization**: The given number (`積`) is set as the starting value (`實`).
2. **Iterative Approximation**: The algorithm iteratively finds the largest possible value of `借算` such that its square is less than or equal to the current value of `實`.
3. **Division and Refinement**: The procedure refines the divisor (`法`) and calculates the quotient (`商`) and remainder (`餘數`).
4. **Repeat Until Exact**: The process repeats until the remainder becomes zero, indicating that the square root has been fully extracted.
5. **Handle Non-Perfect Squares**: If the remainder is not zero, the algorithm concludes that the square root cannot be exactly extracted.

### Note:
This implementation assumes that the input (`積`) is a perfect square. If the input is not a perfect square, the algorithm will return "不可開" (cannot be opened). If fractional results are needed, additional steps for handling fractions would be required.
"""


"""
"""
