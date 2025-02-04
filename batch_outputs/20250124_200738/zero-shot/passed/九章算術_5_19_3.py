"""
今有陽馬，廣五尺，袤七尺，高八尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，三而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a rectangular prism (陽馬) with dimensions given in 尺 (Chinese feet). The formula for the volume is:

\[
\text{Volume} = \frac{\text{Length} \times \text{Width} \times \text{Height}}{3}
\]

Here, the dimensions are:
- Width (廣) = 5 尺
- Length (袤) = 7 尺
- Height (高) = 8 尺

The result will be divided by 3 as per the problem's instructions.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions in 尺
width = 5
length = 7
height = 8

# Calculate the volume
a = Fraction(width * length * height, 3)

# The result is stored in variable 'a'
#----- content ends here -----


"""


The value of `a` will represent the volume in 尺³.
"""


"""
"""
