"""
又有積二萬五千二百八十一步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=159)步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 25281 bu. Question: what is the side length of the square field?

The procedure for extracting square roots says: Place the area as the dividend. Borrow one counting rod to represent the side length, skipping one place (digit). Estimate the result. Multiply the borrowed counting rod by itself to form the divisor, and divide. After dividing, double the divisor to form the "fixed divisor." Divide again. Subtract the divisor and continue. Place the borrowed counting rod again as before, and estimate again. Multiply the result by itself to form the auxiliary value, add it to the fixed divisor, and divide. Subtract the auxiliary value from the fixed divisor and continue dividing as before. If the square root cannot be exact, it is considered "inextractable," and the result should be expressed as a side length with a remainder. If the area has fractions, convert the fractions to a common denominator and treat them as integers. Extract the square root of the numerator, and then extract the square root of the denominator. If the denominator cannot be extracted, multiply the numerator by the denominator and extract the square root of the product.

Answer: *a*(=159) bu.
"""

# 置積為實
積 = 25281

# 開方術
def 開方(積):
    # 初始值
    借算 = 0
    while (借算 + 1) ** 2 <= 積:
        借算 += 1

    # 初步結果
    定法 = 借算
    餘數 = 積 - 借算 ** 2

    # 若有餘數，繼續處理
    while 餘數 > 0:
        # 倍法為定法
        定法 *= 2

        # 復議一乘之
        借算 = 0
        while (定法 + 借算 + 1) * (借算 + 1) <= 積:
            借算 += 1

        # 更新定法與餘數
        定法 += 借算
        餘數 = 積 - 定法 * 借算

    return 定法

# 計算結果
a = 開方(積) # 159
#----- content ends here -----

"""
"""
