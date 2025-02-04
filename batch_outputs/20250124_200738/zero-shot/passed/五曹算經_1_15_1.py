"""
今有田形如牛角從五十步口廣二十步。問：為田㡬何？
術曰：列口廣二十步半之得十步以從五十步乘之得五百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will compute the area of a field shaped like a "牛角" (ox horn), which is a trapezoid. The formula for the area of a trapezoid is:

\[
\text{Area} = \frac{\text{(Base1 + Base2)}}{2} \times \text{Height}
\]

Here, the problem states:
- The width at the narrow end (Base1) is \( 0 \) (implicitly).
- The width at the wide end (Base2) is \( 20 \) steps.
- The length (Height) is \( 50 \) steps.

The area is then converted into "畝" (a traditional Chinese unit of area) using the "畝法" (conversion factor). In ancient Chinese mathematics, 1 畝 = 240 步².

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
base1 = 0  # Narrow end width in steps
base2 = 20  # Wide end width in steps
height = 50  # Length of the field in steps
conversion_factor = 240  # 1 畝 = 240 步²

# Compute the area in 步²
area_in_steps = Fraction((base1 + base2), 2) * height

# Convert the area to 畝 and 步
a = area_in_steps // conversion_factor  # Whole 畝
b = area_in_steps % conversion_factor  # Remaining 步

# Results
a, b
#----- content ends here -----


"""


This will compute the values of \( a \) (whole 畝) and \( b \) (remaining 步).
"""


"""
"""
