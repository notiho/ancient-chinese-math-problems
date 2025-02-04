"""
今有環田外周三十步內周一十二步徑三步。問：為田㡬何？
術曰：并內外周得四十二步半之得二十一步以徑三步乘之即得。
答曰： a步 。
"""

"""
To solve this problem, we will calculate the area of the ring-shaped field (環田). The problem provides the outer circumference (外周), inner circumference (內周), and the diameter (徑). The formula for the area of a ring is derived from the difference between the areas of the outer and inner circles.

### Given:
- Outer circumference (外周) = 30 steps
- Inner circumference (內周) = 12 steps
- Diameter (徑) = 3 steps

### Steps:
1. Calculate the radius of the outer circle:
   \[
   r_{\text{outer}} = \frac{\text{Outer circumference}}{2\pi}
   \]

2. Calculate the radius of the inner circle:
   \[
   r_{\text{inner}} = \frac{\text{Inner circumference}}{2\pi}
   \]

3. Compute the area of the ring:
   \[
   \text{Area of ring} = \pi \cdot (r_{\text{outer}}^2 - r_{\text{inner}}^2)
   \]

4. Substitute \(\pi = \frac{22}{7}\) as per ancient Chinese mathematics.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
outer_circumference = Fraction(30)  # steps
inner_circumference = Fraction(12)  # steps
diameter = Fraction(3)  # steps

# Pi approximation
pi = Fraction(22, 7)

# Calculate radii
r_outer = outer_circumference / (2 * pi)
r_inner = inner_circumference / (2 * pi)

# Calculate the area of the ring
a = pi * (r_outer**2 - r_inner**2)

# The answer is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the area of the ring in square steps.
"""


"""
Variable 'a' has wrong value. Expected: 63, Actual: 1323/22"""
