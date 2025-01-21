"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
This problem involves solving a system of equations to determine the yield (實) per sheaf (秉) of two types of grain, "上禾" (upper grain) and "下禾" (lower grain). The solution follows the ancient Chinese "方程術" (method of solving simultaneous equations). Let's translate the procedure into Python code.

### Problem Setup:
- 6 sheaves of upper grain lose 1 dou 8 sheng of yield when compared to 10 sheaves of lower grain.
- 15 sheaves of lower grain lose 5 sheng of yield when compared to 5 sheaves of upper grain.
- Question: What is the yield per sheaf for both upper and lower grain?

### Procedure:
The procedure involves setting up two equations based on the problem statement and solving them using elimination and substitution.

---


"""


from fractions import Fraction

# Convert units for clarity
斗 = 10  # 1 dou = 10 sheng

# Problem setup
# Equation 1: 6上禾 - 10下禾 = 1斗8升
上禾1 = 6
下禾1 = -10
實1 = 1 * 斗 + 8  # Convert 1斗8升 to sheng

# Equation 2: -5上禾 + 15下禾 = 5升
上禾2 = -5
下禾2 = 15
實2 = 5  # Already in sheng

# Solve using elimination
# Multiply equations to align coefficients for elimination
# Multiply Equation 1 by 5 and Equation 2 by 6
上禾1_scaled = 5 * 上禾1
下禾1_scaled = 5 * 下禾1
實1_scaled = 5 * 實1

上禾2_scaled = 6 * 上禾2
下禾2_scaled = 6 * 下禾2
實2_scaled = 6 * 實2

# Eliminate 上禾 by adding the scaled equations
下禾_total = 下禾1_scaled + 下禾2_scaled
實_total = 實1_scaled + 实2_scaled

# Solve for 下禾 yield (per sheaf)
下禾實 = Fraction(實_total, 下禾_total)

# Substitute 下禾實 back into one of the original equations to solve for 上禾 yield
實1_adjusted = 實1 - 下禾1 * 下禾實
上禾實 = Fraction(實1_adjusted, 上禾1)

# Convert results to dou and sheng for clarity
a = 1  # Upper grain sheaf count (秉)
b = 上禾實  # Upper grain yield per sheaf (升)

c = 1  # Lower grain sheaf count (秉)
d = 下禾實  # Lower grain yield per sheaf (升)

# Output results
print(f"上禾 {a}秉 實 {b}升")
print(f"下禾 {c}秉 實 {d}升")


"""


---

### Explanation of the Code:
1. **Unit Conversion**: The problem uses dou (斗) and sheng (升) as units. We convert all quantities to sheng for consistent calculations.
2. **Equation Setup**: Two equations are derived from the problem statement:
   - \( 6 \text{上禾} - 10 \text{下禾} = 1 \text{斗} 8 \text{升} \)
   - \( -5 \text{上禾} + 15 \text{下禾} = 5 \text{升} \)
3. **Elimination**: The equations are scaled to align coefficients for elimination. This allows us to solve for one variable (下禾 yield) first.
4. **Substitution**: The value of 下禾 yield is substituted back into one of the original equations to solve for 上禾 yield.
5. **Result Conversion**: The results are presented in terms of dou and sheng for clarity.

### Final Answer:
The yield per sheaf for upper and lower grain is calculated and displayed in the format:
- 上禾 \( a \) 秉 實 \( b \) 升
- 下禾 \( c \) 秉 實 \( d \) 升
"""


"""
Code error: name '实2_scaled' is not defined"""
