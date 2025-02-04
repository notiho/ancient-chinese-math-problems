"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The problem involves solving a system of linear equations using the described method, which is essentially Gaussian elimination.

---

### Problem Setup
We are given:
1. **Equation 1**: 6上禾 - 10下禾 = 1斗8升 (18升)
2. **Equation 2**: -5上禾 + 15下禾 = 5升

We need to find the "實" (value per unit) for 上禾 and 下禾.

---

### Python Code Implementation


"""

#----- content starts here -----

from fractions import Fraction

# Convert units: 1斗 = 10升
斗_to_升 = 10

# Equation 1: 6上禾 - 10下禾 = 1斗8升
上禾1 = 6
下禾1 = -10
實1 = 1 * 斗_to_升 + 8  # 1斗8升 = 18升

# Equation 2: -5上禾 + 15下禾 = 5升
上禾2 = -5
下禾2 = 15
實2 = 5  # 5升

# Step 1: Eliminate 上禾 from the second equation
# Multiply Equation 1 by 5 and Equation 2 by 6 to align 上禾 coefficients
factor1 = 5
factor2 = 6

上禾1 *= factor1
下禾1 *= factor1
實1 *= factor1

上禾2 *= factor2
下禾2 *= factor2
實2 *= factor2

# Subtract the scaled equations to eliminate 上禾
下禾_combined = 下禾1 - 下禾2
實_combined = 實1 - 实2

# Step 2: Solve for 下禾 (value per unit)
b = Fraction(實_combined, 下禾_combined)

# Step 3: Substitute 下禾 value into one of the original equations to solve for 上禾
實1_adjusted = 實1 - (下禾1 * b)
a = Fraction(實1_adjusted, 上禾1)

# Results
print(f"上禾一秉實 a = {a} 升")
print(f"下禾一秉實 b = {b} 升")
#----- content ends here -----


"""


---

### Explanation of the Code
1. **Unit Conversion**: Convert 1斗 into 10升 for consistency in units.
2. **Equation Setup**: Represent the two equations in terms of 上禾 and 下禾.
3. **Elimination**: Use Gaussian elimination to eliminate one variable (上禾) and solve for the other (下禾).
4. **Back Substitution**: Substitute the solved value of 下禾 back into one of the original equations to solve for 上禾.
5. **Fraction Handling**: Use the `Fraction` class to ensure exact arithmetic for non-integer results.

---

### Final Answer
The values of `a` (上禾一秉實) and `b` (下禾一秉實) will be printed in 升.
"""


"""
Code error: name '实2' is not defined"""
