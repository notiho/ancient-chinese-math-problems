"""
又有積二萬五千二百八十一步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
This problem involves finding the side length of a square given its area. The ancient Chinese method described here is essentially a square root calculation. Let's translate this into Python code:


"""


from fractions import Fraction

# Given area
area = Fraction(25281)  # The area is 25281 square steps.

# Compute the side length of the square
a = area ** Fraction(1, 2)  # Square root of the area

# The result is stored in variable 'a' as the side length in steps.


"""


Here, `a` represents the side length of the square in steps. The `Fraction` class ensures that the calculation is precise and can handle non-integer results.
"""


"""
"""
