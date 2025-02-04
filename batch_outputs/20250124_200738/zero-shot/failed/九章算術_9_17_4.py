"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
術曰：東門南至隅步數，以乘南門東至隅步數為實。以木去門步數為法。實如法而一。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
east_west_distance = 7  # in li
north_south_distance = 9  # in li
distance_from_east_gate_to_tree = 15  # in li

# Convert li to steps (1 li = 1800 steps)
east_west_steps = east_west_distance * 1800
north_south_steps = north_south_distance * 1800
distance_to_tree_steps = distance_from_east_gate_to_tree * 1800

# Calculate the steps from the south gate to the tree
south_gate_to_tree_steps = Fraction(east_west_steps // 2 * north_south_steps // 2, distance_to_tree_steps)

# Assign the result to variable 'a'
a = south_gate_to_tree_steps

# Output the result
a
#----- content ends here -----


"""


The variable `a` will contain the number of steps from the south gate to the tree.
"""


"""
Variable 'a' has wrong value. Expected: 315, Actual: 1890"""
