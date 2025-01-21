"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
total_height = Fraction(10)  # 1丈 = 10尺
distance_from_base = Fraction(3)  # 去本 = 3尺

# Calculation
# Step 1: Square the distance from the base
distance_squared = distance_from_base * distance_from_base

# Step 2: Subtract the squared distance from the total height
remaining_height = total_height - distance_squared

# Step 3: Halve the remaining height to find the height of the broken part
a = remaining_height / 2

# Answer
a  # This is the height of the broken part in 尺


"""


The variable `a` contains the height of the broken part in 尺 as a `Fraction`.
"""


"""
Variable 'a' has wrong value. Expected: 91/20, Actual: 1/2"""
