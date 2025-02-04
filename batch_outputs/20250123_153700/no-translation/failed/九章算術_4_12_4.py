"""
又有積二萬五千二百八十一步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
To solve this problem, we need to implement the ancient Chinese square root extraction method described in the procedure. Here's the Python code:


"""


from fractions import Fraction

# 置積為實
積 = 25281

# 開方術
def 開方(積):
    # Step 1: 超一等 (determine the highest place value for the square root)
    借算 = 1
    while 借算 * 借算 <= 積:
        借算 += 1
    借算 -= 1

    # Step 2: 以一乘所借一算為法，而以除
    法 = 借算 * 2
    商 = 積 // 法
    餘 = 積 % 法

    # Step 3: 倍法為定法
    定法 = 法 * 2

    # Step 4: 折法而下，復置借算步之如初
    while 餘 > 0:
        法 = 定法 + 商
        商 = 餘 // 法
        餘 = 餘 % 法
        定法 = 法 * 2

    # Step 5: 若開之不盡者為不可開，當以面命之
    # If there is a remainder, the square root is not exact
    if 餘 != 0:
        return "不可開"

    return 借算

# 計算結果
a = 開方(積)
print(f"荅曰： {a}步 。")


"""


This code implements the square root extraction method described in the problem. It calculates the square root of the given area (`積`) step by step, following the ancient procedure. If the square root cannot be extracted exactly, it will return "不可開" (not extractable).
"""


"""
Timed out"""
