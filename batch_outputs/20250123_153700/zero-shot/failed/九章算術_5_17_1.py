"""
今有圓錐下周三丈五尺，高五丈一尺。問︰積幾何？
術曰：下周自乘，以高乘之，三十六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a cone. The formula for the volume of a cone is:

\[
V = \frac{1}{3} \pi r^2 h
\]

The problem gives:
- The circumference of the base of the cone (下周) = 3丈5尺 = 35尺 (1丈 = 10尺),
- The height (高) = 5丈1尺 = 51尺.

From the circumference, we can calculate the radius \( r \) using the formula for the circumference of a circle:

\[
\text{Circumference} = 2 \pi r \implies r = \frac{\text{Circumference}}{2 \pi}
\]

The volume is then calculated using the cone volume formula.

Here is the Python code to compute the solution:


"""


from fractions import Fraction
import math

# Given values
circumference = Fraction(35)  # in 尺
height = Fraction(51)  # in 尺

# Calculate radius
radius = circumference / (2 * math.pi)

# Volume of the cone
a = (Fraction(1, 3) * math.pi * radius**2 * height) * 36  # Convert to 尺³

# Result
a  # Volume in 尺³


"""


The variable `a` will contain the volume of the cone in cubic 尺 (尺³).
"""


"""
Variable 'a' has wrong value. Expected: 20825/12, Actual: 59659.230417996965"""
