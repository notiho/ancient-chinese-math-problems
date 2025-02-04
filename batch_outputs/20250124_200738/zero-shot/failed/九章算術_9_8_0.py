"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
術曰：半鐻道自乘，如深寸而一，以深寸增之，即材徑。
荅曰：材徑 a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code. The problem describes a circular material embedded in a wall, and we are tasked with finding its diameter based on the depth of the cut and the length of the chord created by the cut.

The formula provided in the problem is:
1. Take half of the chord length and square it.
2. Divide the depth by itself (this is essentially 1).
3. Add the depth to the squared value from step 1.
4. The result is the diameter of the circular material.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
depth = Fraction(1, 12)  # 1寸 = 1/12尺
chord_length = Fraction(1)  # 1尺

# Calculations
half_chord = chord_length / 2
half_chord_squared = half_chord * half_chord
a = half_chord_squared / depth + depth

# The diameter of the circular material is stored in variable 'a'
#----- content ends here -----


"""


After running this code, the variable `a` will contain the diameter of the circular material in units of 尺.
"""


"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 37/12"""
