"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
術曰：令兩出門步數相乘，因而四之，為實。開方除之，即得邑方。
荅曰： a里 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. Here's the solution:


"""


from fractions import Fraction
import math

# Given data
north_gate_steps = 30  # steps from the north gate to the tree
west_gate_steps = 750  # steps from the west gate to the tree

# Calculation
product_of_steps = north_gate_steps * west_gate_steps
area_in_square_steps = 4 * product_of_steps
side_length_in_steps = math.sqrt(area_in_square_steps)

# Convert steps to li (里), assuming 1 li = 180 steps
a = Fraction(side_length_in_steps, 180)

# The answer is stored in variable 'a'


"""


The variable `a` will contain the side length of the square city in the unit of li (里).
"""


"""
Code error: both arguments should be Rational instances"""
