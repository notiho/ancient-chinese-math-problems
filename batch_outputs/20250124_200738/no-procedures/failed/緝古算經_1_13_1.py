"""
假令有粟二萬六千三百四十二石四斗，欲作方窖六、圓窖四，令口小底大，方面與圓徑等，其深亦同，令深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問上下方、深數各多少？
答曰：方窖上方 a尺 ，下方 b丈 ，深 c丈 ，圓窖上下徑深與方窖同。
"""

"""
This is a classic ancient Chinese mathematics problem involving the calculation of dimensions for square and circular granaries. Let's break it down and solve it step by step.

---

### Problem Breakdown:
1. **Given:**
   - Total millet volume: 26342 石 4 斗.
   - 6 square granaries and 4 circular granaries.
   - The square granaries are square in shape, and the circular granaries are cylindrical.
   - The top side (upper square) is smaller than the bottom side (lower square) by 7 尺.
   - The depth is 1 丈 4 尺 (14 尺) greater than the top side.
   - The depth is the same for both square and circular granaries.
   - The total volume of millet is evenly distributed among the granaries.

2. **To Find:**
   - The dimensions of the square granaries:
     - Top side (上方, `a` 尺),
     - Bottom side (下方, `b` 丈),
     - Depth (深, `c` 丈).
   - The circular granaries have the same depth and diameter as the square granaries.

3. **Key Relationships:**
   - Volume of a square granary = \( \frac{1}{3} \times \text{depth} \times (\text{top side}^2 + \text{top side} \times \text{bottom side} + \text{bottom side}^2) \).
   - Volume of a circular granary = \( \frac{1}{3} \times \pi \times \text{depth} \times (\text{top radius}^2 + \text{top radius} \times \text{bottom radius} + \text{bottom radius}^2) \).
   - 1 石 = 10 斗.

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Total millet volume in cubic chi
total_volume = 26342 * 10 + 4  # Convert 石 and 斗 to cubic chi

# Number of square and circular granaries
square_granaries = 6
circular_granaries = 4

# Volume per granary
volume_per_granary = Fraction(total_volume, square_granaries + circular_granaries)

# Relationships
# Let the top side of the square granary = a 尺
# Bottom side of the square granary = b 尺 = a + 7
# Depth of the granary = c 尺 = a + 14

# Volume of a square granary:
# V = (1/3) * depth * (top_side^2 + top_side * bottom_side + bottom_side^2)
# V = (1/3) * c * (a^2 + a * b + b^2)

# Substitute b = a + 7 and c = a + 14 into the volume equation
# V = (1/3) * (a + 14) * (a^2 + a * (a + 7) + (a + 7)^2)

# Simplify the equation
# V = (1/3) * (a + 14) * (a^2 + a^2 + 7a + a^2 + 14a + 49)
# V = (1/3) * (a + 14) * (3a^2 + 21a + 49)
# V = (a + 14) * (a^2 + 7a + Fraction(49, 3))

# Solve for a such that the volume equals volume_per_granary
for a in range(1, 100):  # Test integer values for a
    top_side = a
    bottom_side = a + 7
    depth = a + 14
    volume = Fraction(1, 3) * depth * (top_side**2 + top_side * bottom_side + bottom_side**2)
    if volume == volume_per_granary:
        break

# Results
a = top_side  # Top side of the square granary in chi
b = Fraction(bottom_side, 10)  # Bottom side in zhang
c = Fraction(depth, 10)  # Depth in zhang

# Output
print(f"方窖上方 a = {a} 尺")
print(f"方窖下方 b = {b} 丈")
print(f"方窖深 c = {c} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Volume Calculation:**
   - The formula for the volume of a square granary is derived from the ancient Chinese formula for a truncated pyramid.
   - The bottom side and depth are expressed in terms of the top side.

2. **Iterative Solution:**
   - The code iterates over possible values for the top side (`a`) and calculates the corresponding bottom side, depth, and volume.
   - It checks when the calculated volume matches the required volume per granary.

3. **Conversion to Appropriate Units:**
   - The bottom side and depth are converted to 丈 (1 丈 = 10 尺).

---

### Final Answer:
The program will output the dimensions:
- 方窖上方 \( a \) 尺,
- 方窖下方 \( b \) 丈,
- 方窖深 \( c \) 丈.
"""


"""
Variable 'a' has wrong value. Expected: 7, Actual: 99
Variable 'b' has wrong value. Expected: 14/5, Actual: 53/5
Variable 'c' has wrong value. Expected: 21/10, Actual: 113/10"""
