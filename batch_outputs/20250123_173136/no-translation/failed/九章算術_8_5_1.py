"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
To solve this problem, we need to translate the ancient Chinese method of solving simultaneous linear equations into Python code. Here's the step-by-step implementation:


"""


from fractions import Fraction

# Define the equations based on the problem:
# 3上禾 - 10下禾 = -6
# -2上禾 + 5下禾 = -1

# Coefficients for the equations
a1, b1, c1 = 3, -10, -6  # First equation: 3上禾 - 10下禾 = -6
a2, b2, c2 = -2, 5, -1   # Second equation: -2上禾 + 5下禾 = -1

# Solve for 下禾 (b) using elimination
# Multiply the first equation by 2 and the second equation by 3 to align 上禾 coefficients
a1, b1, c1 = 2 * a1, 2 * b1, 2 * c1
a2, b2, c2 = 3 * a2, 3 * b2, 3 * c2

# Eliminate 上禾 by adding the two equations
b = Fraction(b1 + b2, -(c1 + c2))  # 下禾一秉實

# Substitute 下禾 back into the first equation to solve for 上禾
a = Fraction(-(b1 * b + c1), a1)  # 上禾一秉實

# Results
print(f"上禾一秉實 a = {a}斗")
print(f"下禾一秉實 b = {b}斗")


"""


### Explanation:
1. The two equations are derived from the problem statement:
   - \( 3 \text{上禾} - 10 \text{下禾} = -6 \)
   - \( -2 \text{上禾} + 5 \text{下禾} = -1 \)
2. We use the elimination method to solve for one variable (下禾) first.
3. After finding 下禾, we substitute it back into one of the original equations to solve for 上禾.
4. The results are expressed as fractions (斗).

### Answer:
- \( \text{上禾一秉實} = a \text{斗} \)
- \( \text{下禾一秉實} = b \text{斗} \)
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 8/9
Variable 'b' has wrong value. Expected: 3, Actual: -1/3"""
