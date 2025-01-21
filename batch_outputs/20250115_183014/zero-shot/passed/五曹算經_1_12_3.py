"""
今有箕田一頭廣八十六步一頭廣四十步從九十步。問：為田㡬何？
術曰：并二廣得一百二十六步半之得六十三步以從九十步乘之得五千六百七十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a trapezoidal field. The formula for the area of a trapezoid is:

\[
\text{Area} = \frac{\text{Sum of the two parallel sides}}{2} \times \text{Height}
\]

Here is the Python code:


"""


from fractions import Fraction

# Given data
wide1 = 86  # One parallel side in steps
wide2 = 40  # Other parallel side in steps
height = 90  # Height in steps

# Calculate the area in steps²
average_width = Fraction(wide1 + wide2, 2)
area_steps_squared = average_width * height

# Convert steps² to 畝 and 步
# 1 畝 = 240 步²
a = area_steps_squared // 240  # Whole 畝
b = area_steps_squared % 240  # Remaining 步²

# Results
a = int(a)  # Convert to integer for 畝
b = int(b)  # Convert to integer for 步²


"""


After running this code, the variables `a` and `b` will contain the number of 畝 and 步², respectively.
"""


"""
"""
