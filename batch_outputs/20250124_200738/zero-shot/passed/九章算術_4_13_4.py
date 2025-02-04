"""
又有積七萬一千八百二十四步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
This problem describes a method for finding the square root of a number, which is essentially asking for the side length of a square given its area. The area is given as 71,824 steps, and the goal is to compute the square root of this number.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given area
area = 71824

# Compute the square root
a = int(area**0.5)

# Result
a  # in steps
#----- content ends here -----


"""


The value of `a` will represent the side length of the square in steps.
"""


"""
"""
