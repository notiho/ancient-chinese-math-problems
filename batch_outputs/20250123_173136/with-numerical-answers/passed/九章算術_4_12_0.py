"""
又有積二萬五千二百八十一步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=159)步 。
"""

"""
Suppose there is a volume of 25281 bu. 
Question: what is the side length of the square field?

The procedure for square root extraction says: Place the volume as the dividend. Borrow one counting rod and place it, skipping one position. 
Estimate the result, and multiply the estimate by itself to form the divisor, then divide. After dividing, double the divisor to form the fixed divisor. Divide again, reducing the divisor step by step. 
Place the borrowed counting rod as before, and estimate again, multiplying the estimate by itself to form the auxiliary value. Add this to the fixed divisor and divide. Subtract the auxiliary value from the fixed divisor and continue dividing as before. 
If the root cannot be fully extracted, it is considered unsolvable, and the side length is expressed as a fraction. 
If the volume has a fractional part, convert it into a common fraction and extract the root. Afterward, extract the root of the denominator and report the result. If the denominator cannot be extracted, multiply the numerator by the denominator and extract the root, ensuring the result is expressed as a fraction.

Answer: *a*(=159) bu.
"""

# 置積為實
實 = 25281

# 開方術
def 開方(實):
    # 初始值
    借算 = 0
    while (借算 + 1) ** 2 <= 實:
        借算 += 1

    # 初步結果
    定法 = 借算
    餘數 = 實 - 借算 ** 2

    # 若餘數為 0，直接返回
    if 餘數 == 0:
        return 定法

    # 若餘數不為 0，進一步處理
    while 餘數 > 0:
        # 倍法為定法
        定法 *= 2

        # 折法而下
        折法 = 0
        while (定法 + 折法 + 1) * (折法 + 1) <= 實:
            折法 += 1

        # 更新定法和餘數
        定法 += 折法
        餘數 = 實 - 定法 ** 2

    return 定法

# 計算結果
a = 開方(實) # 159
"""
"""
