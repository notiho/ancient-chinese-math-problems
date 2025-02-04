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
- The circumference of the base of the cone (\(C\)) = 3丈5尺 = \(35\)尺 (since 1丈 = 10尺).
- The height of the cone (\(h\)) = 5丈1尺 = \(51\)尺.

We need to find the radius (\(r\)) from the circumference using the formula \(C = 2\pi r\), then compute the volume.

The problem specifies using \(\pi = 3\) for simplicity. Let's compute the solution in Python.


"""


from fractions import Fraction

# Given values
circumference = Fraction(35)  # in 尺
height = Fraction(51)         # in 尺
pi = Fraction(3)              # approximate value of π

# Calculate the radius
radius = circumference / (2 * pi)

# Calculate the volume of the cone
a = (pi * radius**2 * height) / 3

# The result is stored in variable 'a' (in cubic 尺)
a


"""

"""


"""
"""
