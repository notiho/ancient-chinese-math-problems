"""
假令有粟二萬六千三百四十二石四斗，欲作方窖六、圓窖四，令口小底大，方面與圓徑等，其深亦同，令深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問上下方、深數各多少？
術曰：以四十二乘斛法，以乘粟，三百八十四而一，為方亭積尺。令方差自乘，三而一，為隅陽冪。以多乘之，以減積，余為實。以多乘差，加冪，為方法。又以多加差，為廉法，從。開立方除之，即上方。加差，即合所問。
答曰：方窖上方 a尺 ，下方 b丈 ，深 c丈 ，圓窖上下徑深與方窖同。
"""

"""
This is a complex ancient Chinese mathematical problem involving the calculation of dimensions for square and circular granaries based on a given volume of grain. Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
- **Given:**
  - Total grain: 26,342 石 4 斗.
  - There are 6 square granaries and 4 circular granaries.
  - The square granaries have square bases, and the circular granaries have circular bases.
  - The bases of the square granaries and the diameters of the circular granaries are equal.
  - The depths of all granaries are the same.
  - The depth is 7 尺 less than the bottom side and 1 丈 4 尺 (14 尺) more than the top side.
  - All granaries are filled completely, and the grain is used up exactly.

- **To Find:**
  - The dimensions of the top side, bottom side, and depth of the granaries.

- **Procedure:**
  1. Convert the total grain into 方亭積尺 (cubic chi).
  2. Use the relationships between the dimensions (top side, bottom side, and depth) to set up equations.
  3. Solve for the dimensions.

---

### Step-by-Step Solution in Python:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve
from fractions import Fraction

# Given data
total_grain_stone = 26342  # 石
total_grain_dou = 4  # 斗
granaries_square = 6  # 方窖
granaries_circular = 4  # 圓窖

# Conversion factors
shi_to_dou = 10  # 1 石 = 10 斗
dou_to_cubic_chi = Fraction(42, 384)  # 1 斗 = 42/384 cubic chi

# Convert total grain to cubic chi
total_grain_dou += total_grain_stone * shi_to_dou  # Convert all to 斗
total_grain_cubic_chi = total_grain_dou * dou_to_cubic_chi  # Convert to cubic chi

# Total cubic chi for square granaries
total_square_cubic_chi = total_grain_cubic_chi * Fraction(granaries_square, granaries_square + granaries_circular)

# Variables for dimensions
top_side, bottom_side, depth = symbols('top_side bottom_side depth')

# Relationships between dimensions
depth_eq = Eq(depth, bottom_side - 7)  # Depth is 7 chi less than the bottom side
top_side_eq = Eq(top_side, bottom_side - 14 - 7)  # Top side is 14 chi less than depth

# Volume of a single square granary
volume_eq = Eq((bottom_side**2 + top_side**2 + bottom_side * top_side) * depth / 3, total_square_cubic_chi / granaries_square)

# Solve the equations
solution = solve([depth_eq, top_side_eq, volume_eq], (top_side, bottom_side, depth))

# Extract the results
top_side_result = solution[top_side]
bottom_side_result = solution[bottom_side]
depth_result = solution[depth]

# Output the results
print(f"方窖上方: {top_side_result} 尺")
print(f"方窖下方: {bottom_side_result} 尺")
print(f"方窖深: {depth_result} 尺")
print(f"圓窖上下徑深與方窖同。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Convert Grain Volume:**
   - The total grain is converted from 石 and 斗 into cubic chi using the given conversion factors.

2. **Set Up Equations:**
   - The relationships between the top side, bottom side, and depth are expressed as equations.
   - The volume of a square granary is calculated using the formula for a truncated pyramid:
     \[
     V = \frac{1}{3} \cdot h \cdot (a^2 + b^2 + a \cdot b)
     \]
     where \(a\) is the top side, \(b\) is the bottom side, and \(h\) is the depth.

3. **Solve the Equations:**
   - The equations are solved simultaneously to find the dimensions of the granaries.

4. **Output the Results:**
   - The dimensions of the top side, bottom side, and depth are printed.

---

### Answer Format:
- 方窖上方 \(a\) 尺
- 方窖下方 \(b\) 尺
- 方窖深 \(c\) 尺
- 圓窖上下徑深與方窖同.

Let me know if you need further clarification!
"""


"""
Timed out"""
