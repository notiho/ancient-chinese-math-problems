"""
又有積七萬一千八百二十四步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
To solve this problem, we need to compute the square root of the given area (積) in terms of steps (步). The problem describes a method for extracting the square root, but we can directly compute it using Python.

Here is the Python code to compute the value of \( a \) (the side length in steps):


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given area in steps
area = 71824  # 積七萬一千八百二十四步

# Compute the square root of the area
a = Fraction(math.isqrt(area))  # Using integer square root for exact computation

# Output the result
a  # The side length in steps
#----- content ends here -----


"""


The variable `a` will hold the side length in steps. If the square root is not an integer, the problem states that it is "不可開" (cannot be opened), and further steps would be needed to handle fractional results. However, for this specific problem, the square root of 71824 is an integer.
"""


"""
"""
