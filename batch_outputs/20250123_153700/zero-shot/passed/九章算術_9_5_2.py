"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
術曰：半池方自乘，以出水一尺自乘，減之，餘，倍出水除之，即得水深。加出水數，得葭長。
荅曰：水深 a丈 ；葭長 b丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a square pond with a reed growing at its center. The reed extends 1 foot above the water, and when bent to the edge of the pond, it just reaches the shore. We are tasked with finding the depth of the water (`a`, in zhang) and the length of the reed (`b`, in zhang).

Here is the Python code:


"""


from fractions import Fraction

# Given values
pond_side = Fraction(1)  # 1 zhang (side length of the square pond)
reed_above_water = Fraction(1, 10)  # 1 chi = 1/10 zhang (reed above water)

# Step 1: Calculate half the pond's side
half_pond_side = pond_side / 2

# Step 2: Square half the pond's side
half_pond_side_squared = half_pond_side ** 2

# Step 3: Square the reed above water
reed_above_water_squared = reed_above_water ** 2

# Step 4: Subtract the square of the reed above water from the square of half the pond's side
difference = half_pond_side_squared - reed_above_water_squared

# Step 5: Divide the difference by twice the reed above water to get the water depth
water_depth = difference / (2 * reed_above_water)

# Step 6: Add the reed above water to the water depth to get the total reed length
reed_length = water_depth + reed_above_water

# Assign the results to the variables a and b
a = water_depth  # Water depth in zhang
b = reed_length  # Reed length in zhang

# Output the results
a, b


"""


### Explanation of the Code:
1. The pond is square with a side length of 1 zhang. Half the side of the pond is `1/2` zhang.
2. The reed extends 1 chi (1/10 zhang) above the water.
3. Using the Pythagorean theorem, we calculate the depth of the water (`a`) and the total length of the reed (`b`).
4. The formula for water depth is derived as:
   \[
   a = \frac{\left(\frac{\text{pond side}}{2}\right)^2 - (\text{reed above water})^2}{2 \cdot (\text{reed above water})}
   \]
5. The total reed length is the sum of the water depth and the portion of the reed above the water:
   \[
   b = a + (\text{reed above water})
   \]

### Final Output:
The variables `a` and `b` will contain the water depth and reed length in zhang, respectively.
"""


"""
"""
