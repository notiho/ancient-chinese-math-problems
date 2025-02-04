"""
今有環田，中周九十二步，外周一百二十二步，徑五步。問：為田幾何？
術曰：并中外周而半之，以徑乘之為積步。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a circular field with an inner circumference (中周) of 92 steps, an outer circumference (外周) of 122 steps, and a diameter (徑) of 5 steps. The goal is to calculate the area of the field in terms of "畝" (a traditional Chinese unit of area).

The method described in the problem is as follows:
1. Add the inner and outer circumferences together.
2. Divide the sum by 2 to get the average circumference.
3. Multiply the average circumference by the diameter to calculate the area in "積步" (step-squared).
4. Convert the area from "積步" to "畝". The conversion factor is typically 240 "積步" per "畝".

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
inner_circumference = 92  # 中周 (steps)
outer_circumference = 122  # 外周 (steps)
diameter = 5  # 徑 (steps)

# Step 1: Calculate the average circumference
average_circumference = Fraction(inner_circumference + outer_circumference, 2)

# Step 2: Calculate the area in step-squared (積步)
area_in_steps_squared = average_circumference * diameter

# Step 3: Convert the area to 畝 (1 畝 = 240 積步)
a = area_in_steps_squared / 240

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the area of the field in "畝" as a `Fraction`.
"""


"""
"""
