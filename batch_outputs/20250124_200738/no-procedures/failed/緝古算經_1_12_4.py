"""
假令有粟五千一百四十石，欲作方窖、圓窖各一，令口小底大，方面於圓徑等，兩深亦同，其深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問：方、徑、深各多少？
答曰：上方徑各 a尺 ，下方徑各 b丈 ，深各 c丈 。
"""

"""
This is a classic ancient Chinese math problem involving the calculation of dimensions for square and circular granaries. Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. There are **5140 shi** of millet to be stored.
2. Two granaries are to be built:
   - One square granary (方窖).
   - One circular granary (圓窖).
3. Both granaries have:
   - The same depth.
   - The same top width (上方 or top diameter for the circular granary).
   - The same bottom width (下方 or bottom diameter for the circular granary).
4. The depth (深) is:
   - **7 chi less than the bottom width (下方).**
   - **1 zhang 4 chi (14 chi) more than the top width (上方).**
5. The total volume of the two granaries combined equals **5140 shi**.

---

### Formulas:
1. **Volume of the square granary (方窖):**
   The volume of a square granary is calculated as:
   \[
   V_{\text{square}} = \frac{(上方^2 + 上方 \cdot 下方 + 下方^2) \cdot 深}{3}
   \]

2. **Volume of the circular granary (圓窖):**
   The volume of a circular granary is calculated as:
   \[
   V_{\text{circle}} = \frac{(上方^2 + 上方 \cdot 下方 + 下方^2) \cdot 深 \cdot \pi}{12}
   \]

3. **Total volume:**
   \[
   V_{\text{square}} + V_{\text{circle}} = 5140 \, \text{shi}
   \]

4. **Relationships between dimensions:**
   \[
   深 = 下方 - 7
   \]
   \[
   深 = 上方 + 14
   \]

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from math import pi

# Total millet volume in shi
total_volume = 5140

# Relationships between dimensions
def calculate_dimensions():
    for 上方 in range(1, 100):  # Iterate over possible top widths (in chi)
        for 下方 in range(上方, 100):  # Iterate over possible bottom widths (in chi)
            深 = 下方 - 7  # Depth based on bottom width
            if 深 != 上方 + 14:  # Depth must also satisfy the second condition
                continue
            
            # Calculate the volume of the square granary
            square_volume = Fraction((上方**2 + 上方 * 下方 + 下方**2) * 深, 3)
            
            # Calculate the volume of the circular granary
            circle_volume = Fraction((上方**2 + 上方 * 下方 + 下方**2) * 深 * pi, 12)
            
            # Check if the total volume matches
            if square_volume + circle_volume == total_volume:
                return 上方, 下方, 深

# Solve for dimensions
a, b, c = calculate_dimensions()

# Convert results to zhang and chi
a = Fraction(a, 10)  # Top diameter in zhang
b = Fraction(b, 10)  # Bottom diameter in zhang
c = Fraction(c, 10)  # Depth in zhang

# Output the results
a, b, c
#----- content ends here -----


"""


---

### Explanation of the Code:
1. The code iterates over possible values for the top width (上方) and bottom width (下方), ensuring that the depth (深) satisfies both conditions.
2. It calculates the volumes of the square and circular granaries using the given formulas.
3. It checks if the total volume matches the given value of 5140 shi.
4. Once a match is found, it returns the dimensions in zhang (1 zhang = 10 chi).

---

### Final Answer:
The dimensions of the granaries are:
- Top diameter (上方徑): `a` zhang.
- Bottom diameter (下方徑): `b` zhang.
- Depth (深): `c` zhang.
"""


"""
Code error: both arguments should be Rational instances"""
