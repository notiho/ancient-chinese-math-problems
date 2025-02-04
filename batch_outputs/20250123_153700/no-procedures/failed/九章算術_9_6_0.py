"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
荅曰： a丈 。
"""

"""
Suppose there is a standing tree. A rope is tied to the top of the tree, and the other end of the rope is placed on the ground 3 chi away from the base of the tree. 
When the rope is pulled tight, the person pulling it walks 8 chi away from the base of the tree until the rope is fully stretched.
Question: how long is the rope?

Answer: the rope is *a* zhang.
"""

# The problem forms a right triangle:
# - The height of the tree (minus the 3 chi where the rope touches the ground) is one leg of the triangle.
# - The distance the person walks away from the base of the tree is the other leg of the triangle.
# - The length of the rope is the hypotenuse.

# Height of the tree above the ground where the rope touches (in chi)
height = 8 - 3  # 8 chi (tree height) minus 3 chi (rope touching ground)

# Distance from the base of the tree (in chi)
distance = 8

# Using the Pythagorean theorem: hypotenuse^2 = height^2 + distance^2
rope_length_squared = height**2 + distance**2

# Calculate the rope length (hypotenuse)
rope_length = Fraction(rope_length_squared).sqrt()

# Convert the rope length from chi to zhang (1 zhang = 10 chi)
a = rope_length / 10
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
