"""
今有方堡壔方一丈六尺，高一丈五尺。問︰積幾何？
術曰：方自乘，以高乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a cuboid (方堡壔). The given dimensions are:

- Side length of the square base: 1丈6尺 (1丈 = 10尺, so 1丈6尺 = 16尺)
- Height: 1丈5尺 (1丈 = 10尺, so 1丈5尺 = 15尺)

The formula for the volume of a cuboid is:

\[
\text{Volume} = \text{Base Area} \times \text{Height}
\]

The base area of the square is calculated as:

\[
\text{Base Area} = \text{Side Length}^2
\]

Now, let's write the Python code to compute the volume.


"""


from fractions import Fraction

# Dimensions in 尺
side_length = Fraction(16)  # 1丈6尺 = 16尺
height = Fraction(15)       # 1丈5尺 = 15尺

# Calculate the base area
base_area = side_length * side_length

# Calculate the volume
a = base_area * height  # Volume in 尺³

# The result is stored in variable 'a'


"""


The variable `a` will contain the volume in cubic 尺 (尺³).
"""


"""
"""
