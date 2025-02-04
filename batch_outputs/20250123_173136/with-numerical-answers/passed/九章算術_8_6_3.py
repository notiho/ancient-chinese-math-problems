"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a(=34/21)兩 ，羊一，直金 b(=20/21)兩 。
"""

"""
Suppose there are 5 oxen and 2 sheep, worth 10 taels of gold. 
And 2 oxen and 5 sheep are worth 8 taels of gold.
Question: how much is each ox and each sheep worth in gold?

The procedure says: Solve using the method of simultaneous equations ("方程術").
The method of simultaneous equations says:
1. Arrange the coefficients of the unknowns (oxen and sheep) into rows, with the total values on the right-hand side.
2. Perform elimination by multiplying rows and dividing by the pivot element to simplify the system.
3. Solve for each unknown by back-substitution.

Answer: Each ox is worth *a*(=34/21) taels of gold, and each sheep is worth *b*(=20/21) taels of gold.
"""

from fractions import Fraction

# 牛五、羊二，直金十兩
牛1 = 5
羊1 = 2
金1 = 10

# 牛二、羊五，直金八兩
牛2 = 2
羊2 = 5
金2 = 8

# Eliminate one variable (羊) using the method of simultaneous equations
# Multiply the first equation by 羊2 and the second equation by 羊1
eq1_multiplier = 羊2
eq2_multiplier = 羊1

# New system after scaling
scaled_牛1 = eq1_multiplier * 牛1
scaled_羊1 = eq1_multiplier * 羊1
scaled_金1 = eq1_multiplier * 金1

scaled_牛2 = eq2_multiplier * 牛2
scaled_羊2 = eq2_multiplier * 羊2
scaled_金2 = eq2_multiplier * 金2

# Subtract the second equation from the first to eliminate 羊
eliminated_牛 = scaled_牛1 - scaled_牛2
eliminated_金 = scaled_金1 - scaled_金2

# Solve for 牛 (oxen)
牛價 = Fraction(eliminated_金, eliminated_牛)  # a = 34/21

# Substitute 牛價 back into the first equation to solve for 羊 (sheep)
羊價 = Fraction(金1 - 牛1 * 牛價, 羊1)  # b = 20/21

# Final results
a = 牛價  # 34/21
b = 羊價  # 20/21
"""
"""
