"""
又有積七萬一千八百二十四步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=268)步 。
"""

"""
Suppose there is an area of 71824 bu². 
Question: what is the side length of the square field?

The procedure for extracting the square root says: Place the area as the dividend. Borrow one counting rod column, shifting it one place to the left. 
Estimate the result. Multiply the estimate by itself, obtaining the divisor, and divide. After dividing, double the divisor to get the fixed divisor. Divide again. Subtract the divisor and bring down the next digit. Repeat the process as before. 
If the square root cannot be fully extracted, it is considered "not exact" and the result should be expressed in terms of the side length. 
If the dividend has a fraction, convert it to a common fraction and proceed as before. After completing the extraction, extract the square root of the denominator. If the denominator cannot be extracted, multiply the numerator by the denominator and extract again, ensuring the denominator is 1.

Answer: *a*(=268) bu.
"""

# 置積為實
積 = 71824

# 開平方根
def 開平方根(實):
    # Initialize variables
    借算 = 0
    定法 = 0
    副 = 0
    開方結果 = 0

    # Step-by-step manual square root extraction
    while 實 > 0:
        # 超一等 (shift left by one place)
        借算 = len(str(實)) // 2

        # 議所得 (estimate the next digit)
        所得 = 1
        while (所得 * 所得) <= 實:
            所得 += 1
        所得 -= 1

        # Update 開方結果
        開方結果 = 開方結果 * 10 + 所得

        # Subtract the square of the estimate
        實 -= 所得 * 所得

        # 倍法為定法 (double the divisor for the next step)
        定法 = 2 * 開方結果

    return 開方結果

# 計算答案
a = 開平方根(積) # 268
"""
"""
