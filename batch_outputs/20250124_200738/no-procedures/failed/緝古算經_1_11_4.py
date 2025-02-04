"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
答曰：方徑各 a丈 ，高 b丈 ，深 c丈 。
"""

"""
This is a classic ancient Chinese math problem involving the calculation of the dimensions of a square granary and a circular granary based on their volumes and relationships. Let's break it down step by step and solve it.

---

### Problem Breakdown:
1. **Given:**
   - Total millet: 3072 石 (shi).
   - There is a square granary and a circular granary.
   - The diameter of the circular granary equals the side length of the square granary.
   - The depth of the circular granary is 2 chi (尺) less than the height of the square granary.
   - The height of the square granary is 3 chi (尺) less than the side length of the square granary.
   - Both granaries are filled to capacity, and the total millet is exactly used up.

2. **To Find:**
   - The side length of the square granary (`a` 丈).
   - The height of the square granary (`b` 丈).
   - The depth of the circular granary (`c` 丈).

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction
from math import pi

# Total millet in cubic chi (1 石 = 10 cubic chi)
total_volume = 3072 * 10  # Convert 石 to cubic chi

# Let the side length of the square granary and the diameter of the circular granary be `a` 丈 (10 chi = 1 丈)
# Let the height of the square granary be `b` 丈
# Let the depth of the circular granary be `c` 丈

# Relationships:
# b = a - Fraction(3, 10)  # Height of square granary is 3 chi (3/10 丈) less than the side length
# c = b - Fraction(2, 10)  # Depth of circular granary is 2 chi (2/10 丈) less than the height of the square granary

# Volumes:
# Volume of square granary = a^2 * b
# Volume of circular granary = (pi / 4) * a^2 * c

# Total volume:
# a^2 * b + (pi / 4) * a^2 * c = total_volume

# Substitute b and c in terms of a:
# b = a - 3/10
# c = b - 2/10 = a - 3/10 - 2/10 = a - 5/10 = a - 1/2

# Equation becomes:
# a^2 * (a - 3/10) + (pi / 4) * a^2 * (a - 1/2) = total_volume

# Simplify:
# a^2 * (a - 3/10) + (pi / 4) * a^2 * (a - 1/2) = 30720

# Factor out a^2:
# a^2 * [(a - 3/10) + (pi / 4) * (a - 1/2)] = 30720

# Solve for a numerically:
from sympy import symbols, Eq, solve

a = symbols('a')
b = a - Fraction(3, 10)
c = b - Fraction(2, 10)

square_volume = a**2 * b
circular_volume = (pi / 4) * a**2 * c

# Total volume equation
equation = Eq(square_volume + circular_volume, total_volume)

# Solve for a
solution = solve(equation, a)
a_solution = max([sol.evalf() for sol in solution if sol.is_real and sol > 0])  # Take the positive real solution

# Calculate b and c
b_solution = a_solution - Fraction(3, 10)
c_solution = b_solution - Fraction(2, 10)

# Convert to 丈
a_in_zhang = a_solution
b_in_zhang = b_solution
c_in_zhang = c_solution

# Output results
a_in_zhang, b_in_zhang, c_in_zhang
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Convert Units:** The total millet is converted from 石 to cubic chi (1 石 = 10 cubic chi).
2. **Define Relationships:** The relationships between the side length (`a`), height (`b`), and depth (`c`) are expressed in terms of `a`.
3. **Volume Equations:** The volumes of the square and circular granaries are calculated, and their sum is set equal to the total volume.
4. **Solve for `a`:** The equation is solved numerically for `a` (side length of the square granary).
5. **Calculate `b` and `c`:** Using the relationships, the height (`b`) and depth (`c`) are calculated.
6. **Output Results:** The results are converted to 丈 and displayed.

---

### Final Answer:
- Side length of the square granary (`a`): **a 丈**.
- Height of the square granary (`b`): **b 丈**.
- Depth of the circular granary (`c`): **c 丈**.


"""


"""
Variable 'a' has wrong value. Expected: 8/5, Actual: a
Variable 'b' has wrong value. Expected: 19/10, Actual: a - 3/10
Variable 'c' has wrong value. Expected: 7/5, Actual: a - 1/2"""
