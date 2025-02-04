"""
今有陽馬，廣五尺，袤七尺，高八尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，三而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a rectangular prism (陽馬). The formula for the volume is given as the product of the length (廣), width (袤), and height (高), divided by 3.

Here is the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Dimensions of the rectangular prism
廣 = 5  # in 尺
袤 = 7  # in 尺
高 = 8  # in 尺

# Calculate the volume
a = Fraction(廣 * 袤 * 高, 3)  # in 尺

# The result is stored in variable `a`


"""


The value of `a` represents the volume in cubic 尺.
"""


"""
"""
