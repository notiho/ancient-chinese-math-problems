"""
又有積二萬五千二百八十一步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
To solve this problem, we need to implement the ancient Chinese square root extraction method ("開方術"). Here's the Python code that follows the procedure step by step:


"""

#----- content starts here -----

from fractions import Fraction

# 置積為實
積 = 25281

# 開方術
def 開方(積):
    # Step 1: 借一算步之，超一等
    借算 = 1
    while 借算 ** 2 <= 積:
        借算 += 1
    借算 -= 1  # Step back to the last valid 借算

    # Step 2: 以一乘所借一算為法，而以除
    法 = 借算 * 2
    餘 = 積 - 借算 ** 2

    # Step 3: 倍法為定法
    定法 = 法 * 2

    # Step 4: 復除，折法而下
    while 餘 > 0:
        # 復置借算步之如初，以復議一乘之
        副 = 1
        while (定法 + 副) * 副 <= 餘:
            副 += 1
        副 -= 1  # Step back to the last valid 副

        # 所得副，以加定法，以除
        定法 += 副
        餘 -= 定法 * 副

        # 復除折下如前
        定法 += 副

    # 若開之不盡者為不可開，當以面命之
    if 餘 != 0:
        return "不可開"

    # 若實有分者，通分內子為定實
    return 借算

# Calculate the result
a = 開方(積)
print(f"a步 = {a}")
#----- content ends here -----


"""


This code implements the ancient procedure for extracting the square root of a number. It follows the steps described in the "開方術" text. If the square root cannot be extracted exactly, it will return "不可開" (not extractable). If it can be extracted, it will return the result as `a步`.
"""


"""
"""
