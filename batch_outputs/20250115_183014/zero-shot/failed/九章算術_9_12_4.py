"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a尺 。
"""

"""
This is a classic ancient Chinese math problem. Let's translate it into Python code to compute the value of the unknown `a` (折者之高, the height of the broken part of the bamboo). We'll use the `Fraction` class to ensure precision.

### Problem Breakdown:
- The bamboo is 1 丈 (10 尺) tall.
- The top of the bamboo bends to touch the ground, 3 尺 away from the base.
- We need to find the height of the broken part of the bamboo (`a` 尺).

The solution method:
1. Square the distance from the base to where the top touches the ground (3 尺).
2. Subtract this value from the total height of the bamboo (10 尺).
3. Halve the remaining value to find the height of the broken part.

### Python Code:

"""


from fractions import Fraction

# Given values
bamboo_height = Fraction(10)  # 1 丈 = 10 尺
distance_from_base = Fraction(3)  # 3 尺

# Step 1: Square the distance from the base
distance_squared = distance_from_base * distance_from_base

# Step 2: Subtract the squared distance from the bamboo height
remaining_height = bamboo_height - distance_squared

# Step 3: Halve the remaining height to find the height of the broken part
a = remaining_height / 2

# The height of the broken part is stored in variable `a`


"""


### Solution:
The variable `a` will contain the height of the broken part of the bamboo in 尺.
"""


"""
Variable 'a' has wrong value. Expected: 91/20, Actual: 1/2"""
