"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The problem involves a system of linear equations, and the solution uses the described "正負術" (positive-negative method) to solve for the values of "上禾" (upper grain) and "下禾" (lower grain) per unit秉.

### Problem Setup:
1. **Equations**:
   - Equation 1: 6上禾 - 10下禾 = 1斗8升 (convert to升: 1斗 = 10升, so 1斗8升 = 18升)
   - Equation 2: -5上禾 + 15下禾 = 5升

2. **Goal**:
   - Solve for the value of 1秉 of上禾 (a升) and 1秉 of下禾 (b升).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Convert given values into equations
# Equation 1: 6上禾 - 10下禾 = 18升
上禾1 = 6
下禾1 = -10
實1 = 18

# Equation 2: -5上禾 + 15下禾 = 5升
上禾2 = -5
下禾2 = 15
實2 = 5

# Step 1: Eliminate one variable (use正負術)
# Multiply Equation 1 by 5 and Equation 2 by 6 to align coefficients of上禾
上禾系數 = 上禾1 * 5 + 上禾2 * 6
下禾系數 = 下禾1 * 5 + 下禾2 * 6
實系數 = 實1 * 5 + 實2 * 6

# Now we have a single equation for下禾:
# 下禾系數 * 下禾 = 實系數
下禾實 = Fraction(實系數, 下禾系數)

# Step 2: Solve for上禾 using下禾實
# Substitute下禾實 back into Equation 1:
上禾實 = Fraction(實1 - (下禾1 * 下禾實), 上禾1)

# Results
a = 上禾實  # 上禾一秉實
b = 下禾實  # 下禾一秉實

# Output the results
a, b
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Equation Conversion**:
   - The problem provides two equations in terms of秉 (bundles of grain). These are converted into numerical coefficients for上禾 and下禾, with the損實 (loss in volume) converted to升 for consistency.

2. **正負術 (Positive-Negative Method)**:
   - The method involves eliminating one variable (e.g.,上禾) by aligning coefficients through multiplication and then solving for the other variable (e.g.,下禾).

3. **Substitution**:
   - Once one variable is solved, it is substituted back into one of the original equations to solve for the remaining variable.

4. **Fraction Handling**:
   - The `Fraction` class is used to ensure precise calculations, as the results may not be integers.

---

### Final Answer:
The values of `a` (上禾一秉實) and `b` (下禾一秉實) will be output as fractions in升.
"""


"""
"""
