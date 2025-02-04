"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
術曰：半池方自乘，以出水一尺自乘，減之，餘，倍出水除之，即得水深。加出水數，得葭長。
荅曰：水深 a丈 ；葭長 b丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a square pond with a reed growing in the center, extending 1 foot (1/10 of a丈) above the water. When the reed is bent to the edge of the pond, it just touches the edge. We are tasked to find the depth of the water (`a`) and the length of the reed (`b`).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
pond_side = Fraction(1)  # 1丈
reed_above_water = Fraction(1, 10)  # 1尺 = 1/10丈

# Step 1: Calculate half the pond's side
half_pond_side = pond_side / 2

# Step 2: Square half the pond's side
half_pond_side_squared = half_pond_side ** 2

# Step 3: Square the reed above water
reed_above_water_squared = reed_above_water ** 2

# Step 4: Subtract the square of the reed above water from the square of half the pond's side
difference = half_pond_side_squared - reed_above_water_squared

# Step 5: Divide the result by twice the reed above water to find the water depth
a = difference / (2 * reed_above_water)

# Step 6: Add the reed above water to the water depth to find the total reed length
b = a + reed_above_water

# Results
a  # Water depth in 丈
b  # Reed length in 丈
#----- content ends here -----


"""


### Explanation of the Code:
1. **Half the pond's side**: The pond is square with a side length of 1丈. Half of the side is `1丈 / 2`.
2. **Square half the pond's side**: This gives the square of the distance from the center of the pond to the edge.
3. **Square the reed above water**: The reed extends 1尺 (1/10丈) above the water. We square this value.
4. **Subtract**: The difference between the square of half the pond's side and the square of the reed above water gives the square of the water depth.
5. **Divide**: Dividing this difference by twice the reed above water gives the water depth (`a`).
6. **Add**: Adding the reed above water to the water depth gives the total length of the reed (`b`).

### Final Results:
- `a` is the water depth in 丈.
- `b` is the reed length in 丈.
"""


"""
"""
