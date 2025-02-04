"""
有木去人不知遠近。立四表，相去各一丈，令左兩表與所望參相直。從後右表望之，入前右表三寸。問︰木去人幾何？
荅曰： a丈 。
"""

"""
There is a tree at an unknown distance from a person. Four markers are placed, each 1 zhang apart in a square formation. The left two markers are aligned with the tree in a straight line. Observing from the rear-right marker, the tree appears to shift inward by 3 cun relative to the front-right marker. 

Question: How far is the tree from the person?

Answer: The tree is *a* zhang away.
"""

# Distance between markers (1 zhang)
marker_distance = 1

# Apparent shift of the tree (3 cun, convert to zhang: 1 zhang = 10 chi, 1 chi = 10 cun)
apparent_shift = Fraction(3, 100)  # 3 cun = 3/100 zhang

# Using similar triangles, the distance to the tree can be calculated as:
# Distance to tree = marker_distance / apparent_shift
a = Fraction(marker_distance, apparent_shift)

# Result
a  # The distance to the tree in zhang
"""
"""
