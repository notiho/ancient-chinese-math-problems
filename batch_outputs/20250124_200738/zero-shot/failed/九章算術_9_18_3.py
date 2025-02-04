"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
術曰：令兩出門步數相乘，因而四之，為實。開方除之，即得邑方。
荅曰： a里 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given data
north_gate_steps = 30
west_gate_steps = 750

# Calculation
product_of_steps = north_gate_steps * west_gate_steps
area = Fraction(product_of_steps * 4)  # Multiply by 4 as per the method
side_length = math.sqrt(area)  # Take the square root to find the side length of the square

# Convert to "里" (assuming 1 step = 1/300 里)
a = Fraction(side_length, 300)

# Result
a
#----- content ends here -----


"""


The variable `a` will contain the side length of the square in "里".
"""


"""
Code error: both arguments should be Rational instances"""
