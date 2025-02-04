"""
今有竿，不知長短，度其影，得一丈五尺，別立一表，長一尺五寸，影得五寸。問：竿長幾何？
術曰：置竿影一丈五尺，以表長一尺五寸乘之，上十之，得二十二丈五尺，以表影五寸除之，即得。
答曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the length of a pole ("竿") based on the ratio of its shadow to the shadow of a smaller object ("表"). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
pole_shadow = Fraction(1, 1) + Fraction(5, 10)  # 1丈5尺 = 1 + 5/10 丈
marker_length = Fraction(1, 10) + Fraction(5, 100)  # 1尺5寸 = 1/10 + 5/100 丈
marker_shadow = Fraction(5, 100)  # 5寸 = 5/100 丈

# Calculation
a = (pole_shadow * marker_length) / marker_shadow

# The length of the pole (竿) is stored in variable 'a'
#----- content ends here -----


"""


### Explanation:
1. Convert all measurements into the same unit (丈). 
   - 1丈 = 10尺, and 1尺 = 10寸.
   - 1丈5尺 = 1 + 5/10 丈.
   - 1尺5寸 = 1/10 + 5/100 丈.
   - 5寸 = 5/100 丈.

2. Use the formula provided in the problem:
   - Multiply the shadow of the pole by the length of the marker.
   - Divide the result by the shadow of the marker.

3. Store the result in the variable `a`, which represents the length of the pole.

### Output:
The variable `a` will contain the length of the pole in terms of 丈 as a `Fraction`.
"""


"""
"""
