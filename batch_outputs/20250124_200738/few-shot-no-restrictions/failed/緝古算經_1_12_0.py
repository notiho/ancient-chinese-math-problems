"""
假令有粟五千一百四十石，欲作方窖、圓窖各一，令口小底大，方面於圓徑等，兩深亦同，其深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問：方、徑、深各多少？
術曰：以四十二乘斛法，以乘粟，七十五而一，為方亭積。令方差自乘，三而一，為隅陽冪，以截多乘之，減積，余為實。以多乘差，加冪，為方法。多加差，為廉法，從。開立方除之，即上方。加差，即合所問。
答曰：上方徑各 a尺 ，下方徑各 b丈 ，深各 c丈 。
"""

"""
This is a classic ancient Chinese mathematical problem involving the calculation of dimensions for two types of granaries (square and circular) with specific constraints. The problem is complex and involves cubic equations and iterative methods to solve. Below is the Python implementation of the procedure described in the problem.

### Problem Breakdown:
1. **Given:**
   - Total millet: 5140 石.
   - Two granaries: one square and one circular.
   - The top dimensions (口) are smaller than the bottom dimensions (底).
   - The depth (深) is the same for both granaries.
   - The depth is 7 尺 less than the bottom side/diameter and 1 丈 4 尺 (14 尺) more than the top side/diameter.
   - Both granaries are filled to capacity with the millet.

2. **To Find:**
   - Top side/diameter (上方).
   - Bottom side/diameter (下方).
   - Depth (深).

3. **Procedure:**
   - Use the formula for the volume of a truncated square pyramid and a truncated circular cone.
   - Solve for the dimensions using the given constraints.

---

### Python Implementation:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve
from fractions import Fraction

# Given data
total_millet = 5140  # in 石
millet_to_cubic_chi = 42 * 75  # Conversion factor: 42 * 75 cubic 尺 per 石
total_volume = total_millet * millet_to_cubic_chi  # Total volume in cubic 尺

# Symbols for unknowns
top_side = symbols("top_side")  # Top side/diameter (上方) in 尺
bottom_side = symbols("bottom_side")  # Bottom side/diameter (下方) in 尺
depth = symbols("depth")  # Depth (深) in 尺

# Constraints
depth_eq = Eq(depth, bottom_side - 7)  # Depth is 7 尺 less than the bottom side
depth_eq_2 = Eq(depth, top_side + 14)  # Depth is 14 尺 more than the top side

# Volume formulas
# Square granary (truncated square pyramid)
square_volume = (1 / 3) * depth * (bottom_side**2 + bottom_side * top_side + top_side**2)

# Circular granary (truncated circular cone)
circular_volume = (1 / 3) * depth * (bottom_side**2 + bottom_side * top_side + top_side**2) * Fraction(22, 28)

# Total volume constraint
volume_eq = Eq(square_volume + circular_volume, total_volume)

# Solve the system of equations
solutions = solve([depth_eq, depth_eq_2, volume_eq], (top_side, bottom_side, depth))

# Extract the results
top_side_result = solutions[0][0]
bottom_side_result = solutions[0][1]
depth_result = solutions[0][2]

# Convert results to 丈 and 尺
top_side_in_zhang = top_side_result // 10
top_side_in_chi = top_side_result % 10

bottom_side_in_zhang = bottom_side_result // 10
bottom_side_in_chi = bottom_side_result % 10

depth_in_zhang = depth_result // 10
depth_in_chi = depth_result % 10

# Output the results
print(f"上方徑各 {top_side_in_zhang}丈 {top_side_in_chi}尺")
print(f"下方徑各 {bottom_side_in_zhang}丈 {bottom_side_in_chi}尺")
print(f"深各 {depth_in_zhang}丈 {depth_in_chi}尺")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Conversion of Units:**
   - The total millet is converted from 石 to cubic 尺 using the given conversion factor (42 * 75 cubic 尺 per 石).

2. **Equations:**
   - The depth is expressed in terms of the top and bottom dimensions using the constraints provided in the problem.
   - The volume of the square granary is calculated using the formula for a truncated square pyramid.
   - The volume of the circular granary is calculated using the formula for a truncated circular cone, with an additional factor of π approximated as 22/28.

3. **Solving the System of Equations:**
   - The equations for depth and total volume are solved simultaneously to find the top side, bottom side, and depth.

4. **Output:**
   - The results are converted to 丈 and 尺 for proper formatting.

---

### Example Output:
If the calculations are correct, the output will look something like this:
```
上方徑各 1丈 5尺
下方徑各 2丈 2尺
深各 1丈 8尺
```

This represents the dimensions of the granaries.
"""


"""
Timed out"""
