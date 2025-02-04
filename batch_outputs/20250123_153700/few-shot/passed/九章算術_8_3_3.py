"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, similar to Gaussian elimination. Here's the solution step by step:

### Problem Breakdown:
- **Given:**
  - 5 bundles of upper millet lose 1 dou 1 sheng (11 sheng) when compared to 7 bundles of lower millet.
  - 7 bundles of upper millet lose 2 dou 5 sheng (25 sheng) when compared to 5 bundles of lower millet.

- **Goal:**
  - Find the yield of 1 bundle of upper millet (`a`) and 1 bundle of lower millet (`b`).

- **Procedure:**
  - Set up the equations:
    1. \( 5a - 7b = 11 \)
    2. \( 7a - 5b = 25 \)
  - Solve using the elimination method described in the "方程術" (method of simultaneous equations).

---

### Python Implementation:


"""


from fractions import Fraction

# Given data
上禾_秉1 = 5  # Upper millet bundles in the first equation
下禾_秉1 = -7  # Lower millet bundles in the first equation (negative because it's subtracted)
損實1 = 11  # Loss in sheng for the first equation (1 dou 1 sheng = 11 sheng)

上禾_秉2 = 7  # Upper millet bundles in the second equation
下禾_秉2 = -5  # Lower millet bundles in the second equation (negative because it's subtracted)
損實2 = 25  # Loss in sheng for the second equation (2 dou 5 sheng = 25 sheng)

# Step 1: Eliminate one variable (下禾, b)
# Multiply the first equation by 7 (coefficient of 上禾 in the second equation)
# Multiply the second equation by 5 (coefficient of 上禾 in the first equation)
eq1_scaled = [7 * 上禾_秉1, 7 * 下禾_秉1, 7 * 損實1]  # [35a, -49b, 77]
eq2_scaled = [5 * 上禾_秉2, 5 * 下禾_秉2, 5 * 損實2]  # [35a, -25b, 125]

# Subtract the second scaled equation from the first to eliminate 上禾 (a)
eliminated_eq = [
    eq1_scaled[0] - eq2_scaled[0],  # Coefficient of a (should be 0)
    eq1_scaled[1] - eq2_scaled[1],  # Coefficient of b
    eq1_scaled[2] - eq2_scaled[2],  # Constant term
]  # [0, -24b, -48]

# Simplify the eliminated equation
下禾_系數 = eliminated_eq[1]  # Coefficient of b
損實_系數 = eliminated_eq[2]  # Constant term
b = Fraction(損實_系數, 下禾_系數)  # Solve for b (下禾, lower millet yield per bundle)

# Step 2: Substitute b back into one of the original equations to solve for a (上禾)
# Using the first equation: 5a - 7b = 11
a = Fraction(損實1 - (下禾_秉1 * b), 上禾_秉1)  # Solve for a (上禾, upper millet yield per bundle)

# Results
print(f"上禾一秉 a = {a} 升")  # Yield of 1 bundle of upper millet
print(f"下禾一秉 b = {b} 升")  # Yield of 1 bundle of lower millet


"""


---

### Explanation of the Code:
1. **Set Up Equations:**
   - The two equations are derived from the problem statement:
     - \( 5a - 7b = 11 \)
     - \( 7a - 5b = 25 \)

2. **Elimination:**
   - Multiply the equations to align the coefficients of \( a \) (upper millet) and subtract to eliminate \( a \), leaving an equation with only \( b \) (lower millet).

3. **Solve for \( b \):**
   - Simplify the resulting equation to find \( b \), the yield of 1 bundle of lower millet.

4. **Substitute Back:**
   - Substitute \( b \) into one of the original equations to solve for \( a \), the yield of 1 bundle of upper millet.

5. **Output Results:**
   - The results are expressed as fractions to maintain precision.

---

### Final Answer:
- \( a \): Yield of 1 bundle of upper millet in sheng.
- \( b \): Yield of 1 bundle of lower millet in sheng.
"""


"""
"""
