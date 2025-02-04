"""
今有箕田一頭廣八十六步一頭廣四十步從九十步。問：為田㡬何？
術曰：并二廣得一百二十六步半之得六十三步以從九十步乘之得五千六百七十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we need to compute the area of the trapezoidal field (箕田). The formula for the area of a trapezoid is:

\[
\text{Area} = \frac{\text{Sum of parallel sides} \times \text{Height}}{2}
\]

Here:
- One parallel side is 86 steps (步),
- The other parallel side is 40 steps (步),
- The height (distance between the parallel sides) is 90 steps (步).

The area is then converted into "畝" (a traditional Chinese unit of area) and "步" (a smaller unit of area). The conversion rule is:
1 畝 = 240 步.

Let's compute this in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
parallel_side1 = 86  # in steps
parallel_side2 = 40  # in steps
height = 90  # in steps
conversion_factor = 240  # 1 畝 = 240 步

# Compute the area in steps
area_in_steps = Fraction(parallel_side1 + parallel_side2, 2) * height

# Convert the area into 畝 and 步
a = area_in_steps // conversion_factor  # Full 畝
b = area_in_steps % conversion_factor  # Remaining 步

# Results
a = int(a)  # 畝
b = int(b)  # 步
#----- content ends here -----


"""


The variables `a` and `b` will contain the number of 畝 and the remaining 步, respectively.
"""


"""
"""
