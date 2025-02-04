"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
術曰：半池方自乘，以出水一尺自乘，減之，餘，倍出水除之，即得水深。加出水數，得葭長。
荅曰：水深 a丈 ；葭長 b丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a square pond with a reed growing in the center, extending 1 foot above the water. When the reed is pulled to the edge of the pond, it just touches the edge. We are tasked with finding the depth of the water (`a`, in zhang) and the length of the reed (`b`, in zhang).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
pond_side = Fraction(1)  # 1 zhang (side length of the square pond)
reed_above_water = Fraction(1, 10)  # 1 chi = 1/10 zhang (reed above water)

# Step 1: Calculate water depth (a)
# Half the pond's side length
half_pond_side = pond_side / 2

# Square of half the pond's side length
half_pond_side_squared = half_pond_side ** 2

# Square of the reed above water
reed_above_water_squared = reed_above_water ** 2

# Subtract the square of the reed above water from the square of half the pond's side length
difference = half_pond_side_squared - reed_above_water_squared

# Divide the difference by twice the reed above water to get the water depth
water_depth = difference / (2 * reed_above_water)

# Step 2: Calculate reed length (b)
# Add the water depth to the reed above water
reed_length = water_depth + reed_above_water

# Assign results to variables a and b
a = water_depth  # Water depth in zhang
b = reed_length  # Reed length in zhang

# Results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: The side length of the square pond is 1 zhang, and the reed extends 1 chi (1/10 zhang) above the water.
2. **Water Depth Calculation**:
   - The square of half the pond's side length is calculated.
   - The square of the reed above water is subtracted from this value.
   - The result is divided by twice the reed above water to find the water depth (`a`).
3. **Reed Length Calculation**:
   - The water depth is added to the reed above water to find the total length of the reed (`b`).
4. **Output**: The variables `a` and `b` store the water depth and reed length, respectively.

### Final Result:
The variables `a` and `b` will contain the water depth and reed length in zhang.
"""


"""
"""
