"""
有木去人不知遠近。立四表，相去各一丈，令左兩表與所望參相直。從後右表望之，入前右表三寸。問︰木去人幾何？
荅曰： a丈 。
"""

"""
There is a tree at an unknown distance. Four markers are placed, each 1 zhang apart in a square formation. 
The left two markers are aligned with the tree. From the rear-right marker, the tree appears to shift inward by 3 cun relative to the front-right marker.
Question: how far is the tree from the observer?

Answer: the tree is *a* zhang away.
"""

# Distance between markers (1 zhang)
marker_distance = 1  # in zhang

# Apparent shift of the tree (3 cun)
apparent_shift = Fraction(3, 10)  # convert 3 cun to zhang (1 zhang = 10 cun)

# Using similar triangles, the distance to the tree is calculated as:
# Distance to tree = marker_distance / apparent_shift
a = Fraction(marker_distance, apparent_shift)  # in zhang

a  # Result in zhang
"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 10/3"""
