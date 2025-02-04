"""
今有邑方不知大小，各中開門。出北門二十步有木。出南門十四步，折而西行一千七百七十五步見木。問︰邑方幾何？
術曰：以出北門步數乘西行步數，倍之，為實。并出南門步數為從法，開方除之，即邑方。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code. The problem involves finding the side length of a square-shaped city ("邑方") based on distances given for walking out of its gates and encountering a tree.

Here is the Python code:


"""


from fractions import Fraction
import math

# Given data
north_steps = 20  # steps out of the north gate
south_steps = 14  # steps out of the south gate
west_steps = 1775  # steps walking west after exiting the south gate

# Calculation
product = north_steps * west_steps  # Multiply north steps by west steps
double_product = 2 * product  # Double the product
sum_with_south = double_product + south_steps  # Add the south steps
a = math.sqrt(sum_with_south)  # Take the square root to find the side length of the square

# Result
a = Fraction(a).limit_denominator()  # Convert to a fraction if necessary


"""


The variable `a` will contain the side length of the square city in steps.
"""


"""
Variable 'a' has wrong value. Expected: 250, Actual: 101212953/379808"""
