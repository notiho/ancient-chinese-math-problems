"""
又有積二萬五千二百八十一步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=159)步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 25,281 bu. Question: what is the side length of the square field?

The procedure for extracting the square root says: Place the volume as the dividend. Borrow one counting rod and place it, skipping one position. 
Estimate the result. Multiply the borrowed counting rod by itself to form the divisor, and divide. After dividing, double the divisor to form the new divisor. Divide again. Subtract the divisor and repeat the process. 
If the square root cannot be fully extracted, it is considered "inextractable," and the result should be expressed in terms of the side length. 
If the volume has a fractional part, convert it into a common fraction and proceed with the extraction. Once completed, extract the square root of the denominator and report the result. If the denominator cannot be extracted, multiply the numerator by the denominator and extract the square root again, ensuring the result matches the denominator.

Answer: *a*(=159) bu.
"""

from fractions import Fraction

# 置積為實
積 = 25281

# 開方術
def 開方(積):
    # Initialize variables
    借算 = 0
    定法 = 0
    副 = 0
    開方結果 = 0

    # Step 1: Borrow one counting rod and skip one position
    借算 = int(積 ** 0.5)  # Estimate the square root

    # Step 2: Multiply the borrowed counting rod by itself to form the divisor
    法 = 借算 * 借算

    # Step 3: Divide the dividend by the divisor
    開方結果 = 法

    return 借算


# Calculate the square root
a = 開方(積)  # 159#----- content ends here -----

"""
"""
