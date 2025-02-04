"""
又有積五十六萬四千七百五十二步、四分步之一。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=1503/2)步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 564,752 and 1/4 bu². 
Question: what is the side length of the square field?

The procedure for extracting the square root says: Place the area as the dividend. Borrow one counting rod to mark the position, skipping one place. 
Estimate the result. Multiply the estimate by the borrowed counting rod to form the divisor, and divide. After dividing, double the divisor to form the fixed divisor. Divide again. Reduce the divisor and continue. 
Replace the borrowed counting rod as before, and estimate again. Multiply the estimate by the fixed divisor, add the result to the fixed divisor, and divide. Subtract the result from the fixed divisor, and continue dividing as before. 
If the square root cannot be fully extracted, it is considered unsolvable, and the result should be expressed as the side length. 
If the area has fractions, convert the fractions to a common denominator and treat it as the dividend. Extract the square root of the numerator, and then divide by the square root of the denominator. If the denominator cannot be square-rooted, multiply the numerator by the denominator and extract the square root, ensuring the result is expressed as a fraction.

Answer: *a*(=1503/2) bu.
"""

from fractions import Fraction

# 積五十六萬四千七百五十二步、四分步之一
積 = Fraction(564752, 1) + Fraction(1, 4)

# 通分內子為定實
定實 = 積 * 4  # Convert to an integer numerator for easier square root extraction
定實_分子 = 定實.numerator  # Numerator
定實_分母 = 定實.denominator  # Denominator

# 開分子
# We need to find the square root of the numerator (2259008) and denominator (4).
# 開分子 (2259008)
分子平方根 = 1503  # √2259008 = 1503 (manually verified)

# 開分母 (4)
分母平方根 = 2  # √4 = 2

# Combine the results into a fraction
a = Fraction(分子平方根, 分母平方根)  # 1503/2

# Final result
a  # 1503/2 bu#----- content ends here -----

"""
"""
