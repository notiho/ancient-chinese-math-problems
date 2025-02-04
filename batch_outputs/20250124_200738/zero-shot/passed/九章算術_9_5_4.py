"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
術曰：半池方自乘，以出水一尺自乘，減之，餘，倍出水除之，即得水深。加出水數，得葭長。
荅曰：水深 a丈 ；葭長 b丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a square pond with a reed growing at its center, extending 1 foot above the water. When the reed is bent to the edge of the pond, it just touches the edge. We need to calculate the depth of the water (`a`) and the length of the reed (`b`).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
side_length = Fraction(1)  # side length of the square pond in 丈
reed_above_water = Fraction(1, 10)  # height of the reed above water in 丈 (1 尺 = 1/10 丈)

# Step 1: Calculate half the side length of the pond
half_side = side_length / 2

# Step 2: Square the half side length
half_side_squared = half_side ** 2

# Step 3: Square the height of the reed above water
reed_above_water_squared = reed_above_water ** 2

# Step 4: Subtract the squared height of the reed above water from the squared half side length
difference = half_side_squared - reed_above_water_squared

# Step 5: Divide the difference by twice the height of the reed above water to get the water depth
a = difference / (2 * reed_above_water)

# Step 6: Add the height of the reed above water to the water depth to get the total reed length
b = a + reed_above_water

# Results
a  # Water depth in 丈
b  # Reed length in 丈
#----- content ends here -----


"""


### Explanation of the Code:
1. The pond is square with a side length of 1 丈. Half the side length is `1/2 丈`.
2. The reed extends 1 尺 (1/10 丈) above the water.
3. Using the Pythagorean theorem, the hypotenuse (reed length) and one leg (half the pond's side) are related to the other leg (water depth).
4. The formula for water depth (`a`) is derived as:
   \[
   a = \frac{\left(\frac{\text{side length}}{2}\right)^2 - (\text{reed above water})^2}{2 \times (\text{reed above water})}
   \]
5. The reed length (`b`) is the sum of the water depth and the height above water:
   \[
   b = a + (\text{reed above water})
   \]

### Results:
- `a` is the water depth in 丈.
- `b` is the total reed length in 丈.
"""


"""
"""
