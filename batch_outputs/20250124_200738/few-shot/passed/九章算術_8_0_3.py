"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

#----- content starts here -----
"""
Suppose there are three types of grain: upper grain (shanghe), middle grain (zhonghe), and lower grain (xiahe). 
The quantities and total yields are as follows:
- 3 bundles of upper grain, 2 bundles of middle grain, and 1 bundle of lower grain yield 39 dou.
- 2 bundles of upper grain, 3 bundles of middle grain, and 1 bundle of lower grain yield 34 dou.
- 1 bundle of upper grain, 2 bundles of middle grain, and 3 bundles of lower grain yield 26 dou.

Question: How much does one bundle of upper grain, middle grain, and lower grain yield respectively?

The procedure for solving equations says:
1. Place the equations for the upper, middle, and lower grains in rows, with the total yields on the right-hand side.
2. Eliminate variables row by row using multiplication and subtraction to isolate the unknowns.
3. Solve for the lower grain first by isolating its value.
4. Substitute the value of the lower grain into the second equation to solve for the middle grain.
5. Substitute the values of the middle and lower grains into the first equation to solve for the upper grain.

Answer: One bundle of upper grain yields *a* dou, one bundle of middle grain yields *b* dou, and one bundle of lower grain yields *c* dou.
"""

from fractions import Fraction

# Coefficients and constants from the problem
# 3上 + 2中 + 1下 = 39
# 2上 + 3中 + 1下 = 34
# 1上 + 2中 + 3下 = 26

# Step 1: Represent the equations as coefficients and constants
eq1 = [3, 2, 1, 39]  # 3上, 2中, 1下, 39
eq2 = [2, 3, 1, 34]  # 2上, 3中, 1下, 34
eq3 = [1, 2, 3, 26]  # 1上, 2中, 3下, 26

# Step 2: Eliminate 上 (upper grain) from eq2 and eq3 using eq1
# Multiply eq1 by 2 and subtract from eq2
eq2 = [
    eq2[0] - Fraction(2, 3) * eq1[0],
    eq2[1] - Fraction(2, 3) * eq1[1],
    eq2[2] - Fraction(2, 3) * eq1[2],
    eq2[3] - Fraction(2, 3) * eq1[3],
]

# Multiply eq1 by 1 and subtract from eq3
eq3 = [
    eq3[0] - Fraction(1, 3) * eq1[0],
    eq3[1] - Fraction(1, 3) * eq1[1],
    eq3[2] - Fraction(1, 3) * eq1[2],
    eq3[3] - Fraction(1, 3) * eq1[3],
]

# Step 3: Eliminate 中 (middle grain) from eq3 using eq2
# Multiply eq2 by eq3[1] / eq2[1] and subtract from eq3
factor = eq3[1] / eq2[1]
eq3 = [
    eq3[0] - factor * eq2[0],
    eq3[1] - factor * eq2[1],
    eq3[2] - factor * eq2[2],
    eq3[3] - factor * eq2[3],
]

# Step 4: Solve for 下 (lower grain) from eq3
c = eq3[3] / eq3[2]

# Step 5: Solve for 中 (middle grain) from eq2
b = (eq2[3] - eq2[2] * c) / eq2[1]

# Step 6: Solve for 上 (upper grain) from eq1
a = (eq1[3] - eq1[2] * c - eq1[1] * b) / eq1[0]

# Final results
a = Fraction(a)
b = Fraction(b)
c = Fraction(c)#----- content ends here -----

"""
"""
