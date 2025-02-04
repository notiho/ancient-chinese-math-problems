"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a(=34/21)兩 ，羊一，直金 b(=20/21)兩 。
"""

#----- content starts here -----
"""
Suppose there are 5 oxen and 2 sheep, worth a total of 10 liang of gold.
And 2 oxen and 5 sheep are worth a total of 8 liang of gold.
Question: how much is each ox and each sheep worth in gold?

The procedure says: Solve using the method of simultaneous equations.

The method of simultaneous equations says:
Place the coefficients of the unknowns (e.g., oxen and sheep) in rows, with their totals on the right side.
Perform row operations to eliminate variables systematically, dividing by the coefficients as needed.
Continue until the values of the unknowns are determined.

Answer: Each ox is worth *a*(=34/21) liang of gold, and each sheep is worth *b*(=20/21) liang of gold.
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

# Step 1: Eliminate one variable (羊)
# Multiply the first equation by 5 and the second equation by 2 to align the coefficients of 羊
eq1牛 = 5 * 牛1  # 25
eq1羊 = 5 * 羊1  # 10
eq1金 = 5 * 金1  # 50

eq2牛 = 2 * 牛2  # 4
eq2羊 = 2 * 羊2  # 10
eq2金 = 2 * 金2  # 16

# Subtract the second equation from the first to eliminate 羊
牛差 = eq1牛 - eq2牛  # 21
金差 = eq1金 - eq2金  # 34

# Solve for 牛 (a)
a = Fraction(金差, 牛差)  # 34/21

# Step 2: Solve for 羊 (b)
# Substitute 牛 = a into the first equation
羊金 = 金1 - 牛1 * a  # Remaining value for 羊
b = Fraction(羊金, 羊1)  # 20/21

# Results:
# 牛一，直金 a(=34/21)兩
# 羊一，直金 b(=20/21)兩#----- content ends here -----

"""
"""
