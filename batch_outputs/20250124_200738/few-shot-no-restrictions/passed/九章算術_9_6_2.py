"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
術曰：以去本自乘，令如委數而一，所得，加委地數而半之，即索長
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a standing tree, with a rope tied to its top, and the rope touches the ground at a distance of 3 chi from the base of the tree.
When pulling the rope and walking backward, the person is 8 chi away from the base of the tree when the rope is fully stretched.
Question: how long is the rope?

The procedure says: Square the distance from the base (去本自乘), divide it by the distance the rope touches the ground (委數), and add the distance the rope touches the ground (委地數). Then take half of the result, which gives the length of the rope.

Answer: the rope is *a* zhang long.
"""

from fractions import Fraction

# 委地數 (distance the rope touches the ground)
委地數 = 3  # chi

# 去本 (distance from the base of the tree)
去本 = 8  # chi

# 索長 calculation
索長 = Fraction(去本**2, 委地數) + 委地數
索長 = 索長 / 2  # 半之

# Convert chi to zhang (1 zhang = 10 chi)
索長_丈 = 索長 / 10

a = 索長_丈  # 索長 in zhang

# Output the result
a#----- content ends here -----

"""
"""
