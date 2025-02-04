"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a(=37/4)斗 ，中禾一秉， b(=17/4)斗 ，下禾一秉， c(=11/4)斗 。
"""

"""
Suppose there are three types of grain: upper grain (shanghe), middle grain (zhonghe), and lower grain (xiahe).
Three bundles of upper grain, two bundles of middle grain, and one bundle of lower grain yield 39 dou.
Two bundles of upper grain, three bundles of middle grain, and one bundle of lower grain yield 34 dou.
One bundle of upper grain, two bundles of middle grain, and three bundles of lower grain yield 26 dou.
Question: how much does one bundle of upper, middle, and lower grain yield respectively?

The procedure for solving simultaneous equations says:
1. Place the first equation (3 upper grain, 2 middle grain, 1 lower grain, yielding 39 dou) on the right side.
2. Arrange the second and third equations similarly.
3. Multiply the upper grain coefficient in the second equation by the first equation and divide directly.
4. Repeat for the third equation.
5. For the middle grain, multiply the middle grain coefficient in the third equation by the second equation and divide directly.
6. For the lower grain, use the remaining coefficients to calculate its value.
7. Solve for the middle grain and upper grain using the calculated values of the lower grain.

Answer: One bundle of upper grain yields *a*(=37/4) dou, one bundle of middle grain yields *b*(=17/4) dou, and one bundle of lower grain yields *c*(=11/4) dou.
"""

from fractions import Fraction

# Equations:
# 3上 + 2中 + 1下 = 39
# 2上 + 3中 + 1下 = 34
# 1上 + 2中 + 3下 = 26

# Step 1: Eliminate "上禾" (upper grain) from the second and third equations
# Multiply the first equation by 2 and subtract the second equation
# Multiply the first equation by 1 and subtract the third equation

# First equation: 3上 + 2中 + 1下 = 39
eq1_upper = 3
eq1_middle = 2
eq1_lower = 1
eq1_result = 39

# Second equation: 2上 + 3中 + 1下 = 34
eq2_upper = 2
eq2_middle = 3
eq2_lower = 1
eq2_result = 34

# Third equation: 1上 + 2中 + 3下 = 26
eq3_upper = 1
eq3_middle = 2
eq3_lower = 3
eq3_result = 26

# Eliminate "上禾" from the second equation
factor2 = Fraction(eq1_upper, eq2_upper)
eq2_middle = eq2_middle * factor2 - eq1_middle
eq2_lower = eq2_lower * factor2 - eq1_lower
eq2_result = eq2_result * factor2 - eq1_result

# Eliminate "上禾" from the third equation
factor3 = Fraction(eq1_upper, eq3_upper)
eq3_middle = eq3_middle * factor3 - eq1_middle
eq3_lower = eq3_lower * factor3 - eq1_lower
eq3_result = eq3_result * factor3 - eq1_result

# Step 2: Eliminate "中禾" (middle grain) from the third equation
factor4 = Fraction(eq2_middle, eq3_middle)
eq3_lower = eq3_lower * factor4 - eq2_lower
eq3_result = eq3_result * factor4 - eq2_result

# Step 3: Solve for "下禾" (lower grain)
下禾 = Fraction(eq3_result, eq3_lower)

# Step 4: Solve for "中禾" (middle grain)
中禾 = Fraction(eq2_result - eq2_lower * 下禾, eq2_middle)

# Step 5: Solve for "上禾" (upper grain)
上禾 = Fraction(eq1_result - eq1_middle * 中禾 - eq1_lower * 下禾, eq1_upper)

# Final results
a = 上禾  # 37/4
b = 中禾  # 17/4
c = 下禾  # 11/4
"""
"""
