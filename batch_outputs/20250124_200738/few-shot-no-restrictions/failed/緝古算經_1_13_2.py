"""
假令有粟二萬六千三百四十二石四斗，欲作方窖六、圓窖四，令口小底大，方面與圓徑等，其深亦同，令深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問上下方、深數各多少？
術曰：以四十二乘斛法，以乘粟，三百八十四而一，為方亭積尺。令方差自乘，三而一，為隅陽冪。以多乘之，以減積，余為實。以多乘差，加冪，為方法。又以多加差，為廉法，從。開立方除之，即上方。加差，即合所問。
答曰：方窖上方 a尺 ，下方 b丈 ，深 c丈 ，圓窖上下徑深與方窖同。
"""

"""
This is a complex ancient Chinese mathematical problem involving the calculation of dimensions for square and circular granaries (窖) based on a given volume of grain. Let's break it down step by step and encode it into Python.

---

### Problem Breakdown:
1. **Given:**
   - Total grain: `26342石4斗` (convert to cubic chi).
   - There are 6 square granaries and 4 circular granaries.
   - The square granaries and circular granaries have the same depth, and the bottom is larger than the top.
   - The depth is 7 chi less than the bottom side and 14 chi more than the top side.
   - The granaries are filled completely with the grain.

2. **Goal:**
   - Find the dimensions of the top side, bottom side, and depth of the granaries.

3. **Procedure:**
   - Convert the total grain into cubic chi using the conversion factor for 石 and 斗.
   - Use the formulas provided in the problem to calculate the dimensions:
     - Use the formula for the volume of a square granary.
     - Solve the cubic equation to find the top side, then calculate the bottom side and depth.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from sympy import symbols, solve, Eq

# Conversion factors
石_to_斗 = 10  # 1 石 = 10 斗
斗_to_升 = 10  # 1 斗 = 10 升
升_to_立方尺 = Fraction(1, 10)  # 1 升 = 1/10 立方尺

# Total grain in 石 and 斗
total_grain_石 = 26342
total_grain_斗 = 4

# Convert total grain to cubic chi (立方尺)
total_grain_立方尺 = (total_grain_石 * 石_to_斗 + total_grain_斗) * 斗_to_升 * 升_to_立方尺

# Number of granaries
square_granaries = 6
circular_granaries = 4

# Total volume for square granaries and circular granaries
square_granary_volume = total_grain_立方尺 * Fraction(6, 10)  # 60% for square granaries
circular_granary_volume = total_grain_立方尺 * Fraction(4, 10)  # 40% for circular granaries

# Variables for the dimensions
top_side = symbols('top_side')  # 上方 (top side of the square granary)
bottom_side = top_side + 7 + 14  # 下方 (bottom side of the square granary)
depth = bottom_side - 7  # 深 (depth of the granary)

# Volume formula for a square granary
# Volume = depth * (top_side^2 + top_side * bottom_side + bottom_side^2) / 3
volume_formula = depth * (top_side**2 + top_side * bottom_side + bottom_side**2) / 3

# Total volume for one square granary
one_square_granary_volume = square_granary_volume / square_granaries

# Solve the equation
equation = Eq(volume_formula, one_square_granary_volume)
solution = solve(equation, top_side)

# Extract the positive solution for the top side
top_side_solution = max([sol.evalf() for sol in solution if sol.is_real and sol > 0])

# Calculate the bottom side and depth
bottom_side_solution = top_side_solution + 7 + 14
depth_solution = bottom_side_solution - 7

# Output the results
a = top_side_solution
b = bottom_side_solution / 10  # Convert chi to zhang
c = depth_solution / 10  # Convert chi to zhang

print(f"方窖上方 a = {a:.2f} 尺")
print(f"方窖下方 b = {b:.2f} 丈")
print(f"方窖深 c = {c:.2f} 丈")
print("圓窖上下徑深與方窖同。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Conversion of Grain Volume:**
   - The total grain is converted from 石 and 斗 into cubic chi (立方尺) using the given conversion factors.

2. **Granary Volume Distribution:**
   - The total grain volume is divided into 60% for square granaries and 40% for circular granaries.

3. **Volume Formula:**
   - The formula for the volume of a square granary is used:
     \[
     V = \frac{\text{depth} \cdot (\text{top\_side}^2 + \text{top\_side} \cdot \text{bottom\_side} + \text{bottom\_side}^2)}{3}
     \]

4. **Cubic Equation:**
   - The equation is solved for the top side (`top_side`), and the positive real solution is selected.

5. **Calculate Bottom Side and Depth:**
   - Using the relationships between the top side, bottom side, and depth, the other dimensions are calculated.

6. **Final Output:**
   - The dimensions are printed in chi (尺) and zhang (丈), as required.

---

### Example Output:
```
方窖上方 a = 12.34 尺
方窖下方 b = 1.56 丈
方窖深 c = 1.23 丈
圓窖上下徑深與方窖同。
```

This code provides the dimensions of the square and circular granaries based on the given problem.
"""


"""
Variable 'a' has wrong value. Expected: 7, Actual: 17.6879017305206
Variable 'b' has wrong value. Expected: 14/5, Actual: 3.86879017305206
Variable 'c' has wrong value. Expected: 21/10, Actual: 3.16879017305206"""
