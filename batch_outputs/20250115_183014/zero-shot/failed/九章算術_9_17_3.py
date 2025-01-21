"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
術曰：東門南至隅步數，以乘南門東至隅步數為實。以木去門步數為法。實如法而一。
荅曰： a步 。
"""

"""
To solve this problem, we need to calculate the number of steps from the south gate to the point where the tree becomes visible. Here's the Python code that computes the value of `a`:


"""


from fractions import Fraction

# Dimensions of the city
east_west = 7  # in li
north_south = 9  # in li

# Conversion: 1 li = 300 steps
li_to_steps = 300

# Distance from the east gate to the tree
distance_to_tree = 15  # in li

# Convert dimensions to steps
east_west_steps = east_west * li_to_steps
north_south_steps = north_south * li_to_steps

# Calculate the steps from the east gate to the southeast corner
east_gate_to_corner = north_south_steps // 2

# Calculate the steps from the south gate to the southeast corner
south_gate_to_corner = east_west_steps // 2

# Apply the formula
a = Fraction(east_gate_to_corner * south_gate_to_corner, distance_to_tree * li_to_steps)

# Result in steps
a = a * li_to_steps

# The answer is stored in variable 'a'


"""


The variable `a` now contains the number of steps from the south gate to the point where the tree becomes visible.
"""


"""
Variable 'a' has wrong value. Expected: 315, Actual: 94500"""
