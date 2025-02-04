"""
今有田形如牛角從五十步口廣二十步。問：為田㡬何？
術曰：列口廣二十步半之得十步以從五十步乘之得五百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will compute the area of a field shaped like a "牛角" (ox horn), which is essentially a trapezoid. The formula for the area of a trapezoid is:

\[
\text{Area} = \frac{\text{Base1} + \text{Base2}}{2} \times \text{Height}
\]

Here, the problem states:
- The wider base ("口廣") is 20 steps.
- The narrower base is assumed to be 0 (as it is not explicitly mentioned, but this is common in ancient problems for "牛角"-shaped fields).
- The height ("五十步") is 50 steps.

The solution involves:
1. Taking half of the wider base (20 steps) to represent the average width.
2. Multiplying this average width by the height (50 steps) to get the area in square steps.
3. Converting the area into 畝 (a traditional Chinese unit of area) using the conversion factor: 1 畝 = 240 square steps.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
wide_base = 20  # steps
height = 50  # steps
conversion_factor = 240  # 1 畝 = 240 square steps

# Step 1: Compute the average width (half of the wide base)
average_width = Fraction(wide_base, 2)

# Step 2: Compute the area in square steps
area_in_square_steps = average_width * height

# Step 3: Convert the area into 畝 and remaining steps
a = area_in_square_steps // conversion_factor  # 畝
b = area_in_square_steps % conversion_factor  # remaining steps

# Results
a = int(a)  # 畝
b = int(b)  # steps
#----- content ends here -----


"""


After running this code:
- `a` will contain the number of 畝.
- `b` will contain the remaining steps.
"""


"""
"""
