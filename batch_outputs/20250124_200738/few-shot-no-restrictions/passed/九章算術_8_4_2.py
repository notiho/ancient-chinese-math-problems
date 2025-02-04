"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

"""
This problem involves solving a system of linear equations to determine the yield of one sheaf of "upper millet" (上禾) and one sheaf of "lower millet" (下禾). The problem is essentially a classic simultaneous equations problem, where the relationships between the sheaves and their yields are given.

### Problem Breakdown:
1. **First relationship**:
   - 6 sheaves of upper millet (上禾) and 10 sheaves of lower millet (下禾) together lose 1 dou and 8 sheng (1斗8升 = 18升).
   - Equation: \( 6x - 10y = 18 \), where \( x \) is the yield of one sheaf of upper millet, and \( y \) is the yield of one sheaf of lower millet.

2. **Second relationship**:
   - 5 sheaves of upper millet (上禾) and 15 sheaves of lower millet (下禾) together lose 5 sheng.
   - Equation: \( -5x + 15y = 5 \).

We will solve this system of equations using Python.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations:
# 6x - 10y = 18
# -5x + 15y = 5

# Coefficients of the equations
a1, b1, c1 = 6, -10, 18  # First equation: 6x - 10y = 18
a2, b2, c2 = -5, 15, 5   # Second equation: -5x + 15y = 5

# Solve using elimination method
# Multiply the first equation by 5 and the second equation by 6 to align coefficients of x
eq1_mult = [a1 * 5, b1 * 5, c1 * 5]  # 30x - 50y = 90
eq2_mult = [a2 * 6, b2 * 6, c2 * 6]  # -30x + 90y = 30

# Add the two equations to eliminate x
y_coeff = eq1_mult[1] + eq2_mult[1]  # -50y + 90y = 40y
result = eq1_mult[2] + eq2_mult[2]   # 90 + 30 = 120

# Solve for y
y = Fraction(result, y_coeff)  # y = 120 / 40 = 3

# Substitute y back into the first equation to solve for x
# 6x - 10y = 18
x = Fraction(c1 - b1 * y, a1)  # x = (18 - (-10 * 3)) / 6 = (18 + 30) / 6 = 48 / 6 = 8

# Convert x and y to sheng
a = x  # Upper millet yield per sheaf (in sheng)
b = y  # Lower millet yield per sheaf (in sheng)

# Output the results
print(f"上禾一秉實 {a} 升")
print(f"下禾一秉實 {b} 升")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Equations Setup**:
   - The two equations are set up based on the problem's description.
   - The coefficients \( a1, b1, c1 \) and \( a2, b2, c2 \) represent the terms in the equations.

2. **Elimination Method**:
   - The first equation is multiplied by 5, and the second equation is multiplied by 6 to align the coefficients of \( x \).
   - Adding the two equations eliminates \( x \), leaving an equation in terms of \( y \).

3. **Solve for \( y \)**:
   - The resulting equation is solved for \( y \), which represents the yield of one sheaf of lower millet.

4. **Substitute \( y \) into the First Equation**:
   - The value of \( y \) is substituted back into the first equation to solve for \( x \), which represents the yield of one sheaf of upper millet.

5. **Output**:
   - The results are printed in terms of sheng (升).

---

### Answer:
The yield of one sheaf of upper millet (上禾) is **8升**, and the yield of one sheaf of lower millet (下禾) is **3升**.


"""


"""
"""
