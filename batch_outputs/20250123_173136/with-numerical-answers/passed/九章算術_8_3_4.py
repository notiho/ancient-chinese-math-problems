"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a(=5)升 ，下禾一秉 b(=2)升 。
"""

"""
Suppose there are 5 bundles of upper millet, losing 1 dou and 1 sheng of grain, equivalent to 7 bundles of lower millet.
Suppose there are 7 bundles of upper millet, losing 2 dou and 5 sheng of grain, equivalent to 5 bundles of lower millet.
Question: how much grain does one bundle of upper millet and one bundle of lower millet yield?

The procedure says: Treat it as a system of linear equations.
Place 5 bundles of upper millet as positive, 7 bundles of lower millet as negative, and 1 dou and 1 sheng as positive.
Next, place 7 bundles of upper millet as positive, 5 bundles of lower millet as negative, and 2 dou and 5 sheng as positive.
Use the positive-negative method to solve.

The procedure for solving systems of equations says: Place 3 unknowns (upper millet, middle millet, lower millet) and their total grain (39 dou) on the right side.
Arrange the middle and left millet similarly to the right side.
Multiply the right row of upper millet by the middle row and divide directly.
Repeat for the next term, also dividing directly.
Then, for the middle row, multiply the middle millet by the left row and divide directly.
For the left row, if the lower millet is not exact, treat the upper as the divisor and the lower as the dividend.
The result is the grain for the lower millet.
To find the middle millet, multiply the divisor by the middle row's lower result and divide by the lower millet's result.
The remainder, divided by the middle millet's count plus one, gives the middle millet's grain.
To find the upper millet, multiply the divisor by the right row's lower result and divide by the lower and middle millet's results.
The remainder, divided by the upper millet's count plus one, gives the upper millet's grain.
The results follow the rules, yielding 1 dou for each.

Answer: One bundle of upper millet yields *a*(=5) sheng, and one bundle of lower millet yields *b*(=2) sheng.
"""

# 上禾五秉，損實一斗一升，當下禾七秉
上禾1 = 5
下禾1 = -7
損實1 = 1 * 10 + 1  # 1斗1升 converted to sheng

# 上禾七秉，損實二斗五升，當下禾五秉
上禾2 = 7
下禾2 = -5
損實2 = 2 * 10 + 5  # 2斗5升 converted to sheng

# 正負術 (solving the linear equations)
# Multiply the first equation by 7 and the second equation by 5 to align the coefficients of 上禾
eq1 = (上禾1 * 7, 下禾1 * 7, 損實1 * 7)
eq2 = (上禾2 * 5, 下禾2 * 5, 損實2 * 5)

# Subtract the second equation from the first to eliminate 上禾
下禾系數 = eq1[1] - eq2[1]
損實差 = eq1[2] - eq2[2]

# Solve for 下禾 (one bundle of lower millet)
b = Fraction(損實差, 下禾系數)  # 2 sheng

# Substitute b into the first equation to solve for 上禾 (one bundle of upper millet)
上禾實 = 損實1 - (下禾1 * b)
a = Fraction(上禾實, 上禾1)  # 5 sheng
"""
"""
