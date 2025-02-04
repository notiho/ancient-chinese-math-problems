"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

"""
To solve this problem using the described ancient Chinese method (方程術), we will encode the procedure step by step in Python. The problem involves solving a system of linear equations to determine the yield of one秉 (bundle) of 上禾 (upper grain) and 下禾 (lower grain).

### Problem Setup:
1. **Equation 1**: 6上禾 - 10下禾 = 1斗8升 (18升)
2. **Equation 2**: -5上禾 + 15下禾 = 5升

We will solve this system of equations using the described method.

---


"""


from fractions import Fraction

# Convert units to consistent terms (升)
斗_to_升 = 10
損實1 = 1 * 斗_to_升 + 8  # 1斗8升 = 18升
損實2 = 5  # 5升

# Coefficients of the equations
# Equation 1: 6上禾 - 10下禾 = 18升
上禾1 = 6
下禾1 = -10
實1 = 損實1

# Equation 2: -5上禾 + 15下禾 = 5升
上禾2 = -5
下禾2 = 15
實2 = 損實2

# Step 1: Eliminate one variable (use 上禾 as the pivot)
# Multiply equations to align 上禾 coefficients
factor1 = 上禾2
factor2 = 上禾1

# Scale equations
上禾1_scaled = 上禾1 * factor1
下禾1_scaled = 下禾1 * factor1
實1_scaled = 實1 * factor1

上禾2_scaled = 上禾2 * factor2
下禾2_scaled = 下禾2 * factor2
實2_scaled = 実2 * factor2

# Subtract equations to eliminate 上禾
下禾_combined = 下禾1_scaled - 下禾2_scaled
實_combined = 實1_scaled - 實2_scaled

# Step 2: Solve for 下禾 (lower grain yield per bundle)
下禾實 = Fraction(實_combined, 下禾_combined)

# Step 3: Solve for 上禾 (upper grain yield per bundle)
實1_adjusted = 實1 - 下禾1 * 下禾實
上禾實 = Fraction(實1_adjusted, 上禾1)

# Results
a = 上禾實  # Upper grain yield per bundle
b = 下禾實  # Lower grain yield per bundle

# Output the results
a, b


"""


### Explanation of the Code:
1. **Setup**: The coefficients of the equations are defined based on the problem statement. Units are converted to consistent terms (升).
2. **Elimination**: The first variable (上禾) is eliminated by scaling and subtracting the equations.
3. **Solve for 下禾**: The resulting equation is solved for 下禾.
4. **Solve for 上禾**: The value of 下禾 is substituted back into one of the original equations to solve for 上禾.
5. **Results**: The yields per bundle for 上禾 and 下禾 are stored in `a` and `b`, respectively.

### Final Answer:
`a` (上禾一秉實) and `b` (下禾一秉實) will be expressed in terms of 升.
"""


"""
Code error: name '実2' is not defined"""
