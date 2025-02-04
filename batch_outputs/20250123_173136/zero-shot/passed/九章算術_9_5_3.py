"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
術曰：半池方自乘，以出水一尺自乘，減之，餘，倍出水除之，即得水深。加出水數，得葭長。
荅曰：水深 a丈 ；葭長 b丈 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. We'll use the `Fraction` class to ensure precise calculations for numbers that might not be integers.

The problem describes a square pool with a side length of 1 丈 (zhang). A reed grows in the center of the pool and extends 1 尺 (chi) above the water. When the reed is pulled to the edge of the pool, it just touches the edge of the pool. We are tasked with finding the water depth (`a`, in 丈) and the length of the reed (`b`, in 丈).

1 丈 = 10 尺, so we need to convert units appropriately.

Here's the Python code:


"""


from fractions import Fraction

# Given values
side_length = Fraction(1)  # Pool side length in 丈
reed_above_water = Fraction(1, 10)  # Reed above water in 丈 (1 尺 = 1/10 丈)

# Step 1: Calculate the water depth (a)
# Half the pool's side length
half_side = side_length / 2

# Square of half the pool's side length
half_side_squared = half_side ** 2

# Square of the reed above water
reed_above_water_squared = reed_above_water ** 2

# Subtract the square of the reed above water from the square of half the pool's side length
difference = half_side_squared - reed_above_water_squared

# Divide the difference by twice the reed above water to get the water depth
a = difference / (2 * reed_above_water)

# Step 2: Calculate the total length of the reed (b)
b = a + reed_above_water

# Results
a  # Water depth in 丈
b  # Reed length in 丈


"""


This code calculates the water depth (`a`) and the reed length (`b`) in 丈. The `Fraction` class ensures that the calculations are precise and handle fractional values correctly.
"""


"""
"""
