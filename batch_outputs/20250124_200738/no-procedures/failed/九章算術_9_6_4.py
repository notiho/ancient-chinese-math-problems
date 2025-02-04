"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is an upright tree. A rope is tied to the top of the tree, and the other end of the rope touches the ground 3 chi away from the base of the tree. 
When the rope is pulled tight and the person walks 8 chi away from the base of the tree, the rope is fully stretched.
Question: how long is the rope?

Answer: the rope is *a* zhang.
"""

# Given values
base_to_ground = 3  # chi
distance_walked = 8  # chi

# The length of the rope forms the hypotenuse of a right triangle
# Hypotenuse = sqrt((base_to_ground)^2 + (distance_walked)^2)

# Calculate the rope length
rope_length = (base_to_ground**2 + distance_walked**2)**0.5  # in chi

# Convert chi to zhang (1 zhang = 10 chi)
a = Fraction(rope_length, 10)  # in zhang#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
