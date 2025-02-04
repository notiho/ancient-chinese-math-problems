"""
今有箕田一頭廣八十六步一頭廣四十步從九十步。問：為田㡬何？
術曰：并二廣得一百二十六步半之得六十三步以從九十步乘之得五千六百七十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve the problem, we will calculate the area of the trapezoidal field using the given dimensions. The formula for the area of a trapezoid is:

\[
\text{Area} = \frac{\text{Sum of parallel sides} \times \text{Height}}{2}
\]

Here, the parallel sides are 86 steps and 40 steps, and the height is 90 steps. The area will then be converted into "畝" (Chinese acres) and "步" (steps).

Below is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
parallel_side1 = 86  # in steps
parallel_side2 = 40  # in steps
height = 90          # in steps

# Calculate the area in steps^2
area_steps2 = Fraction(parallel_side1 + parallel_side2, 2) * height

# Conversion factor: 1 畝 = 240 步^2
mu_conversion = 240

# Calculate the area in 畝 and 步
a = area_steps2 // mu_conversion  # Full 畝
b = area_steps2 % mu_conversion   # Remaining 步

# Results
a = int(a)  # Convert to integer for 畝
b = int(b)  # Convert to integer for 步
#----- content ends here -----


"""


After running this code, the values of `a` (畝) and `b` (步) will contain the solution.
"""


"""
"""
