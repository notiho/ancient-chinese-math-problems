"""
假令有粟五千一百四十石，欲作方窖、圓窖各一，令口小底大，方面於圓徑等，兩深亦同，其深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問：方、徑、深各多少？
術曰：以四十二乘斛法，以乘粟，七十五而一，為方亭積。令方差自乘，三而一，為隅陽冪，以截多乘之，減積，余為實。以多乘差，加冪，為方法。多加差，為廉法，從。開立方除之，即上方。加差，即合所問。
答曰：上方徑各 a尺 ，下方徑各 b丈 ，深各 c丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving the calculation of dimensions for a square and circular granary based on given conditions. Let's break it down and translate it into Python code step by step.

---

### Problem Breakdown:
1. **Given:**
   - Total millet: 5140 石.
   - Two granaries: one square and one circular.
   - Both granaries have:
     - The same depth.
     - The same top dimensions (square side = circular diameter).
   - The depth is:
     - 7 尺 less than the bottom dimensions.
     - 1 丈 4 尺 (14 尺) more than the top dimensions.
   - Both granaries are filled completely with millet.

2. **Goal:**
   - Find:
     - Top dimensions (square side and circular diameter).
     - Bottom dimensions.
     - Depth.

3. **Procedure:**
   - Use the formula for volume of square and circular granaries.
   - Solve for the unknown dimensions using the given relationships and millet volume.

---

### Translation into Python Code:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve
from fractions import Fraction

# Step 1: Define variables
上方 = symbols("上方")  # Top dimension (square side or circular diameter) in 尺
下方 = symbols("下方")  # Bottom dimension in 尺
深 = symbols("深")      # Depth in 尺

# Step 2: Define relationships
# Depth is 7 尺 less than the bottom dimension
eq1 = Eq(深, 下方 - 7)

# Depth is 14 尺 more than the top dimension
eq2 = Eq(深, 上方 + 14)

# Step 3: Volume formulas
# Total millet: 5140 石
# 1 石 = 10 斛, and 1 斛 = 42 cubic 尺
total_volume = 5140 * 10 * 42  # in cubic 尺

# Volume of square granary
square_volume = (上方**2 + 上方 * 下方 + 下方**2) * 深 / 3

# Volume of circular granary
circular_volume = (上方**2 + 上方 * 下方 + 下方**2) * 深 / 3 * Fraction(11, 14)

# The total volume is split equally between the two granaries
eq3 = Eq(square_volume + circular_volume, total_volume)

# Step 4: Solve the equations
solution = solve([eq1, eq2, eq3], (上方, 下方, 深))

# Step 5: Extract results
上方_value = solution[0][0]  # Top dimension
下方_value = solution[0][1]  # Bottom dimension
深_value = solution[0][2]    # Depth

# Convert results to 丈 and 尺 for final answer
def convert_to_zhang_and_chi(value):
    zhang = value // 10  # 1 丈 = 10 尺
    chi = value % 10
    return f"{zhang}丈 {chi}尺"

# Final results
上方_result = convert_to_zhang_and_chi(上方_value)
下方_result = convert_to_zhang_and_chi(下方_value)
深_result = convert_to_zhang_and_chi(深_value)

# Print the results
print(f"上方徑各 {上方_result} ，下方徑各 {下方_result} ，深各 {深_result} 。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Variables:**
   - `上方` represents the top dimension (square side or circular diameter).
   - `下方` represents the bottom dimension.
   - `深` represents the depth.

2. **Equations:**
   - `eq1` and `eq2` encode the relationships between depth, top, and bottom dimensions.
   - `eq3` ensures the total volume of millet is split equally between the square and circular granaries.

3. **Volume Formulas:**
   - The volume of the square granary is calculated using the formula for a truncated square pyramid.
   - The volume of the circular granary is calculated similarly, with an adjustment for the circular base.

4. **Solution:**
   - The equations are solved simultaneously to find the values of `上方`, `下方`, and `深`.

5. **Conversion:**
   - The results are converted from 尺 to 丈 and 尺 for the final answer.

---

### Final Output:
The program will output the dimensions of the top, bottom, and depth in the format:
```
上方徑各 a丈 b尺 ，下方徑各 c丈 d尺 ，深各 e丈 f尺 。
```
"""


"""
Timed out"""
