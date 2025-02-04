"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
術曰：令兩出門步數相乘，因而四之，為實。開方除之，即得邑方。
荅曰： a里 。
"""

"""
To solve this problem, we need to compute the side length of a square city ("邑方") based on the distances from its gates to trees. The problem states that the distances from the north gate and the west gate to their respective trees are 30 steps and 750 steps. The formula provided is:

1. Multiply the distances from the two gates.
2. Multiply the result by 4.
3. Take the square root of the result to find the side length of the square city.

The answer is given in "里" (a traditional Chinese unit of length). To convert steps to "里", we assume 1 "里" = 360 steps.

Here is the Python code to calculate the solution:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given data
north_gate_to_tree = 30  # steps
west_gate_to_tree = 750  # steps
steps_per_li = 360  # steps in one "里"

# Step 1: Multiply the distances from the two gates
product_of_distances = north_gate_to_tree * west_gate_to_tree

# Step 2: Multiply the result by 4
area_times_four = product_of_distances * 4

# Step 3: Take the square root of the result
side_length_in_steps = math.sqrt(area_times_four)

# Convert the side length from steps to "里"
a = Fraction(side_length_in_steps, steps_per_li)

# The answer is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the side length of the square city in "里".
"""


"""
Code error: both arguments should be Rational instances"""
