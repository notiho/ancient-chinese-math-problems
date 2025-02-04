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

Here, the problem provides:
- The circumference of the base of the cone ("下周") is \(3\) 丈 \(5\) 尺.
- The height ("高") is \(5\) 丈 \(1\) 尺.

We need to compute the volume in cubic 尺 (cubic feet). First, we convert the given measurements into 尺:
- \(1\) 丈 = \(10\) 尺, so \(3\) 丈 \(5\) 尺 = \(35\) 尺.
- \(5\) 丈 \(1\) 尺 = \(51\) 尺.

The circumference of the base is \(35\) 尺. Using the formula for the circumference of a circle (\(C = 2 \pi r\)), we can solve for the radius \(r\):
\[
r = \frac{C}{2 \pi} = \frac{35}{2 \pi}
\]

Next, we calculate the volume:
\[
V = \frac{1}{3} \pi r^2 h
\]

Substituting \(r = \frac{35}{2 \pi}\) and \(h = 51\):
\[
V = \frac{1}{3} \pi \left(\frac{35}{2 \pi}\right)^2 \cdot 51
\]

Simplify the expression:
\[
V = \frac{1}{3} \pi \cdot \frac{35^2}{(2 \pi)^2} \cdot 51
\]
\[
V = \frac{1}{3} \cdot \frac{35^2 \cdot 51}{4 \pi}
\]
\[
V = \frac{35^2 \cdot 51}{12 \pi}
\]

Finally, we compute the value in Python using the `Fraction` class to maintain precision.


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
circumference = Fraction(35)  # in 尺
height = Fraction(51)         # in 尺

# Calculate radius
pi = Fraction(math.pi)
radius = circumference / (2 * pi)

# Calculate volume
a = (Fraction(1, 3) * pi * radius**2 * height).limit_denominator()

# Output the result
a  # Volume in cubic 尺
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 20825/12, Actual: 1607100349/969768"""
