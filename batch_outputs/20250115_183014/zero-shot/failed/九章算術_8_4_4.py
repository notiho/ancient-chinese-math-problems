"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. We'll use the `Fraction` class to handle numbers that might not be integers. The problem involves solving a system of linear equations. Let's compute the values of the unknowns step by step.


"""


from fractions import Fraction

# Define the equations based on the problem statement:
# Equation 1: 6a - 10c = 1斗8升 (convert 1斗8升 to 升: 1斗 = 10升, so 1斗8升 = 18升)
# Equation 2: -5a + 15c = 5升

# Convert the units to consistent terms (升)
eq1_constant = 18  # 1斗8升 = 18升
eq2_constant = 5   # 5升

# Coefficients of the equations
# Equation 1: 6a - 10c = 18
# Equation 2: -5a + 15c = 5

# Solve the system of equations using substitution or elimination
# Multiply Equation 1 by 5 and Equation 2 by 6 to eliminate 'a'
eq1_multiplied = [6 * 5, -10 * 5, 18 * 5]  # [30a, -50c, 90]
eq2_multiplied = [-5 * 6, 15 * 6, 5 * 6]   # [-30a, 90c, 30]

# Add the two equations to eliminate 'a'
# (30a - 30a) + (-50c + 90c) = 90 + 30
# 40c = 120
c = Fraction(120, 40)  # c = 3

# Substitute c = 3 into one of the original equations to solve for 'a'
# Use Equation 1: 6a - 10c = 18
# 6a - 10(3) = 18
# 6a - 30 = 18
# 6a = 48
a = Fraction(48, 6)  # a = 8

# Now compute the actual values of 'b' (上禾實) and 'd' (下禾實)
# 上禾實 (b升) = a秉 = 8秉
# 下禾實 (d升) = c秉 = 3秉

# Final results
b = a  # 上禾實 (b升)
d = c  # 下禾實 (d升)

# Output the results
print(f"a = {a} 秉")  # 上禾秉數
print(f"b = {b} 升")  # 上禾實
print(f"c = {c} 秉")  # 下禾秉數
print(f"d = {d} 升")  # 下禾實


"""


### Explanation of the Code:
1. The problem is translated into two linear equations:
   - \( 6a - 10c = 18 \) (where \( 18 \) represents \( 1斗8升 \))
   - \( -5a + 15c = 5 \) (where \( 5 \) represents \( 5升 \))
2. The equations are solved using the elimination method to find \( a \) and \( c \).
3. The values of \( b \) and \( d \) are directly derived from \( a \) and \( c \), as they represent the actual quantities of grain per unit.

### Final Output:
```
a = 8 秉
b = 8 升
c = 3 秉
d = 3 升
```
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 8
Variable 'c' has wrong value. Expected: 1, Actual: 3"""
