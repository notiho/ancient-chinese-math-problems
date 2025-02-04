"""
有山居木西，不知其高。山去木五十三里，木高九丈五尺。人立木東三里，望木末適與山峰斜平。人目高七尺。問︰山高幾何？
術曰：置木高減人目高七尺，餘，以乘五十三里為實。以人去木三里為法。實如法而一，所得，加木高即山高。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
distance_mountain_to_tree = Fraction(53)  # in li
tree_height = Fraction(9 * 10 + 5)  # in chi (9丈5尺 converted to chi, 1丈 = 10尺)
distance_person_to_tree = Fraction(3)  # in li
eye_height = Fraction(7)  # in chi

# Step 1: Calculate the effective height of the tree above the person's eye level
effective_tree_height = tree_height - eye_height

# Step 2: Multiply the effective tree height by the distance from the mountain to the tree
product = effective_tree_height * distance_mountain_to_tree

# Step 3: Divide the product by the distance from the person to the tree
mountain_height_above_tree_base = product / distance_person_to_tree

# Step 4: Add the tree height to get the total mountain height
a = mountain_height_above_tree_base + tree_height  # in chi

# Convert the result to zhang (1丈 = 10尺)
a = a / 10  # in zhang

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` now contains the height of the mountain in zhang.
"""


"""
"""
