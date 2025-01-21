"""
今有環田，中周九十二步，外周一百二十二步，徑五步。問：為田幾何？
術曰：并中外周而半之，以徑乘之為積步。
荅曰： a畝 。
"""

"""
To solve this problem, we need to calculate the area of a ring-shaped field (環田). The problem provides the inner circumference (中周), the outer circumference (外周), and the diameter (徑). The formula for the area is given in the problem: add the inner and outer circumferences, divide by 2 to get the average circumference, and then multiply by the diameter to get the area in square steps (積步). Finally, convert the area from square steps to 畝 (a traditional Chinese unit of area).

1 畝 = 240 square steps.

Here is the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Given data
inner_circumference = 92  # 中周 in steps
outer_circumference = 122  # 外周 in steps
diameter = 5  # 徑 in steps

# Calculate the area in square steps
average_circumference = Fraction(inner_circumference + outer_circumference, 2)
area_in_square_steps = average_circumference * diameter

# Convert square steps to 畝
a = area_in_square_steps / 240

# Result
a


"""


The variable `a` will contain the area of the ring-shaped field in 畝 as a `Fraction`.
"""


"""
"""
