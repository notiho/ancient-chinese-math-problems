"""
有木去人不知遠近。立四表，相去各一丈，令左兩表與所望參相直。從後右表望之，入前右表三寸。問︰木去人幾何？
荅曰： a丈 。
"""

"""
There is a tree at an unknown distance from a person. Four markers are placed, each one zhang apart in a square formation. The left two markers and the tree are aligned in a straight line. From the rear-right marker, the tree appears to shift inward by 3 cun relative to the front-right marker. 

Question: How far is the tree from the person?

Answer: The tree is *a* zhang away.
"""

# Define the known values
marker_distance = 1  # Distance between markers in zhang
shift = Fraction(3, 10)  # Apparent shift of the tree in zhang (3 cun = 3/10 zhang)

# Use similar triangles to calculate the distance to the tree
# The ratio of the shift to the marker distance is the same as the ratio of the marker distance to the tree's distance
a = marker_distance * marker_distance / shift

# The tree is `a` zhang away.
"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 10/3"""
