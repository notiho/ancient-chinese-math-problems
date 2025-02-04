"""
又有圓田，周一百八十一步，徑六十步三分步之一。問：為田幾何？
術曰：半周半徑相乘得積步。
荅曰： a畝 。
"""

"""
To solve this problem, we need to calculate the area of a circular field. The problem states that the circumference (周) of the circular field is 180 1/3 steps, and the diameter (徑) is 60 1/3 steps. The formula provided states that the area is calculated by multiplying the semi-circumference (半周) by the semi-diameter (半徑).

Here is the Python code to compute the area:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = Fraction(180) + Fraction(1, 3)  # 180 1/3 steps
diameter = Fraction(60) + Fraction(1, 3)        # 60 1/3 steps

# Calculations
semi_circumference = circumference / 2  # 半周
semi_diameter = diameter / 2            # 半徑

# Area calculation
a = semi_circumference * semi_diameter  # Area in 畝

# Result
a  # The area in 畝
#----- content ends here -----


"""


The variable `a` will contain the area of the circular field in 畝.
"""


"""
Variable 'a' has wrong value. Expected: 32761/2880, Actual: 97921/36"""
