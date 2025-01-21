"""
今有田形如牛角從五十步口廣二十步。問：為田㡬何？
術曰：列口廣二十步半之得十步以從五十步乘之得五百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will compute the area of a field shaped like a "bull's horn," which is essentially a trapezoid. The formula for the area of a trapezoid is:

\[
\text{Area} = \frac{\text{Base1} + \text{Base2}}{2} \times \text{Height}
\]

Here, the problem states:
- The wider base (口廣) is 20 steps.
- The narrower base is half of the wider base, i.e., \( \frac{20}{2} = 10 \) steps.
- The height (五十步) is 50 steps.

The area is then divided by the "畝法" (a unit conversion factor) to express the result in 畝 and 步. In ancient Chinese mathematics, 1 畝 = 240 步.

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given data
base1 = 20  # steps
base2 = Fraction(20, 2)  # half of base1, steps
height = 50  # steps
mu_conversion = 240  # 1 畝 = 240 步

# Calculate the area in 步
area_in_steps = Fraction(base1 + base2, 2) * height

# Convert the area to 畝 and 步
a = area_in_steps // mu_conversion  # 畝
b = area_in_steps % mu_conversion  # 步

# Results
a = int(a)  # 畝
b = int(b)  # 步


"""


After running the code, the values of `a` and `b` will represent the area in 畝 and 步, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 2, Actual: 3
Variable 'b' has wrong value. Expected: 20, Actual: 30"""
