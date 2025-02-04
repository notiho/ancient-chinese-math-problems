"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a standing tree, and a rope is tied to its top. The rope touches the ground 3 chi away from the base of the tree.
When the rope is pulled taut and walked backward, the person is 8 chi away from the base of the tree, and the rope is fully extended.
Question: how long is the rope?

Answer: the rope is *a* zhang.
"""

#委地三尺 (distance from the base of the tree to where the rope touches the ground)
base_distance = 3

#去本八尺 (distance from the base of the tree to the person pulling the rope)
pull_distance = 8

#索長 (length of the rope, calculated using the Pythagorean theorem)
# Hypotenuse = sqrt(base_distance^2 + pull_distance^2)
rope_length = (base_distance**2 + pull_distance**2)**0.5

# Convert the rope length from chi to zhang (1 zhang = 10 chi)
a = Fraction(rope_length, 10)

a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
