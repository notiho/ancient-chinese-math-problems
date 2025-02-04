"""
今有方錐下方二丈七尺，高二丈九尺。問︰積幾何？
術曰：下方自乘，以高乘之，三而一。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of a square pyramid. The formula for the volume of a square pyramid is:

\[
V = \frac{1}{3} \cdot \text{Base Area} \cdot \text{Height}
\]

Here, the base side length is \(2\) 丈 \(7\) 尺, and the height is \(2\) 丈 \(9\) 尺. We will convert all measurements to 尺 (1 丈 = 10 尺) and compute the volume.


"""

#----- content starts here -----

from fractions import Fraction

# Convert dimensions to 尺
base_side = 2 * 10 + 7  # 2 丈 7 尺 = 27 尺
height = 2 * 10 + 9     # 2 丈 9 尺 = 29 尺

# Calculate the base area (base_side^2)
base_area = base_side * base_side

# Calculate the volume of the square pyramid
a = Fraction(1, 3) * base_area * height  # Volume formula: (1/3) * base_area * height

# The answer is stored in variable 'a'
a  # Volume in cubic 尺
#----- content ends here -----


"""

"""


"""
"""
