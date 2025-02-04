"""
假令有粟五千一百四十石，欲作方窖、圓窖各一，令口小底大，方面於圓徑等，兩深亦同，其深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問：方、徑、深各多少？
術曰：以四十二乘斛法，以乘粟，七十五而一，為方亭積。令方差自乘，三而一，為隅陽冪，以截多乘之，減積，余為實。以多乘差，加冪，為方法。多加差，為廉法，從。開立方除之，即上方。加差，即合所問。
答曰：上方徑各 a尺 ，下方徑各 b丈 ，深各 c丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving the calculation of dimensions for two grain storage pits (one square and one circular) with specific geometric and volumetric constraints. Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Given:**
   - Total grain: 5140 石.
   - Two pits: one square and one circular.
   - The pits have the same depth, and the square's side length equals the circular pit's diameter.
   - The depth is 7 尺 less than the bottom side/diameter and 1 丈 4 尺 (14 尺) more than the top side/diameter.
   - Both pits are filled to capacity, and the grain is exactly used up.

2. **Goal:**
   - Find the dimensions of the pits:
     - Top side/diameter (`a` 尺),
     - Bottom side/diameter (`b` 丈),
     - Depth (`c` 丈).

3. **Procedure:**
   - Use the formula for volume of truncated square and circular pyramids.
   - Solve for the unknown dimensions using the given constraints.

---

### Python Code Implementation:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve
from fractions import Fraction

# Given data
total_grain = 5140  # in 石
斛法 = 42  # Conversion factor for 石 to cubic 尺
粟 = total_grain * 斛法  # Total volume in cubic 尺

# Variables to solve for
a, b, c = symbols('a b c')  # a: top side/diameter, b: bottom side/diameter, c: depth

# Relationships
depth_difference_top = Fraction(14, 10)  # 1丈4尺 = 14尺 = 1.4丈
depth_difference_bottom = Fraction(7, 10)  # 7尺 = 0.7丈

# Depth in terms of top and bottom dimensions
depth = b - depth_difference_bottom  # Depth is 7尺 less than the bottom
depth_eq = Eq(c, depth)  # c = depth

# Square pit volume formula (truncated square pyramid)
square_volume = (c / 3) * (a**2 + a * b + b**2)

# Circular pit volume formula (truncated circular cone)
circular_volume = (c / 3) * (Fraction(22, 7)) * (a**2 + a * b + b**2) / 4

# Total volume constraint
total_volume_eq = Eq(square_volume + circular_volume, 粟)

# Solve the equations
solutions = solve([depth_eq, total_volume_eq], (a, b, c))

# Extract the results
a_result = solutions[0][0]  # Top side/diameter
b_result = solutions[0][1]  # Bottom side/diameter
c_result = solutions[0][2]  # Depth

# Convert results to appropriate units
a_result_尺 = a_result
b_result_丈 = b_result
c_result_丈 = c_result

# Output the results
print(f"Top side/diameter (a): {a_result_尺} 尺")
print(f"Bottom side/diameter (b): {b_result_丈} 丈")
print(f"Depth (c): {c_result_丈} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Volume Formulas:**
   - The square pit's volume is calculated using the formula for a truncated square pyramid.
   - The circular pit's volume is calculated using the formula for a truncated circular cone.

2. **Depth Relationship:**
   - The depth is expressed in terms of the top and bottom dimensions using the given constraints.

3. **Total Volume Constraint:**
   - The sum of the volumes of the two pits equals the total grain volume (converted to cubic 尺).

4. **Symbolic Solution:**
   - The `sympy` library is used to solve the system of equations symbolically.

5. **Units:**
   - Results are converted to the appropriate units (尺 for `a`, 丈 for `b` and `c`).

---

### Output:
The code will output the values of `a`, `b`, and `c` in their respective units:
- `a`: Top side/diameter in 尺.
- `b`: Bottom side/diameter in 丈.
- `c`: Depth in 丈.


"""


"""
Variable 'a' has wrong value. Expected: 7, Actual: a
Variable 'b' has wrong value. Expected: 14/5, Actual: b
Variable 'c' has wrong value. Expected: 21/10, Actual: c"""
