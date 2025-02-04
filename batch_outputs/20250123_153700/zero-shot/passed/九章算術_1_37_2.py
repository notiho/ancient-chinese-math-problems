"""
又有環田，中周六十二步、四分步之三，外周一百一十三步、二分步之一，徑十二步、三分步之二。問：為田幾何？
術曰：并中外周而半之，以徑乘之為積步。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a circular field, given the inner circumference, outer circumference, and diameter. The formula provided in the problem is to take the average of the inner and outer circumferences, multiply it by the diameter, and then divide by 4 to convert the result into "畝" (a traditional Chinese unit of area).

Here is the Python code:


"""


from fractions import Fraction

# Given values
inner_circumference = Fraction(62, 1) + Fraction(3, 4)  # 中周六十二步、四分步之三
outer_circumference = Fraction(113, 1) + Fraction(1, 2)  # 外周一百一十三步、二分步之一
diameter = Fraction(12, 1) + Fraction(2, 3)  # 徑十二步、三分步之二

# Calculate the average circumference
average_circumference = (inner_circumference + outer_circumference) / 2

# Calculate the area in "步" (square steps)
area_in_steps = average_circumference * diameter

# Convert the area to "畝" (1 畝 = 240 square steps)
a = area_in_steps / 240

# The result is stored in variable 'a'


"""


The variable `a` contains the area of the field in "畝".
"""


"""
"""
