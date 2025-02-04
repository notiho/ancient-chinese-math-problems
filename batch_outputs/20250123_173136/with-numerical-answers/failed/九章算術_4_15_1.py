"""
又有積三十九億七千二百一十五萬六百二十五步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=63025)步 。
"""

"""
Suppose there is a volume of 3,970,215,625 bu. 
Question: what is the side length of the square field?

The procedure for extracting square roots says: Place the volume as the dividend. Borrow one counting rod and place it, skipping one place. 
Estimate the result. Multiply the borrowed counting rod by 1 to create the divisor, and divide. 
After dividing, double the divisor to create the fixed divisor. Divide again. 
Halve the divisor and subtract. Place the borrowed counting rod again as before. Multiply it by 1 to estimate again. 
Add the result to the fixed divisor and divide. Subtract the result from the fixed divisor. Continue dividing and subtracting as before. 
If the square root cannot be fully extracted, it is considered unsolvable, and the side length is expressed as a fraction. 
If the volume has a fractional part, convert the numerator of the fraction into a whole number and extract the square root. 
Afterward, extract the square root of the denominator. If the denominator cannot be extracted, multiply the numerator by the denominator and extract the square root, ensuring the result is expressed as a fraction.

Answer: *a*(=63025) bu.
"""

from fractions import Fraction

# 置積為實
積 = 3970215625

# 開方術
def 開方(實):
    # Initialize variables
    借算 = 0
    定法 = 0
    副 = 0
    開方結果 = 0

    # Step 1: Borrow one counting rod and skip one place
    while (借算 + 1) ** 2 <= 實:
        借算 += 1

    # Step 2: Multiply borrowed rod by 1 to create the divisor
    法 = 借算 * 2

    # Step 3: Divide and update
    開方結果 = 借算
    剩餘 = 實 - 借算 ** 2

    # Step 4: Continue dividing and subtracting
    while 剩餘 > 0:
        借算 = 0
        while (定法 * 10 + 借算) * 借算 <= 剩餘:
            借算 += 1
        借算 -= 1
        副 = 借算
        開方結果 = 開方結果 * 10 + 副
        定法 = 定法 * 10 + 副
        剩餘 -= (定法 * 副)

    return 開方結果

# Calculate the square root
a = 開方(積)  # 63025
"""
Timed out"""
