"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a(=35/26)斗 ，下禾一秉實 b(=41/52)斗 。
"""

"""
This problem involves solving a system of equations to determine the yield of one sheaf of upper-grade grain (*上禾*) and one sheaf of lower-grade grain (*下禾*). The procedure describes how to approach the problem using ancient Chinese methods, which are equivalent to solving simultaneous linear equations.

### Problem Breakdown:
- **Given**:
  - 7 sheaves of upper-grade grain (*上禾*), reduced by 1 dou, and increased by 2 sheaves of lower-grade grain (*下禾*), yield 10 dou.
  - 8 sheaves of lower-grade grain (*下禾*), increased by 1 dou and 2 sheaves of upper-grade grain (*上禾*), yield 10 dou.

- **Unknowns**:
  - Yield of one sheaf of upper-grade grain (*上禾*): `a` dou.
  - Yield of one sheaf of lower-grade grain (*下禾*): `b` dou.

- **Equations**:
  1. \( 7a - 1 + 2b = 10 \)
  2. \( 8b + 1 + 2a = 10 \)

- **Procedure**:
  The ancient method involves manipulating the equations systematically to isolate and solve for the unknowns.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 7a - 1 + 2b = 10
coeff1_a = 7
coeff1_b = 2
const1 = 10 + 1  # Move -1 to the right-hand side

# Equation 2: 8b + 1 + 2a = 10
coeff2_a = 2
coeff2_b = 8
const2 = 10 - 1  # Move +1 to the right-hand side

# Solve for 'a' (上禾) and 'b' (下禾) using substitution/elimination
# Multiply the first equation by coeff2_b and the second equation by coeff1_b to align b terms
mult1 = coeff2_b  # 8
mult2 = coeff1_b  # 2

# Scale the equations
eq1_scaled_a = coeff1_a * mult1  # 7 * 8 = 56
eq1_scaled_b = coeff1_b * mult1  # 2 * 8 = 16
eq1_scaled_const = const1 * mult1  # 11 * 8 = 88

eq2_scaled_a = coeff2_a * mult2  # 2 * 2 = 4
eq2_scaled_b = coeff2_b * mult2  # 8 * 2 = 16
eq2_scaled_const = const2 * mult2  # 9 * 2 = 18

# Eliminate 'b' by subtracting the scaled equations
final_a_coeff = eq1_scaled_a - eq2_scaled_a  # 56 - 4 = 52
final_const = eq1_scaled_const - eq2_scaled_const  # 88 - 18 = 70

# Solve for 'a'
a = Fraction(final_const, final_a_coeff)  # a = 70 / 52 = 35 / 26

# Substitute 'a' back into one of the original equations to solve for 'b'
# Using Equation 1: 7a + 2b = 11
b_numerator = const1 - coeff1_a * a  # 11 - 7 * (35 / 26)
b = Fraction(b_numerator, coeff1_b)  # b = (41 / 26) / 2 = 41 / 52

# Results
a = Fraction(35, 26)  # 上禾一秉實
b = Fraction(41, 52)  # 下禾一秉實

# Output the results
a, b
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Define the Equations**:
   - The coefficients of the two equations are extracted from the problem statement.

2. **Eliminate One Variable**:
   - The equations are scaled to align the coefficients of one variable (in this case, \( b \)).
   - Subtracting the scaled equations eliminates \( b \), leaving an equation in terms of \( a \).

3. **Solve for \( a \)**:
   - The resulting equation is solved for \( a \) using fractions to ensure precision.

4. **Substitute Back**:
   - The value of \( a \) is substituted back into one of the original equations to solve for \( b \).

5. **Output**:
   - The results are expressed as fractions for exactness.

---

### Final Answer:
- Yield of one sheaf of upper-grade grain (*上禾*): \( a = \frac{35}{26} \) dou.
- Yield of one sheaf of lower-grade grain (*下禾*): \( b = \frac{41}{52} \) dou.
"""


"""
"""
