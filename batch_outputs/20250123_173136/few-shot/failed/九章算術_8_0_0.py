"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

"""
Suppose there are three types of grain: upper grain (shanghe), middle grain (zhonghe), and lower grain (xiahe).
The quantities and total volumes are as follows:
- 3 bundles of upper grain, 2 bundles of middle grain, 1 bundle of lower grain yield 39 dou.
- 2 bundles of upper grain, 3 bundles of middle grain, 1 bundle of lower grain yield 34 dou.
- 1 bundle of upper grain, 2 bundles of middle grain, 3 bundles of lower grain yield 26 dou.

Question: How much does one bundle of upper grain, middle grain, and lower grain yield respectively?

The procedure for solving systems of equations says:
1. Place the equations in rows, with the coefficients of the grains on the left and the total volumes on the right.
2. Use the top row to eliminate the upper grain terms from the second and third rows by multiplying and subtracting.
3. Use the second row to eliminate the middle grain term from the third row.
4. Solve for the lower grain by dividing the remaining term in the third row.
5. Substitute the value of the lower grain into the second row to solve for the middle grain.
6. Substitute the values of the lower and middle grains into the first row to solve for the upper grain.

Answer: One bundle of upper grain yields *a* dou, one bundle of middle grain yields *b* dou, and one bundle of lower grain yields *c* dou.
"""

# Coefficients and totals from the problem
上禾系數 = [3, 2, 1]
中禾系數 = [2, 3, 1]
下禾系數 = [1, 2, 3]
總量 = [39, 34, 26]

# Step 1: Eliminate the upper grain (上禾) from the second and third rows
# Multiply the first row by 2 and subtract from the second row
中禾系數[0] -= 2 * 上禾系數[0]
中禾系數[1] -= 2 * 上禾系數[1]
中禾系數[2] -= 2 * 上禾系數[2]
總量[1] -= 2 * 總量[0]

# Multiply the first row by 1 and subtract from the third row
下禾系數[0] -= 1 * 上禾系數[0]
下禾系數[1] -= 1 * 上禾系數[1]
下禾系數[2] -= 1 * 上禾系數[2]
總量[2] -= 1 * 總量[0]

# Step 2: Eliminate the middle grain (中禾) from the third row
# Multiply the second row by the appropriate factor to align with the third row
factor = 下禾系數[1] / 中禾系數[1]
下禾系數[1] -= factor * 中禾系數[1]
下禾系數[2] -= factor * 中禾系數[2]
總量[2] -= factor * 總量[1]

# Step 3: Solve for the lower grain (下禾)
c = Fraction(總量[2], 下禾系數[2])

# Step 4: Solve for the middle grain (中禾)
b = Fraction(總量[1] - 中禾系數[2] * c, 中禾系數[1])

# Step 5: Solve for the upper grain (上禾)
a = Fraction(總量[0] - 上禾系數[1] * b - 上禾系數[2] * c, 上禾系數[0])

# Final results
a, b, c
"""
Code error: both arguments should be Rational instances"""
