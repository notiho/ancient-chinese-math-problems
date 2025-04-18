"""
今有弧田，弦三十步，矢十五步。問：為田幾何？
術曰：以弦乘矢，矢又自乘，并之，二而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a field in the shape of a circular segment (弧田), where the chord (弦) is 30 steps, and the arrow (矢, the height of the segment) is 15 steps. The formula provided in the problem is:

1. Multiply the chord (弦) by the arrow (矢).
2. Square the arrow (矢) and add it to the result from step 1.
3. Divide the sum by 2 to get the area.

Here is the Python code:


"""


from fractions import Fraction

# Given values
chord = 30  # 弦 in steps
arrow = 15  # 矢 in steps

# Calculation
a = Fraction(chord * arrow + arrow**2, 2)  # Area in 畝 (mu)

# Result
a  # The area of the field in 畝


"""


The variable `a` will store the area of the field in 畝 (mu).
"""


"""
Variable 'a' has wrong value. Expected: 45/32, Actual: 675/2"""
