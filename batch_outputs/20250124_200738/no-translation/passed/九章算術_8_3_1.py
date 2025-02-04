"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

"""
To solve this problem, we will translate the ancient Chinese "方程術" (method of simultaneous equations) into Python code. Here's the step-by-step implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Problem setup
# First equation: 上禾 5 秉正，下禾 7 秉負，損實 1 斗 1 升 (11 升)
上禾_1 = 5
下禾_1 = -7
損實_1 = 10 + 1  # Convert 1 斗 1 升 to 升 (1 斗 = 10 升)

# Second equation: 上禾 7 秉正，下禾 5 秉負，損實 2 斗 5 升 (25 升)
上禾_2 = 7
下禾_2 = -5
損實_2 = 20 + 5  # Convert 2 斗 5 升 to 升

# Using the method of elimination to solve for 上禾 and 下禾
# Multiply the first equation by 下禾_2 and the second equation by 下禾_1 to align 下禾 terms
eq1_multiplier = 下禾_2
eq2_multiplier = 下禾_1

# Adjusted equations
adjusted_上禾_1 = 上禾_1 * eq1_multiplier
adjusted_下禾_1 = 下禾_1 * eq1_multiplier
adjusted_損實_1 = 損實_1 * eq1_multiplier

adjusted_上禾_2 = 上禾_2 * eq2_multiplier
adjusted_下禾_2 = 下禾_2 * eq2_multiplier
adjusted_損實_2 = 損實_2 * eq2_multiplier

# Eliminate 下禾 by subtracting the two equations
final_上禾 = adjusted_上禾_1 - adjusted_上禾_2
final_損實 = adjusted_損實_1 - adjusted_損實_2

# Solve for 上禾 (one 秉 of 上禾)
上禾_實 = Fraction(final_損實, final_上禾)

# Substitute 上禾_實 back into one of the original equations to solve for 下禾
下禾_實 = Fraction(損實_1 - (上禾_1 * 上禾_實), 下禾_1)

# Results
a = 上禾_實  # 上禾一秉實
b = 下禾_實  # 下禾一秉實

# Output
print(f"上禾一秉實: {a} 升")
print(f"下禾一秉實: {b} 升")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Setup the Equations**: The problem gives two equations involving the number of 秉 (bundles) of 上禾 and 下禾 and their corresponding losses in 升.
2. **Elimination Method**: The ancient method aligns the coefficients of one variable (下禾 in this case) by multiplying the equations appropriately, then subtracts them to eliminate 下禾 and solve for 上禾.
3. **Substitution**: Once 上禾 is determined, substitute it back into one of the original equations to solve for 下禾.
4. **Use Fractions**: The `Fraction` class ensures precise arithmetic for non-integer results.

### Answer:
After running the code:
- 上禾一秉實: `a` 升
- 下禾一秉實: `b` 升
"""


"""
"""
