"""
今有陽馬，廣五尺，袤七尺，高八尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，三而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a rectangular prism (陽馬) with the given dimensions: width (廣) = 5 尺, length (袤) = 7 尺, and height (高) = 8 尺. The formula for the volume is:

\[
\text{Volume} = \frac{\text{width} \times \text{length} \times \text{height}}{3}
\]

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
width = 5  # 尺
length = 7  # 尺
height = 8  # 尺

# Calculate the volume
a = Fraction(width * length * height, 3)  # Volume in cubic 尺

# The result is stored in variable 'a'
#----- content ends here -----


"""


The value of `a` will represent the volume in cubic 尺.
"""


"""
"""
