"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
答曰：方徑各 a丈 ，高 b丈 ，深 c丈 。
"""

"""
This is a classic ancient Chinese math problem involving the calculation of the dimensions of a square granary and a circular granary based on their volumes. Let's break it down step by step and solve it.

---

### Problem Breakdown:
- There are **3072 shi** of grain.
- A **square granary** (方倉) and a **circular granary** (圓窖) are to be constructed.
- The **diameter of the circular granary** is equal to the **side length of the square granary**.
- The **depth of the circular granary** is 2 chi less than the height of the square granary.
- The **height of the square granary** is 3 chi less than the side length of the square granary.
- Both granaries are filled to capacity, and the total grain is exactly used up.

We need to find:
- The **side length of the square granary** (方, `a`),
- The **diameter of the circular granary** (徑, `a`),
- The **height of the square granary** (高, `b`),
- The **depth of the circular granary** (深, `c`).

---

### Assumptions and Formulas:
1. **Volume of the square granary**:
   \[
   V_{\text{square}} = \text{side}^2 \times \text{height}
   \]

2. **Volume of the circular granary**:
   \[
   V_{\text{circle}} = \frac{\pi}{4} \times \text{diameter}^2 \times \text{depth}
   \]

3. Total volume:
   \[
   V_{\text{square}} + V_{\text{circle}} = 3072 \, \text{shi}
   \]

4. Relationships:
   - Diameter of the circular granary = Side length of the square granary.
   - Depth of the circular granary = Height of the square granary - 2 chi.
   - Height of the square granary = Side length of the square granary - 3 chi.

---

### Solution in Python:


"""


from fractions import Fraction
import math

# Total grain in shi
total_grain = 3072

# Conversion factor: 1 shi = 100 cubic chi
total_volume = total_grain * 100  # in cubic chi

# Let the side length of the square granary (and diameter of the circular granary) be `a`
# Height of the square granary = a - 3
# Depth of the circular granary = a - 3 - 2 = a - 5

# Volume of the square granary
def square_volume(a):
    return a**2 * (a - 3)

# Volume of the circular granary
def circular_volume(a):
    return (math.pi / 4) * a**2 * (a - 5)

# Total volume equation
def total_volume_equation(a):
    return square_volume(a) + circular_volume(a) - total_volume

# Solve for `a` (side length and diameter)
# Using trial and error to find the approximate solution
a = Fraction(0)
for i in range(1, 100):
    if total_volume_equation(Fraction(i)) == 0:
        a = Fraction(i)
        break

# Calculate other dimensions
b = a - 3  # Height of the square granary
c = a - 5  # Depth of the circular granary

# Results
print(f"Side length of the square granary and diameter of the circular granary (a): {a} 丈")
print(f"Height of the square granary (b): {b} 丈")
print(f"Depth of the circular granary (c): {c} 丈")


"""


---

### Explanation of the Code:
1. The total volume is converted from **shi** to **cubic chi** (1 shi = 100 cubic chi).
2. The formulas for the volumes of the square and circular granaries are implemented.
3. The relationship between the dimensions is used to express all variables in terms of `a`.
4. A numerical method (trial and error) is used to find the value of `a` that satisfies the total volume equation.
5. Once `a` is found, the height (`b`) and depth (`c`) are calculated.

---

### Final Answer:
The side length of the square granary and the diameter of the circular granary are **a 丈**, the height of the square granary is **b 丈**, and the depth of the circular granary is **c 丈**.
"""


"""
Variable 'a' has wrong value. Expected: 8/5, Actual: 0
Variable 'b' has wrong value. Expected: 19/10, Actual: -3
Variable 'c' has wrong value. Expected: 7/5, Actual: -5"""
