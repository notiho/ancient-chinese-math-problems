"""
有木去人不知遠近。立四表，相去各一丈，令左兩表與所望參相直。從後右表望之，入前右表三寸。問︰木去人幾何？
荅曰： a丈 。
"""

"""
There is a tree at an unknown distance from a person. Four markers are placed, each 1 zhang apart in a square formation. 
The left two markers are aligned with the tree when viewed from the front-left marker. 
From the back-right marker, the tree appears to shift inward by 3 cun relative to the front-right marker.
Question: How far is the tree from the person?

Answer: The tree is *a* zhang away.
"""

# Define the given values
marker_distance = 1  # distance between markers in zhang
shift = Fraction(3, 10)  # shift of the tree in zhang (3 cun = 3/10 zhang)

# Using similar triangles, the distance to the tree (a) can be calculated as:
# a = marker_distance / shift
a = Fraction(marker_distance, shift)

# The tree is `a` zhang away.
"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 10/3"""
