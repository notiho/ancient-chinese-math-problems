"""
有山居木西，不知其高。山去木五十三里，木高九丈五尺。人立木東三里，望木末適與山峰斜平。人目高七尺。問︰山高幾何？
術曰：置木高減人目高七尺，餘，以乘五十三里為實。以人去木三里為法。實如法而一，所得，加木高即山高。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the height of a mountain based on the given distances and heights. Here's the solution:


"""


from fractions import Fraction

# Given data
wood_height = Fraction(9, 1) + Fraction(5, 10)  # 9丈5尺 = 9 + 5/10 丈
eye_height = Fraction(7, 10)  # 7尺 = 7/10 丈
distance_mountain_to_wood = Fraction(53, 1)  # 53里
distance_person_to_wood = Fraction(3, 1)  # 3里

# Step 1: Subtract the eye height from the wood height
effective_wood_height = wood_height - eye_height

# Step 2: Multiply the effective wood height by the distance from the mountain to the wood
product = effective_wood_height * distance_mountain_to_wood

# Step 3: Divide the product by the distance from the person to the wood
quotient = product / distance_person_to_wood

# Step 4: Add the wood height to the quotient to get the mountain height
a = quotient + wood_height

# The height of the mountain is stored in variable 'a'
a


"""


The variable `a` contains the height of the mountain in 丈.
"""


"""
"""
