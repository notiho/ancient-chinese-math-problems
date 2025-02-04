"""
又有積三十九億七千二百一十五萬六百二十五步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=63025)步 。
"""

"""
Suppose there is a volume of 3,970,215,625 bu. 
Question: what is the side length of the square (cube root)?

The procedure for extracting square roots says: Place the volume as the dividend. Borrow one counting rod, placing it, skipping one position. 
Estimate the result. Multiply the borrowed counting rod by 1 to form the divisor, and divide. After dividing, double the divisor to form the fixed divisor. Divide again. Subtract the divisor and proceed downward. 
Place the borrowed counting rod again as before. Multiply it by the estimate, obtaining the auxiliary result. Add it to the fixed divisor and divide. Subtract the auxiliary result from the fixed divisor. Divide and proceed downward as before. 
If the root cannot be fully extracted, it is considered non-extractable, and the result should be expressed in terms of the side length. 
If the dividend has fractions, convert them into a common fraction and proceed. After completing the extraction, extract the denominator as well. If the denominator cannot be extracted, multiply the denominator by the fixed result and extract it, ensuring it matches the denominator.

Answer: *a*(=63025) bu.
"""

# 置積為實
積 = 3970215625

# 開方術
def 開方(積):
    # Initialize variables
    借算 = 0
    定法 = 0
    副 = 0
    根 = 0
    剩餘 = 積

    while 剩餘 > 0:
        # Borrow one counting rod, skipping one position
        借算 = int(str(剩餘)[:1])  # Take the first digit (approximation)
        剩餘 = int(str(剩餘)[1:])  # Remove the first digit

        # Multiply borrowed rod by 1 to form the divisor
        法 = 借算 * 1

        # Divide and subtract
        商 = 剩餘 // 法
        剩餘 -= 商 * 法

        # Double the divisor to form the fixed divisor
        定法 = 2 * 法

        # Divide again and subtract
        商 = 剩餘 // 定法
        剩餘 -= 商 * 定法

        # Add to the root
        根 = 根 * 10 + 商

    return 根

# Calculate the square root
a = 開方(積)  # 63025
"""
Code error: invalid literal for int() with base 10: ''"""
