"""
今有邑方二百步，各中開門。出東門十五步有木。問︰出南門幾何步而見木？
術曰：出東門步數為法，半邑方自乘為實，實如法得一步。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
side_length = 200  # The side of the square city in steps
east_gate_to_tree = 15  # Distance from the east gate to the tree in steps

# Calculation
half_side = Fraction(side_length, 2)  # Half of the side of the square
square_half_side = half_side ** 2  # Square of half the side
south_gate_to_tree = square_half_side / east_gate_to_tree  # Distance from the south gate to the tree

# Answer
a = south_gate_to_tree


"""


The variable `a` will hold the answer in steps.
"""


"""
"""
