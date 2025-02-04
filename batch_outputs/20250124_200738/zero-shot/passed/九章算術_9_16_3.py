"""
今有邑方二百步，各中開門。出東門十五步有木。問︰出南門幾何步而見木？
術曰：出東門步數為法，半邑方自乘為實，實如法得一步。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
side_length = 200  # The side length of the square city in steps
east_gate_to_tree = 15  # Distance from the east gate to the tree in steps

# Calculation
half_side = Fraction(side_length, 2)  # Half of the side length
half_side_squared = half_side ** 2  # Half the side length squared
south_gate_to_tree = half_side_squared / east_gate_to_tree  # Distance from the south gate to the tree

# Answer
a = south_gate_to_tree  # The distance in steps
#----- content ends here -----


"""


The variable `a` will contain the answer in steps.
"""


"""
"""
