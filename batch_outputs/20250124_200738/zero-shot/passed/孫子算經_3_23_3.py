"""
今有竿，不知長短，度其影，得一丈五尺，別立一表，長一尺五寸，影得五寸。問：竿長幾何？
術曰：置竿影一丈五尺，以表長一尺五寸乘之，上十之，得二十二丈五尺，以表影五寸除之，即得。
答曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the length of a pole (竿) based on the proportion of its shadow to a smaller reference object (表) and its shadow.

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

# Result
a  # Length of the pole in 丈
#----- content ends here -----


"""


### Explanation of the Code:
1. **Units Conversion**:
   - 1 丈 = 10 尺, and 1 尺 = 10 寸.
   - The shadow of the pole is 1丈5尺, which is converted to `1 + 5/10 丈`.
   - The reference object's length is 1尺5寸, which is converted to `1/10 + 5/100 丈`.
   - The shadow of the reference object is 5寸, which is converted to `5/100 丈`.

2. **Proportionality**:
   - The length of the pole is proportional to the ratio of the pole's shadow to the reference object's shadow, scaled by the reference object's length.
   - Formula: `pole_length = (pole_shadow * reference_length) / reference_shadow`.

3. **Result**:
   - The result is stored in the variable `a`, representing the length of the pole in 丈.


"""


"""
"""
