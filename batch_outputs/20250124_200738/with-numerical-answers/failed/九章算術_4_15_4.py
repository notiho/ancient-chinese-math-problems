"""
又有積三十九億七千二百一十五萬六百二十五步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=63025)步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 3,970,215,625 bu. 
Question: what is the side length of the square (cube root)?

The procedure for extracting the square root says: Place the volume as the dividend. Borrow one counting rod, placing it, skipping one position. 
Estimate the result. Multiply the borrowed counting rod by 1 to form the divisor, and divide. After dividing, double the divisor to form the fixed divisor. Divide again. Reduce the divisor and continue. 
Place the borrowed counting rod as before, multiply it by the estimated result, and add it to the fixed divisor. Divide again. Subtract the result from the fixed divisor and continue dividing as before. 
If the root cannot be fully extracted, it is considered unsolvable, and the result should be expressed as the area. 
If the dividend has fractions, convert the fractions to a common denominator for the dividend. Then extract the root, and after completing the process, extract the root of the denominator. If the denominator cannot be extracted, multiply the denominator by the dividend and extract the root again, ensuring the result matches the denominator.

Answer: *a*(=63025) bu.
"""

from fractions import Fraction

# 置積為實
積 = 3970215625

# 開方術
def 開平方(積):
    # 初始值
    實 = 積
    借算 = 0
    根 = 0
    while 實 > 0:
        # 借一算步之，超一等
        借算 = 實 // (10 ** (len(str(實)) // 2))
        實 -= 借算 ** 2
        根 = 借算
        break
    return 根

# 計算結果
a = 開平方(積) # 63025#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 63025, Actual: 39702"""
