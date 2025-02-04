"""
假令有粟二萬六千三百四十二石四斗，欲作方窖六、圓窖四，令口小底大，方面與圓徑等，其深亦同，令深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問上下方、深數各多少？
答曰：方窖上方 a尺 ，下方 b丈 ，深 c丈 ，圓窖上下徑深與方窖同。
"""

"""
This is a complex problem involving the calculation of the dimensions of square and circular granaries based on the volume of grain. Let us break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Given:**
   - Total grain: 26,342 石 4 斗.
   - There are **6 square granaries** and **4 circular granaries**.
   - The square granaries and circular granaries have the same depth.
   - The bottom (larger) side of the square granary is 7 chi longer than the top (smaller) side.
   - The depth is 1 zhang 4 chi longer than the top side.
   - The circular granaries have the same dimensions as the square granaries (the diameter of the circle corresponds to the side length of the square).

2. **Objective:**
   - Find the dimensions of the square granaries:
     - Top side (`a` chi),
     - Bottom side (`b` zhang),
     - Depth (`c` zhang).

3. **Conversion Factors:**
   - 1 石 = 10 斗.
   - 1 丈 = 10 尺.

4. **Volume Formulas:**
   - Volume of a square granary:
     \[
     V_{\text{square}} = \frac{(a + b)}{2} \cdot c \cdot c
     \]
     where \(a\) is the top side, \(b\) is the bottom side, and \(c\) is the depth.
   - Volume of a circular granary:
     \[
     V_{\text{circle}} = \frac{\pi}{4} \cdot \left(\frac{a + b}{2}\right)^2 \cdot c
     \]
     where \((a + b)/2\) is the average diameter and \(c\) is the depth.

5. **Total Volume:**
   - Total grain volume is distributed among 6 square granaries and 4 circular granaries:
     \[
     6 \cdot V_{\text{square}} + 4 \cdot V_{\text{circle}} = \text{Total Grain Volume}.
     \]

---

### Python Code:


"""


from fractions import Fraction
import math

# Total grain in 石 and 斗
total_grain_stone = 26342
total_grain_dou = 4
total_grain_volume = total_grain_stone * 10 + total_grain_dou  # Convert to 斗

# Conversion factors
chi_to_zhang = Fraction(1, 10)  # 1 chi = 1/10 zhang
zhang_to_chi = 10  # 1 zhang = 10 chi

# Variables
# Let the top side of the square granary be 'a' (in chi)
# Let the bottom side of the square granary be 'b' (in zhang)
# Let the depth of the granary be 'c' (in zhang)

# Relationships
# b = a + 7 (convert 7 chi to zhang)
# c = a + 14 (convert 1 zhang 4 chi to zhang)

# Volume formulas
def square_granary_volume(a):
    b = a + Fraction(7, 10)  # Bottom side in zhang
    c = a + Fraction(14, 10)  # Depth in zhang
    return ((a + b) / 2) * c * c

def circular_granary_volume(a):
    b = a + Fraction(7, 10)  # Bottom side in zhang
    c = a + Fraction(14, 10)  # Depth in zhang
    diameter = (a + b) / 2  # Average diameter in zhang
    return (math.pi / 4) * (diameter ** 2) * c

# Total volume equation
def total_volume(a):
    return 6 * square_granary_volume(a) + 4 * circular_granary_volume(a)

# Solve for 'a' (top side in zhang)
a = Fraction(1, 10)  # Start with a small value (1 chi)
while total_volume(a) < total_grain_volume:
    a += Fraction(1, 10)  # Increment by 1 chi (1/10 zhang)

# Calculate b and c
b = a + Fraction(7, 10)  # Bottom side in zhang
c = a + Fraction(14, 10)  # Depth in zhang

# Convert results to chi for clarity
a_chi = a * zhang_to_chi
b_chi = b * zhang_to_chi
c_chi = c * zhang_to_chi

# Output results
print(f"方窖上方 a = {a_chi} 尺")
print(f"方窖下方 b = {b_chi} 尺")
print(f"方窖深 c = {c_chi} 尺")


"""


---

### Explanation of the Code:
1. The code starts by converting the total grain volume into **斗**.
2. It defines the relationships between the top side (`a`), bottom side (`b`), and depth (`c`) of the granaries.
3. It calculates the volume of both square and circular granaries using the given formulas.
4. It iteratively solves for the top side (`a`) such that the total volume of 6 square granaries and 4 circular granaries equals the total grain volume.
5. Finally, it converts the results into chi for clarity and prints the dimensions.

---

### Output:
The output will provide the dimensions of the square granaries:
- Top side (`a`) in chi,
- Bottom side (`b`) in chi,
- Depth (`c`) in chi.


"""


"""
Variable 'a' has wrong value. Expected: 7, Actual: 149/5
Variable 'b' has wrong value. Expected: 14/5, Actual: 61/2
Variable 'c' has wrong value. Expected: 21/10, Actual: 156/5"""
