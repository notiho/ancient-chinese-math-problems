"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
荅曰： a丈 。
"""

"""
Suppose there is a standing tree. A rope is tied to its top and the other end of the rope touches the ground 3 chi away from the base of the tree. 
When the rope is pulled tight and the person walks away, the person is 8 chi away from the base of the tree when the rope is fully stretched.
Question: how long is the rope?

Answer: *a* zhang.
"""

# Given:
委地 = 3  # chi (distance from the base of the tree to where the rope touches the ground)
去本 = 8  # chi (distance from the base of the tree to the person pulling the rope)

# The rope forms the hypotenuse of a right triangle:
# The height of the tree is the vertical leg (h), the horizontal distance from the base to the person is the horizontal leg (b), and the rope is the hypotenuse (c).
# Using the Pythagorean theorem: c^2 = h^2 + b^2

# Calculate the length of the rope (c):
a = Fraction((委地**2 + 去本**2)**0.5, 10)  # Convert chi to zhang (1 zhang = 10 chi)

a
"""
Code error: both arguments should be Rational instances"""
