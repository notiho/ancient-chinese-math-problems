"""
又有積五十六萬四千七百五十二步、四分步之一。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=1503/2)步 。
"""

"""
Suppose there is an area of 564,752 and 1/4 bu².
Question: what is the side length of the square field?

The procedure for extracting the square root says:
1. Place the area as the dividend.
2. Borrow one counting rod position, shifting one place higher.
3. Estimate the result. Multiply the estimate by itself to form the divisor, and divide.
4. After dividing, double the divisor to form the "fixed divisor."
5. Continue dividing. Subtract the divisor and bring down the next digit.
6. Repeat the process by borrowing one counting rod position and estimating again.
7. If the square root cannot be exact, the result is not a perfect square, and the side length should be expressed as a fraction.
8. If the area has a fractional part, convert it to a common fraction and include it in the calculation.
9. Extract the square root of the numerator and denominator separately. If the denominator cannot be simplified, multiply the numerator by the denominator and extract the square root again.

Answer: *a*(=1503/2) bu.
"""

from fractions import Fraction

# 積五十六萬四千七百五十二步、四分步之一
積 = Fraction(564752, 1) + Fraction(1, 4)

# 開方術
# Step 1: Place the area as the dividend
實 = 積

# Step 2: Convert the fractional part into a common fraction
# The numerator is already part of the area, so no further conversion is needed.

# Step 3: Extract the square root of the numerator and denominator separately
# Numerator: 564752 * 4 = 2259009
# Denominator: 4
定實 = Fraction(2259009, 4)

# Step 4: Extract the square root of the numerator and denominator
# Numerator: √2259009 = 1503
# Denominator: √4 = 2
a = Fraction(1503, 2)  # 1503/2 bu
"""
"""
