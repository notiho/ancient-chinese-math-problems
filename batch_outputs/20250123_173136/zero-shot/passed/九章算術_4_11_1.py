"""
今有積五萬五千二百二十五步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
The problem describes a method for finding the square root of a number, expressed in ancient Chinese mathematical terms. The given number is \( 55225 \), and the task is to find its square root. Let's translate this into Python code.


"""


from fractions import Fraction

# Given data
number = 55225

# Compute the square root
a = int(number**0.5)

# Result
a  # The square root in steps (步)


"""


The solution is \( a = 235 \) steps.
"""


"""
"""
