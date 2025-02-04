"""
今有環田，中周九十二步，外周一百二十二步，徑五步。問：為田幾何？
術曰：并中外周而半之，以徑乘之為積步。
荅曰： a畝 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a circular field (田) given the inner circumference (中周), outer circumference (外周), and diameter (徑). The formula provided in the problem is to add the inner and outer circumferences, divide by 2 to get the average circumference, and then multiply by the diameter to compute the area in square steps (積步). Finally, we convert the result into 畝 (a traditional Chinese unit of area).

1 畝 = 240 square steps.

Here is the Python code:


"""


from fractions import Fraction

# Given data
inner_circumference = 92  # 中周 in steps
outer_circumference = 122  # 外周 in steps
diameter = 5  # 徑 in steps

# Compute the average circumference
average_circumference = Fraction(inner_circumference + outer_circumference, 2)

# Compute the area in square steps
area_in_square_steps = average_circumference * diameter

# Convert the area to 畝
a = area_in_square_steps / 240

# The solution is stored in variable 'a'
a


"""


The variable `a` will contain the area of the field in 畝 as a `Fraction`.
"""


"""
"""
