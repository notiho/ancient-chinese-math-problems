"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

#----- content starts here -----
"""
Suppose there are three types of grain: upper grain (上禾), middle grain (中禾), and lower grain (下禾).
The problem provides the following data:
- 3 bundles of upper grain, 2 bundles of middle grain, and 1 bundle of lower grain yield 39 dou.
- 2 bundles of upper grain, 3 bundles of middle grain, and 1 bundle of lower grain yield 34 dou.
- 1 bundle of upper grain, 2 bundles of middle grain, and 3 bundles of lower grain yield 26 dou.

Question: How much does one bundle of upper grain, middle grain, and lower grain yield respectively?

The procedure for solving simultaneous equations (方程術) is as follows:
1. Place the coefficients of the first equation (3 upper grain, 2 middle grain, 1 lower grain, and 39 dou) on the right side.
2. Place the coefficients of the second and third equations in the same format below the first.
3. Eliminate the upper grain term from the second and third equations by multiplying the first equation and subtracting.
4. Eliminate the middle grain term from the third equation by using the second equation.
5. Solve for the lower grain yield (下禾) by dividing the remaining term.
6. Substitute the lower grain yield into the second equation to solve for the middle grain yield (中禾).
7. Substitute both the lower and middle grain yields into the first equation to solve for the upper grain yield (上禾).

Answer: One bundle of upper grain yields *a* dou, one bundle of middle grain yields *b* dou, and one bundle of lower grain yields *c* dou.
"""

# Coefficients of the equations
# 3上 + 2中 + 1下 = 39
# 2上 + 3中 + 1下 = 34
# 1上 + 2中 + 3下 = 26

# Step 1: Represent the equations
上1, 中1, 下1, 實1 = 3, 2, 1, 39
上2, 中2, 下2, 實2 = 2, 3, 1, 34
上3, 中3, 下3, 實3 = 1, 2, 3, 26

# Step 2: Eliminate the upper grain (上禾) term from the second and third equations
# Multiply the first equation by 2 and subtract the second equation
中2_new = 中1 * 2 - 中2
下2_new = 下1 * 2 - 下2
實2_new = 實1 * 2 - 實2

# Multiply the first equation by 1 and subtract the third equation
中3_new = 中1 * 1 - 中3
下3_new = 下1 * 1 - 下3
實3_new = 實1 * 1 - 實3

# Step 3: Eliminate the middle grain (中禾) term from the third equation
# Multiply the new second equation by 中3_new and subtract the new third equation multiplied by 中2_new
下3_final = 下2_new * 中3_new - 下3_new * 中2_new
實3_final = 實2_new * 中3_new - 實3_new * 中2_new

# Solve for the lower grain (下禾)
c = Fraction(實3_final, 下3_final)

# Step 4: Solve for the middle grain (中禾) using the new second equation
實2_final = 實2_new - 下2_new * c
b = Fraction(實2_final, 中2_new)

# Step 5: Solve for the upper grain (上禾) using the first equation
實1_final = 實1 - 中1 * b - 下1 * c
a = Fraction(實1_final, 上1)

# Final results
a, b, c  # 上禾一秉 yields a斗, 中禾一秉 yields b斗, 下禾一秉 yields c斗#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 37/4, Actual: -37/2
Variable 'b' has wrong value. Expected: 17/4, Actual: 101/2
Variable 'c' has wrong value. Expected: 11/4, Actual: -13/2"""
