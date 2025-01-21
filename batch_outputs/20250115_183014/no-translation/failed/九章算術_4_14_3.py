"""
又有積五十六萬四千七百五十二步、四分步之一。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
This problem involves finding the square root of a number using an ancient Chinese method described in the "開方術" (square root extraction procedure). Here's the Python implementation of the procedure:


"""


from fractions import Fraction

# 置積為實
積 = Fraction(564752, 4)  # 五十六萬四千七百五十二步、四分步之一

# 借一算步之，超一等
借算 = 1
超等 = 0
while 借算 * 借算 <= 積:
    借算 *= 10
    超等 += 1
借算 //= 10
超等 -= 1

# 議所得，以一乘所借一算為法，而以除
法 = 2 * 借算
商 = 積 // 法

# 除已，倍法為定法
定法 = 2 * 商

# 其復除。折法而下
餘 = 積 - 商 * 法
折法 = 定法 // 2

# 復置借算步之如初，以復議一乘之，所得副，以加定法，以除
while 餘 > 0 and 折法 > 0:
    副 = 餘 // 折法
    定法 += 副
    餘 -= 副 * 折法
    折法 //= 2

# 若開之不盡者為不可開，當以面命之
if 餘 > 0:
    print("不可開")
else:
    a = 定法
    print(f"荅曰：{a}步。")


"""


This code follows the ancient Chinese method for extracting square roots. It iteratively refines the approximation of the square root by adjusting the divisor (`法`) and the remainder (`餘`). If the square root cannot be fully extracted (i.e., there is a remainder), it is declared "不可開" (not extractable). Otherwise, the result is returned as `a`.
"""


"""
Variable 'a' has wrong value. Expected: 1503/2, Actual: 1413"""
