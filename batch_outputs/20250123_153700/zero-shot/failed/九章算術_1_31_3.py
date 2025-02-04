"""
又有圓田，周一百八十一步，徑六十步三分步之一。問：為田幾何？
術曰：半周半徑相乘得積步。
荅曰： a畝 。
"""

"""
To solve this problem, we will calculate the area of a circular field based on the given information. The circumference (周) is 180.5 steps, and the diameter (徑) is 60 + 1/3 steps. The formula for the area of a circle is given as:

Area = (半周 * 半徑)

Here is the Python code to compute the area:


"""


from fractions import Fraction

# Given values
circumference = Fraction(180.5)  # 周 (circumference)
diameter = Fraction(60) + Fraction(1, 3)  # 徑 (diameter)

# Calculations
radius = diameter / 2  # 半徑 (radius)
semi_circumference = circumference / 2  # 半周 (semi-circumference)
a = semi_circumference * radius  # Area in steps squared

# Result
a  # The area in 畝


"""


The variable `a` will contain the area of the circular field in 畝.
"""


"""
Variable 'a' has wrong value. Expected: 32761/2880, Actual: 65341/24"""
