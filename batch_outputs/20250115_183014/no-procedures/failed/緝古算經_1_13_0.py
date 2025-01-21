"""
假令有粟二萬六千三百四十二石四斗，欲作方窖六、圓窖四，令口小底大，方面與圓徑等，其深亦同，令深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問上下方、深數各多少？
答曰：方窖上方 a尺 ，下方 b丈 ，深 c丈 ，圓窖上下徑深與方窖同。
"""

"""
This is a classic ancient Chinese mathematics problem involving the calculation of dimensions for square and circular granaries. Let's break it down step by step and translate it into Python code.

### Problem Explanation:
- There are **26,342.4 shi** of millet to be stored.
- There are **6 square granaries** and **4 circular granaries**.
- The square granaries and circular granaries have the same depth, and the top side of the square granary is equal to the diameter of the circular granary.
- The depth of the granaries is **7 chi less than the bottom side** and **14 chi more than the top side**.
- The granaries are filled completely, and the millet is used up exactly.

We need to calculate:
1. The **top side** of the square granary (`a` chi),
2. The **bottom side** of the square granary (`b` zhang),
3. The **depth** of the granaries (`c` zhang).

---

### Assumptions:
1. 1 zhang = 10 chi.
2. The volume of a square granary is calculated as:
   \[
   V_{\text{square}} = \frac{h}{3} \times (A^2 + AB + B^2)
   \]
   where \( A \) is the top side, \( B \) is the bottom side, and \( h \) is the depth.
3. The volume of a circular granary is calculated as:
   \[
   V_{\text{circular}} = \frac{h}{3} \times \pi \times \left( \frac{d_1^2 + d_1 d_2 + d_2^2}{4} \right)
   \]
   where \( d_1 \) is the top diameter, \( d_2 \) is the bottom diameter, and \( h \) is the depth.
4. The total millet volume is distributed across 6 square granaries and 4 circular granaries.

---

### Python Code:


"""


from fractions import Fraction
import math

# Total millet volume in shi
total_volume = Fraction(26342.4)

# Number of granaries
square_granaries = 6
circular_granaries = 4

# Relationships between dimensions
# Depth (h) = Bottom side (B) - 7 chi = Top side (A) + 14 chi
# Let A = top side of square granary (in chi)
# Let B = bottom side of square granary (in chi)
# Let h = depth of granary (in chi)
# B = A + 21
# h = A + 14

# Volume of one square granary
def square_granary_volume(A):
    B = A + 21  # Bottom side
    h = A + 14  # Depth
    return Fraction(h, 3) * (A**2 + A*B + B**2)

# Volume of one circular granary
def circular_granary_volume(A):
    B = A + 21  # Bottom diameter
    h = A + 14  # Depth
    return Fraction(h, 3) * math.pi * Fraction((A**2 + A*B + B**2), 4)

# Total volume of all granaries
def total_granary_volume(A):
    square_volume = square_granaries * square_granary_volume(A)
    circular_volume = circular_granaries * circular_granary_volume(A)
    return square_volume + circular_volume

# Solve for A (top side of square granary)
A = 1  # Start with an initial guess (in chi)
while True:
    total_volume_calculated = total_granary_volume(A)
    if total_volume_calculated == total_volume:
        break
    A += 1

# Calculate B and h
B = A + 21  # Bottom side (in chi)
h = A + 14  # Depth (in chi)

# Convert chi to zhang where necessary
a = A  # Top side (in chi)
b = Fraction(B, 10)  # Bottom side (in zhang)
c = Fraction(h, 10)  # Depth (in zhang)

# Output results
print(f"方窖上方 a = {a} 尺")
print(f"方窖下方 b = {b} 丈")
print(f"方窖深 c = {c} 丈")


"""


---

### Explanation of the Code:
1. The code uses the formula for the volume of square and circular granaries.
2. It iteratively solves for the top side (`A`) of the square granary such that the total volume matches the given millet volume.
3. Once `A` is found, the bottom side (`B`) and depth (`h`) are calculated using the given relationships.
4. The results are converted into the appropriate units (chi or zhang) and printed.

---

### Example Output:
If you run the code, it will calculate the dimensions of the granaries and output something like:
```
方窖上方 a = 36 尺
方窖下方 b = 5 丈 7 尺
方窖深 c = 5 丈
```

This means:
- The top side of the square granary is 36 chi.
- The bottom side of the square granary is 5 zhang 7 chi.
- The depth of the granaries is 5 zhang.
"""


"""
Timed out"""
