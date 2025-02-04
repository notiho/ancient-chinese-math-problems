"""
今有圓錐下周三丈五尺，高五丈一尺。問︰積幾何？
術曰：下周自乘，以高乘之，三十六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a cone. The formula for the volume of a cone is:

\[
V = \frac{\pi r^2 h}{3}
\]

Here, the problem provides:
- The circumference of the base (下周) is \(3\) 丈 \(5\) 尺.
- The height (高) is \(5\) 丈 \(1\) 尺.

### Conversion:
1 丈 = 10 尺.  
Thus:
- Circumference = \(3 \times 10 + 5 = 35\) 尺.
- Height = \(5 \times 10 + 1 = 51\) 尺.

From the circumference, we can calculate the radius \(r\) using the formula for the circumference of a circle:

\[
\text{Circumference} = 2 \pi r \implies r = \frac{\text{Circumference}}{2 \pi}
\]

Finally, substitute \(r\) and \(h\) into the cone volume formula to compute the volume.

Here is the Python code to compute the solution:


"""


from fractions import Fraction
from math import pi

# Given data
circumference = Fraction(35)  # in 尺
height = Fraction(51)         # in 尺

# Calculate radius
radius = circumference / (2 * pi)

# Volume of the cone
a = (pi * radius**2 * height) / 3

# Convert to 尺 (since the problem asks for the answer in 尺)
a = a  # Volume is already in 尺³


"""


The variable `a` will hold the volume of the cone in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 20825/12, Actual: 1657.2008449443601"""
