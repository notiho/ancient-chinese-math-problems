"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
術曰：以去本自乘，令如委數而一，所得，加委地數而半之，即索長
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a standing tree, with a rope tied to its top, and the rope touches the ground at a distance of 3 chi from the base of the tree.
When pulling the rope and walking backward, one moves 8 chi from the base of the tree until the rope is fully stretched.
Question: how long is the rope?

The procedure says: Square the distance from the base (去本自乘), divide it by the distance the rope touches the ground (委數), then add the distance the rope touches the ground (委地數) and take half of the result. This gives the length of the rope.

Answer: *a* zhang.
"""

from fractions import Fraction

# 委地數 (distance the rope touches the ground)
委地數 = 3  # in chi

# 去本 (distance from the base of the tree)
去本 = 8  # in chi

# Step 1: 去本自乘 (square the distance from the base)
去本平方 = 去本 ** 2

# Step 2: Divide by 委數 (distance the rope touches the ground)
商 = Fraction(去本平方, 委地數)

# Step 3: Add 委地數 (distance the rope touches the ground)
和 = 商 + 委地數

# Step 4: Take half of the result
索長 = Fraction(和, 2)

# Convert from chi to zhang (1 zhang = 10 chi)
a = Fraction(索長, 10)

# Final answer
a#----- content ends here -----

"""
"""
