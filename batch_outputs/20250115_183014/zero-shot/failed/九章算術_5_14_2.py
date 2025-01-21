"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a frustum of a square pyramid (a truncated pyramid). The formula described in the problem can be interpreted as:

1. Multiply the areas of the top and bottom squares.
2. Add the square of each area.
3. Multiply the result by the height.
4. Divide the result by 3.

The dimensions are given in "丈" (zhang), and the answer is required in "尺" (chi). Since 1 丈 = 10 尺, we will convert the final result into 尺.

Here is the Python code:


"""


from fractions import Fraction

# Dimensions in 丈
bottom_side = 5  # Bottom side length in 丈
top_side = 4     # Top side length in 丈
height = 5       # Height in 丈

# Step 1: Calculate the areas of the top and bottom squares
bottom_area = bottom_side ** 2  # Bottom area in 丈²
top_area = top_side ** 2        # Top area in 丈²

# Step 2: Multiply the areas of the top and bottom squares
product_of_areas = bottom_area * top_area

# Step 3: Add the square of each area
sum_of_areas = bottom_area + top_area + product_of_areas

# Step 4: Multiply by the height
volume_in_zhang_cubed = sum_of_areas * height

# Step 5: Divide by 3
volume_in_zhang_cubed = Fraction(volume_in_zhang_cubed, 3)

# Convert the volume to 尺³ (1 丈³ = 1000 尺³)
a = volume_in_zhang_cubed * 1000  # Volume in 尺³

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the volume of the frustum in cubic 尺 (chi³).
"""


"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 735000"""
