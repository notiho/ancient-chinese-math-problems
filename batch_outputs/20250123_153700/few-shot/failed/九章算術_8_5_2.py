"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, which are similar to modern elimination techniques. Let's translate the problem and procedure into Python code.

The problem involves two equations:
1. 3 bundles of upper millet (上禾) plus 6 dou of additional grain equals the yield of 10 bundles of lower millet (下禾).
2. 5 bundles of lower millet plus 1 dou of additional grain equals the yield of 2 bundles of upper millet.

We aim to find the yield of 1 bundle of upper millet (上禾) and 1 bundle of lower millet (下禾).

### Procedure:
The ancient method involves setting up the equations, eliminating variables step by step, and solving for the unknowns.


"""


from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 3上禾 - 10下禾 - 6 = 0
上禾1 = 3
下禾1 = -10
常數1 = -6

# Equation 2: -2上禾 + 5下禾 - 1 = 0
上禾2 = -2
下禾2 = 5
常數2 = -1

# Eliminate one variable (e.g., 上禾) using the two equations
# Multiply the first equation by 2 and the second equation by 3 to align 上禾 coefficients
上禾系數 = 上禾1 * 2 - 上禾2 * 3
下禾系數 = 下禾1 * 2 - 下禾2 * 3
常數系數 = 常數1 * 2 - 常數2 * 3

# Solve for 下禾 (lower millet yield per bundle)
下禾實 = Fraction(-常數系數, 下禾系數)

# Substitute 下禾實 back into one of the original equations to solve for 上禾 (upper millet yield per bundle)
上禾實 = Fraction(-(下禾1 * 下禾實 + 常數1), 上禾1)

# Results
a = 上禾實  # Yield of 1 bundle of upper millet
b = 下禾實  # Yield of 1 bundle of lower millet

# Output the results
a, b


"""


### Explanation:
1. The coefficients of the equations are extracted from the problem statement.
2. The elimination method is used to remove one variable (上禾) and solve for the other (下禾).
3. The value of 下禾 is substituted back into one of the original equations to solve for 上禾.
4. The results are expressed as fractions to ensure accuracy.

### Answer:
The yield of 1 bundle of upper millet (上禾) is `a` dou, and the yield of 1 bundle of lower millet (下禾) is `b` dou.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 8/7
Variable 'b' has wrong value. Expected: 3, Actual: -9/35"""
