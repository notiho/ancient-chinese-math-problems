"""
又有箕田，舌廣一百一十七步，踵廣五十步，正從一百三十五步。問：為田幾何？
術曰：并踵、舌而半之，以乘正從。畝法而一。
荅曰： a畝 。
"""

"""
To solve the problem, let's translate the ancient Chinese math problem into Python code. The problem describes a trapezoidal field, where the shorter base (踵廣) is 50 steps, the longer base (舌廣) is 117 steps, and the height (正從) is 135 steps. The formula to calculate the area of a trapezoid is:

\[
\text{Area} = \frac{\text{Base1} + \text{Base2}}{2} \times \text{Height}
\]

The result is then converted into "畝" (a unit of area). Let's compute this in Python:


"""


from fractions import Fraction

# Given values
舌廣 = 117  # steps
踵廣 = 50   # steps
正從 = 135  # steps

# Calculate the area in steps squared
area_steps_squared = Fraction(舌廣 + 踵廣, 2) * 正從

# Convert steps squared to 畝 (assuming 1 畝 = 240 steps squared as per ancient Chinese units)
a = area_steps_squared / 240

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the area of the field in 畝 as a `Fraction`.
"""


"""
"""
