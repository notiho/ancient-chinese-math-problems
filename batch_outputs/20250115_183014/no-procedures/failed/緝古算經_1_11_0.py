"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
答曰：方徑各 a丈 ，高 b丈 ，深 c丈 。
"""

"""
This is a classic ancient Chinese math problem involving the calculation of the dimensions of a square granary and a circular silo based on given conditions. Let's solve it step by step.

---

### Problem Breakdown:
1. There are **3072 shi** of grain.
2. The grain is to be stored in:
   - A **square granary** (方倉).
   - A **circular silo** (圓窖).
3. The **diameter of the circular silo** is equal to the **side length of the square granary**.
4. The **depth of the circular silo** is **2 chi** less than the height of the square granary.
5. The **height of the square granary** is **3 chi** less than its side length.
6. Both the granary and the silo are filled completely, and the total grain is exactly used up.

We need to find:
- The **side length** of the square granary (方, or `a`).
- The **diameter** of the circular silo (徑, also `a`).
- The **height** of the square granary (高, or `b`).
- The **depth** of the circular silo (深, or `c`).

---

### Assumptions:
1. The volume of the square granary is calculated as:
   \[
   V_{\text{square}} = \text{side}^2 \times \text{height}
   \]
2. The volume of the circular silo is calculated as:
   \[
   V_{\text{circular}} = \frac{\pi \times \text{diameter}^2 \times \text{depth}}{4}
   \]
3. The total volume of grain is:
   \[
   V_{\text{square}} + V_{\text{circular}} = 3072 \, \text{shi}
   \]
   (Note: 1 shi = 10 cubic chi.)

---

### Solution in Python:


"""


from fractions import Fraction
import math

# Total grain in cubic chi
total_grain = 3072 * 10  # 1 shi = 10 cubic chi

# Let the side length of the square granary and diameter of the circular silo be 'a'
# Height of the square granary is 'b = a - 3'
# Depth of the circular silo is 'c = b - 2 = a - 3 - 2 = a - 5'

# Volume of the square granary
def square_granary_volume(a):
    b = a - 3  # Height of the square granary
    return a**2 * b

# Volume of the circular silo
def circular_silo_volume(a):
    c = a - 5  # Depth of the circular silo
    return (math.pi * a**2 * c) / 4

# Total volume equation
def total_volume(a):
    return square_granary_volume(a) + circular_silo_volume(a)

# Solve for 'a' such that total_volume(a) = total_grain
# We'll use a simple numerical approach to find the solution
a = 1  # Start with an initial guess for 'a'
while True:
    if abs(total_volume(a) - total_grain) < 1e-6:  # Check if the total volume matches
        break
    a += Fraction(1, 10)  # Increment 'a' in small steps

# Calculate the corresponding 'b' and 'c'
b = a - 3
c = a - 5

# Convert results to fractions for exact representation
a = Fraction(a).limit_denominator()
b = Fraction(b).limit_denominator()
c = Fraction(c).limit_denominator()

# Output the results
print(f"方徑各 a = {a} 丈")
print(f"高 b = {b} 丈")
print(f"深 c = {c} 丈")


"""


---

### Explanation of the Code:
1. The total grain volume is converted to cubic chi.
2. The side length of the square granary (`a`) is iteratively adjusted until the total volume matches the given grain volume.
3. The height of the square granary (`b`) and the depth of the circular silo (`c`) are calculated based on the relationships provided in the problem.
4. The results are output as fractions for exact representation.

---

### Final Answer:
After running the code, the results will be:

- 方徑各 \( a = \text{calculated value} \) 丈
- 高 \( b = \text{calculated value} \) 丈
- 深 \( c = \text{calculated value} \) 丈
"""


"""
Timed out"""
