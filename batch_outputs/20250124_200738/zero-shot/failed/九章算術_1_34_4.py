"""
今有弧田，弦三十步，矢十五步。問：為田幾何？
術曰：以弦乘矢，矢又自乘，并之，二而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a segment of a circular field (弧田), where the chord (弦) is 30 steps, and the arrow (矢, the perpendicular distance from the chord to the arc) is 15 steps. The formula provided is:

1. Multiply the chord by the arrow.
2. Square the arrow.
3. Add the results of step 1 and step 2.
4. Divide the sum by 2.

The result is the area of the field in "畝" (a traditional Chinese unit of area).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
chord = 30  # 弦 in steps
arrow = 15  # 矢 in steps

# Calculation
a = Fraction(chord * arrow + arrow**2, 2)  # Area in 畝

# Result
a  # The area in 畝
#----- content ends here -----


"""


The variable `a` will contain the area of the field in 畝 as a `Fraction`.
"""


"""
Variable 'a' has wrong value. Expected: 45/32, Actual: 675/2"""
