"""
今有簫田從四十八步一頭廣二十五步一頭廣三十五步。問：為田㡬何？
術曰：并二廣得六十步半之得三十步以從四十八步乘之得一千四百四十步以畝法除之即得。
答曰： a畝
"""

"""
To solve this problem, we need to calculate the area of a trapezoidal field. The formula for the area of a trapezoid is:

\[
\text{Area} = \frac{\text{Sum of parallel sides} \times \text{Height}}{2}
\]

Here, the two parallel sides are 25 steps and 35 steps, and the height is 48 steps. The area is then converted into "畝" (a traditional Chinese unit of area).

Here is the Python code:


"""


from fractions import Fraction

# Given values
parallel_side1 = 25  # in steps
parallel_side2 = 35  # in steps
height = 48  # in steps

# Calculate the area in square steps
area_in_square_steps = Fraction(parallel_side1 + parallel_side2, 2) * height

# Conversion factor: 1 畝 = 240 square steps
conversion_factor = 240

# Convert the area to 畝
a = area_in_square_steps / conversion_factor

# The result is stored in variable 'a'


"""


The variable `a` now contains the area of the field in 畝 as a `Fraction`.
"""


"""
"""
