"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a尺 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. The problem involves a bamboo of height 1丈 (10尺), which is bent such that its tip touches the ground 3尺 away from the base. We are tasked to find the height of the bent bamboo above the ground, denoted as `a`.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
bamboo_height = Fraction(10)  # 1丈 = 10尺
distance_from_base = Fraction(3)  # 去本 = 3尺

# Calculation
# Step 1: Square the distance from the base
distance_squared = distance_from_base * distance_from_base

# Step 2: Subtract the squared distance from the bamboo height
remaining_height = bamboo_height - distance_squared

# Step 3: Halve the remaining height
a = remaining_height / 2

# The height of the bent bamboo above the ground is stored in variable 'a'
#----- content ends here -----


"""


The solution is stored in the variable `a` as a Fraction in units of 尺.
"""


"""
Variable 'a' has wrong value. Expected: 91/20, Actual: 1/2"""
