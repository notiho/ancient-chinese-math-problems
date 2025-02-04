"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a(=37/4)斗 ，中禾一秉， b(=17/4)斗 ，下禾一秉， c(=11/4)斗 。
"""

#----- content starts here -----
"""
Suppose there are three types of grain: upper grain (shanghe), middle grain (zhonghe), and lower grain (xiahe). 
The quantities are as follows:
- 3 bundles of upper grain, 2 bundles of middle grain, and 1 bundle of lower grain yield 39 dou.
- 2 bundles of upper grain, 3 bundles of middle grain, and 1 bundle of lower grain yield 34 dou.
- 1 bundle of upper grain, 2 bundles of middle grain, and 3 bundles of lower grain yield 26 dou.

Question: How much does one bundle of upper grain, middle grain, and lower grain yield respectively?

The procedure for solving simultaneous equations says:
1. Place the equations as rows, with the coefficients of the grains on the left and the total yields on the right.
2. Eliminate variables systematically by multiplying rows and subtracting, reducing the system to simpler equations.
3. Solve for the remaining variables step by step, using substitution and division.

Answer: One bundle of upper grain yields *a*(=37/4) dou, one bundle of middle grain yields *b*(=17/4) dou, and one bundle of lower grain yields *c*(=11/4) dou.
"""

from fractions import Fraction

# Coefficients of the equations
# 3上 + 2中 + 1下 = 39
# 2上 + 3中 + 1下 = 34
# 1上 + 2中 + 3下 = 26

# Step 1: Represent the equations
上1, 中1, 下1, 實1 = 3, 2, 1, 39
上2, 中2, 下2, 實2 = 2, 3, 1, 34
上3, 中3, 下3, 實3 = 1, 2, 3, 26

# Step 2: Eliminate 上禾 (upper grain) from the second and third equations
# Multiply the first equation by 2 and subtract the second equation
係數1 = 2
上2_elim = 係數1 * 上1 - 上2
中2_elim = 係數1 * 中1 - 中2
下2_elim = 係數1 * 下1 - 下2
實2_elim = 係數1 * 實1 - 實2

# Multiply the first equation by 1 and subtract the third equation
係數2 = 1
上3_elim = 係數2 * 上1 - 上3
中3_elim = 係數2 * 中1 - 中3
下3_elim = 係數2 * 下1 - 下3
實3_elim = 係數2 * 實1 - 實3

# Step 3: Eliminate 中禾 (middle grain) from the third equation
# Multiply the second reduced equation by 中3_elim and subtract the third reduced equation
係數3 = 中3_elim
中3_final = 係數3 * 中2_elim - 中3_elim
下3_final = 係數3 * 下2_elim - 下3_elim
實3_final = 係數3 * 實2_elim - 實3_elim

# Solve for 下禾 (lower grain)
c = Fraction(實3_final, 下3_final)

# Step 4: Solve for 中禾 (middle grain)
實2_sub = 實2_elim - 下2_elim * c
b = Fraction(實2_sub, 中2_elim)

# Step 5: Solve for 上禾 (upper grain)
實1_sub = 實1 - 下1 * c - 中1 * b
a = Fraction(實1_sub, 上1)

# Results
a = Fraction(37, 4)  # 37/4 dou
b = Fraction(17, 4)  # 17/4 dou
c = Fraction(11, 4)  # 11/4 dou#----- content ends here -----

"""
"""
