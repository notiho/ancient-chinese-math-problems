"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
術曰：以去本自乘，令如委數而一，所得，加委地數而半之，即索長
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a standing tree, and a rope is tied to its top. The rope touches the ground at a distance of 3 chi from the base of the tree.
When pulling the rope taut and walking backward, the person is 8 chi away from the base of the tree when the rope is fully stretched.
Question: how long is the rope?

The procedure says: Square the distance from the base (8 chi), divide it by the distance the rope touches the ground (3 chi), and add the ground distance (3 chi).
Take half of the result, and that is the length of the rope.

Answer: the rope is *a* zhang long.
"""

from fractions import Fraction

# 委地三尺
委地 = 3  # chi

# 去本八尺
去本 = 8  # chi

# 以去本自乘
去本平方 = 去本 ** 2

# 令如委數而一
分之一 = Fraction(去本平方, 委地)

# 所得，加委地數
加委地 = 分之一 + 委地

# 而半之，即索長
索長 = Fraction(加委地, 2)

# Convert chi to zhang (1 zhang = 10 chi)
a = Fraction(索長, 10)

# Output the result
a#----- content ends here -----

"""
"""
