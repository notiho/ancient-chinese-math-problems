"""
今有邑方二百步，各中開門。出東門十五步有木。問︰出南門幾何步而見木？
術曰：出東門步數為法，半邑方自乘為實，實如法得一步。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a square city (邑) with a side length of 200 steps (步). A tree is located 15 steps outside the east gate, and we are tasked to find how many steps (a) outside the south gate one must walk to see the tree.

Here is the Python code:


"""


from fractions import Fraction

# Given values
side_length = 200  # side length of the square city in steps
east_gate_distance = 15  # distance from the east gate to the tree in steps

# Calculation
half_side = Fraction(side_length, 2)  # half the side length of the square city
square_half_side = half_side ** 2  # square of half the side length
a = Fraction(square_half_side, east_gate_distance)  # distance from the south gate to see the tree

# Result
a  # distance in steps


"""


The variable `a` will contain the solution in steps as a `Fraction`.
"""


"""
"""
