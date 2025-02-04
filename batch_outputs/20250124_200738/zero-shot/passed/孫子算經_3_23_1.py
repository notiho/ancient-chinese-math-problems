"""
今有竿，不知長短，度其影，得一丈五尺，別立一表，長一尺五寸，影得五寸。問：竿長幾何？
術曰：置竿影一丈五尺，以表長一尺五寸乘之，上十之，得二十二丈五尺，以表影五寸除之，即得。
答曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the length of a pole ("竿") based on the relationship between the lengths of the pole, its shadow, a reference stick, and the shadow of the reference stick.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
pole_shadow = Fraction(1, 1) + Fraction(5, 10)  # 1丈5尺 = 1 + 5/10 丈
reference_length = Fraction(1, 10) + Fraction(5, 100)  # 1尺5寸 = 1/10 + 5/100 丈
reference_shadow = Fraction(5, 100)  # 5寸 = 5/100 丈

# Calculation
a = (pole_shadow * reference_length) / reference_shadow

# The length of the pole (竿長)
a  # Result in 丈
#----- content ends here -----


"""


### Explanation:
1. **Units Conversion**:
   - 1丈 = 10尺, and 1尺 = 10寸. Therefore:
     - 1丈5尺 = 1丈 + 5/10丈 = 1 + 0.5 = 1.5丈.
     - 1尺5寸 = 1/10丈 + 5/100丈 = 0.1 + 0.05 = 0.15丈.
     - 5寸 = 5/100丈 = 0.05丈.

2. **Formula**:
   - The length of the pole is calculated as:
     \[
     \text{竿長} = \frac{\text{竿影} \times \text{表長}}{\text{表影}}
     \]

3. **Substitute Values**:
   - Substitute the given values into the formula and compute the result.

The variable `a` will contain the length of the pole in 丈.
"""


"""
"""
