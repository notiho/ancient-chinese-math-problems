"""
假令有粟五千一百四十石，欲作方窖、圓窖各一，令口小底大，方面於圓徑等，兩深亦同，其深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問：方、徑、深各多少？
答曰：上方徑各 a尺 ，下方徑各 b丈 ，深各 c丈 。
"""

"""
This is a classic ancient Chinese math problem involving the calculation of dimensions for square and circular granaries (窖). Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Given:**
   - Total millet: 5140 石.
   - Two granaries: one square (方窖) and one circular (圓窖).
   - Both granaries have the same depth (深).
   - The square granary's side length (方) is equal to the diameter of the circular granary (圓徑).
   - The depth (深) is 7 尺 less than the bottom width (下方) and 1 丈 4 尺 (14 尺) more than the top width (上方).

2. **Unknowns:**
   - Top width (上方徑, `a`).
   - Bottom width (下方徑, `b`).
   - Depth (深, `c`).

3. **Relationships:**
   - Volume of the square granary:  
     \( V_{\text{square}} = \frac{1}{3} \times c \times (a^2 + a \times b + b^2) \).
   - Volume of the circular granary:  
     \( V_{\text{circle}} = \frac{1}{12} \times \pi \times c \times (a^2 + a \times b + b^2) \).
   - Total volume: \( V_{\text{square}} + V_{\text{circle}} = 5140 \times 10 = 51400 \) cubic 尺 (since 1 石 = 10 cubic 尺).

4. **Depth relationship:**
   - \( c = b - 7 = a + 14 \).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from math import pi

# Total millet in cubic chi
total_volume = 5140 * 10

# Relationships
# c = depth, a = top width, b = bottom width
# c = b - 7 = a + 14
# Therefore, b = c + 7 and a = c - 14

# Solve for c, a, b
for c in range(1, 100):  # Iterate over possible depths (in chi)
    a = c - 14
    b = c + 7
    
    if a <= 0 or b <= 0:  # Widths must be positive
        continue
    
    # Square granary volume
    V_square = Fraction(1, 3) * c * (a**2 + a * b + b**2)
    
    # Circular granary volume
    V_circle = Fraction(1, 12) * pi * c * (a**2 + a * b + b**2)
    
    # Total volume
    total = V_square + V_circle
    
    # Check if the total matches the given volume
    if abs(total - total_volume) < 1e-6:  # Allow for small floating-point errors
        print(f"Top width (a): {a} chi")
        print(f"Bottom width (b): {b} chi")
        print(f"Depth (c): {c} chi")
        break
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Iterate over possible depths (`c`)**: Since the depth must be positive, we iterate over reasonable values (e.g., 1 to 100 尺).
2. **Calculate `a` and `b`**: Using the relationships \( c = b - 7 = a + 14 \), we derive \( a = c - 14 \) and \( b = c + 7 \).
3. **Calculate volumes**: Compute the volumes of the square and circular granaries using the given formulas.
4. **Check total volume**: Compare the sum of the two volumes to the total millet volume (51400 cubic 尺). If they match, we have our solution.

---

### Output:
The program will output the values of:
- Top width \( a \) (in chi),
- Bottom width \( b \) (in chi),
- Depth \( c \) (in chi).

This approach ensures an accurate solution using the relationships and constraints provided in the problem.
"""


"""
Variable 'a' has wrong value. Expected: 7, Actual: 85
Variable 'b' has wrong value. Expected: 14/5, Actual: 106
Variable 'c' has wrong value. Expected: 21/10, Actual: 99"""
