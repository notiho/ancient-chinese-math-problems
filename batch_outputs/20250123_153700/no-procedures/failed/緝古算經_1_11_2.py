"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
答曰：方徑各 a丈 ，高 b丈 ，深 c丈 。
"""

"""
This is a classic ancient Chinese problem involving the calculation of the dimensions of a square granary and a circular granary based on their volumes and relationships. Let's break it down step by step and solve it in Python.

---

### Problem Breakdown:
1. **Given:**
   - Total millet = 3072 石.
   - A square granary and a circular granary are to be constructed.
   - The diameter of the circular granary equals the side length of the square granary.
   - The depth of the circular granary is 2 尺 more than the square granary's depth.
   - The height of the square granary is 3 尺 less than the circular granary's height.
   - Both granaries are filled completely, and the millet is used up exactly.

2. **To Find:**
   - Side length of the square granary (`a` 丈).
   - Diameter of the circular granary (`a` 丈).
   - Height of the square granary (`b` 丈).
   - Depth of the circular granary (`c` 丈).

3. **Units:**
   - 1 丈 = 10 尺.
   - Volumes are calculated in cubic 尺.

4. **Formulas:**
   - Volume of the square granary = side² × height.
   - Volume of the circular granary = (π × radius² × depth).
   - Total volume = 3072 石 = 30720 cubic 尺 (since 1 石 = 10 cubic 尺).

---

### Python Code Solution:


"""


from fractions import Fraction
import math

# Total millet in cubic chi
total_volume = 30720  # 3072 石 × 10 尺/石

# Let the side length and diameter of the granaries be 'a' 丈 (10a 尺)
# Let the height of the square granary be 'b' 丈 (10b 尺)
# Let the depth of the circular granary be 'c' 丈 (10c 尺)

# Relationships:
# c = b + 2 (circular granary depth is 2 尺 more than square granary height)
# b = c - 3 (square granary height is 3 尺 less than circular granary depth)

# Volumes:
# Volume of square granary = (10a)^2 × 10b = 100a^2 × b 尺³
# Volume of circular granary = π × (5a)^2 × 10c = 250πa^2 × c 尺³
# Total volume = 100a^2 × b + 250πa^2 × c = 30720

# Substitute c = b + 2 into the total volume equation:
# 100a^2 × b + 250πa^2 × (b + 2) = 30720
# Expand:
# 100a^2 × b + 250πa^2 × b + 500πa^2 = 30720
# Combine terms:
# (100 + 250π)a^2 × b + 500πa^2 = 30720

# Solve for a, b, c:
# Let π ≈ 3.141592653589793 for simplicity.

# Constants
pi = math.pi

# Coefficients
coeff1 = 100 + 250 * pi  # Coefficient of a^2 × b
coeff2 = 500 * pi        # Coefficient of a^2

# Solve for b in terms of a:
# b = (30720 - coeff2 * a^2) / (coeff1 * a^2)

# Try different values of a to find integer solutions:
for a in range(1, 11):  # Test a in 丈 (1 to 10 丈)
    a_chi = 10 * a  # Convert a to 尺
    numerator = 30720 - coeff2 * (a_chi ** 2)
    denominator = coeff1 * (a_chi ** 2)
    b = numerator / denominator
    if b.is_integer() and b > 0:  # Check if b is a positive integer
        b_chi = int(b)  # Convert b to 尺
        c_chi = b_chi + 2  # c = b + 2 尺
        print(f"方徑各 {a} 丈, 高 {b / 10} 丈, 深 {c_chi / 10} 丈")
        break


"""


---

### Explanation:
1. The code uses the relationships between the dimensions and the total volume to derive a formula for `b` in terms of `a`.
2. It iterates over possible values of `a` (in 丈) to find integer solutions for `b` and `c`.
3. The solution is printed in 丈 for clarity.

---

### Output:
The output will provide the values of `a`, `b`, and `c` in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 8/5, Actual: 10
Variable 'b' has wrong value. Expected: 19/10, Actual: -1.7706433010649443
Missing variable in output: 'c'"""
