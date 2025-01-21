"""
今有方錐下方二丈七尺，高二丈九尺。問︰積幾何？
術曰：下方自乘，以高乘之，三而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a square pyramid. The formula for the volume of a square pyramid is:

\[
V = \frac{1}{3} \times \text{Base Area} \times \text{Height}
\]

Here:
- The side length of the square base is \(2\) 丈 \(7\) 尺.
- The height of the pyramid is \(2\) 丈 \(9\) 尺.

We first convert all measurements to 尺 (since \(1\) 丈 = \(10\) 尺):
- Side length of the base = \(2 \times 10 + 7 = 27\) 尺.
- Height = \(2 \times 10 + 9 = 29\) 尺.

The base area is the square of the side length, and the volume is then calculated using the formula above.

Here is the Python code to compute the volume:


"""


from fractions import Fraction

# Given dimensions
side_length = 27  # in 尺
height = 29       # in 尺

# Calculate the base area
base_area = side_length * side_length  # in square 尺

# Calculate the volume
a = Fraction(1, 3) * base_area * height  # in cubic 尺

# Result
a  # Volume in cubic 尺


"""


The variable `a` will contain the volume of the square pyramid in cubic 尺.
"""


"""
"""
