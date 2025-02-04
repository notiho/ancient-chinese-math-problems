"""
今有環田，中周九十二步，外周一百二十二步，徑五步。問：為田幾何？
術曰：并中外周而半之，以徑乘之為積步。
荅曰： a畝 。
"""

"""
To solve this problem, we will calculate the area of the ring-shaped field (環田). The problem provides the inner circumference (中周), the outer circumference (外周), and the diameter (徑). The formula for the area is given in the problem: 

1. Add the inner and outer circumferences.
2. Divide the sum by 2 to get the average circumference.
3. Multiply the average circumference by the diameter to get the area in square steps (積步).
4. Convert the area from square steps to 畝 (1 畝 = 240 square steps).

Here is the Python code:


"""


from fractions import Fraction

# Given values
inner_circumference = 92  # 中周 in steps
outer_circumference = 122  # 外周 in steps
diameter = 5  # 徑 in steps

# Step-by-step calculation
average_circumference = Fraction(inner_circumference + outer_circumference, 2)  # 平均周長
area_in_square_steps = average_circumference * diameter  # 積步
a = area_in_square_steps / 240  # Convert to 畝 (1 畝 = 240 square steps)

# The result is stored in variable 'a'


"""


The variable `a` will contain the area of the field in 畝 as a `Fraction`.
"""


"""
"""
