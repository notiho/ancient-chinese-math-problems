"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
術曰：以去本自乘，令如委數而一，所得，加委地數而半之，即索長
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is an upright tree, with a rope tied to its top. The rope touches the ground at a distance of 3 chi from the base of the tree.
When pulling the rope and walking backward, the person is 8 chi away from the base of the tree when the rope is fully stretched.
Question: how long is the rope?

The procedure says: Take the distance from the base (8 chi) and square it. Divide it by the distance the rope touches the ground (3 chi), treating it as the divisor.
Add the result to the distance the rope touches the ground (3 chi), and take half of the sum. This is the length of the rope.

Answer: the rope is *a* zhang long.
"""

from fractions import Fraction

# Given values
去本 = 8  # Distance from the base in chi
委地 = 3  # Distance the rope touches the ground in chi

# Procedure
去本平方 = 去本 ** 2  # Square the distance from the base
商 = Fraction(去本平方, 委地)  # Divide by the distance the rope touches the ground
和 = 商 + 委地  # Add the distance the rope touches the ground
索長 = Fraction(和, 2)  # Take half of the sum

# Convert chi to zhang (1 zhang = 10 chi)
a = Fraction(索長, 10)  # Rope length in zhang

a  # Output the result#----- content ends here -----

"""
"""
