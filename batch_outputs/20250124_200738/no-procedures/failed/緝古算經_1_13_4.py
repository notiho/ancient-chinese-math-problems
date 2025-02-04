"""
假令有粟二萬六千三百四十二石四斗，欲作方窖六、圓窖四，令口小底大，方面與圓徑等，其深亦同，令深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問上下方、深數各多少？
答曰：方窖上方 a尺 ，下方 b丈 ，深 c丈 ，圓窖上下徑深與方窖同。
"""

"""
This is a classic ancient Chinese mathematical problem involving the calculation of the dimensions of square and circular granaries based on the volume of grain they can hold. Let's break it down and solve it step by step.

---

### Problem Breakdown:
1. **Given:**
   - Total grain: 26,342 石 4 斗.
   - There are 6 square granaries and 4 circular granaries.
   - The square granaries have a smaller top side and a larger bottom side, with the depth being the same for all granaries.
   - The circular granaries have the same dimensions as the square granaries (in terms of diameter and depth).

2. **Relationships:**
   - The depth is 7 尺 less than the bottom side and 1 丈 4 尺 (14 尺) more than the top side.
   - The total volume of the granaries must equal the total volume of the grain.

3. **Objective:**
   - Find the dimensions of the square granaries:
     - Top side (上方): `a 尺`
     - Bottom side (下方): `b 丈`
     - Depth (深): `c 丈`

   - The circular granaries will have the same dimensions as the square granaries.

---

### Assumptions and Conversions:
1. 1 石 = 10 斗.
2. 1 丈 = 10 尺.
3. The volume of a square granary is calculated as:
   \[
   V_{\text{square}} = \frac{(上方^2 + 上方 \times 下方 + 下方^2) \times 深}{3}
   \]
4. The volume of a circular granary is calculated as:
   \[
   V_{\text{circle}} = \frac{\pi \times (上方^2 + 上方 \times 下方 + 下方^2) \times 深}{12}
   \]
5. Total volume of grain:
   \[
   V_{\text{total}} = 26,342 \times 10 + 4 = 263,424 \, \text{斗}.
   \]

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Total grain in dou
total_grain = 26342 * 10 + 4

# Number of square and circular granaries
num_square = 6
num_circle = 4

# Volume formulas for square and circular granaries
def square_granary_volume(top, bottom, depth):
    return Fraction((top**2 + top * bottom + bottom**2) * depth, 3)

def circular_granary_volume(top, bottom, depth):
    return Fraction(math.pi * (top**2 + top * bottom + bottom**2) * depth, 12)

# Relationships
# depth = bottom - 7 (in chi)
# depth = top + 14 (in chi)

# Solve for dimensions
for top in range(1, 100):  # Iterate over possible top side values in chi
    for bottom in range(top, 200):  # Bottom must be larger than top
        depth = bottom - 7  # Depth in chi
        if depth != top + 14:
            continue  # Skip if the relationship doesn't hold

        # Calculate volumes
        square_volume = square_granary_volume(top, bottom, depth)
        circle_volume = circular_granary_volume(top, bottom, depth)

        # Total volume of all granaries
        total_volume = num_square * square_volume + num_circle * circle_volume

        # Check if the total volume matches the grain volume
        if total_volume == total_grain:
            # Convert bottom and depth to zhang (1 zhang = 10 chi)
            bottom_in_zhang = Fraction(bottom, 10)
            depth_in_zhang = Fraction(depth, 10)

            # Output the results
            print(f"方窖上方 a = {top} 尺")
            print(f"方窖下方 b = {bottom_in_zhang} 丈")
            print(f"方窖深 c = {depth_in_zhang} 丈")
            break
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Volume Formulas:** The formulas for the volumes of square and circular granaries are implemented as functions.
2. **Relationships:** The depth is calculated based on the relationships given in the problem.
3. **Iterative Search:** The program iterates over possible values for the top and bottom sides, checking if the relationships hold and if the total volume matches the grain volume.
4. **Output:** Once the correct dimensions are found, they are printed.

---

### Expected Output:
The program will output the dimensions of the square granaries:
- Top side (a) in chi.
- Bottom side (b) in zhang.
- Depth (c) in zhang.

The circular granaries will have the same dimensions as the square granaries.
"""


"""
Code error: both arguments should be Rational instances"""
