"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
術曰：半鐻道自乘，如深寸而一，以深寸增之，即材徑。
荅曰：材徑 a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves finding the diameter of a circular material embedded in a wall, given the depth of the cut and the length of the chord formed by the cut.

The formula provided in the problem is:
1. Take half of the chord length and square it.
2. Divide this value by the depth of the cut.
3. Add the depth of the cut to the result from step 2.
4. The result is the diameter of the circular material.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
chord_length = Fraction(1, 1)  # 1 尺
depth = Fraction(1, 10)  # 1 寸 = 1/10 尺

# Calculations
half_chord = chord_length / 2
half_chord_squared = half_chord * half_chord
diameter = (half_chord_squared / depth) + depth

# Assign the result to the variable 'a'
a = diameter

# Output the result
a  # The diameter of the circular material in 尺
#----- content ends here -----


"""


This code calculates the diameter of the circular material (`a`) in units of 尺.
"""


"""
"""
