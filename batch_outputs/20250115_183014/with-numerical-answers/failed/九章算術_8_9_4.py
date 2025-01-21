"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲持 a(=75/2)錢 ，乙持 b(=25)錢 。
"""

"""
Suppose there are two people, Jia and Yi, holding an unknown amount of money.
If Jia takes half of Yi's money, he will have 50 qian.
If Yi takes more than half of Jia's money, he will also have 50 qian.
Question: how much money does Jia and Yi each hold?

The procedure says: Use the method of simultaneous equations and balance the gains and losses.

The method of simultaneous equations is as follows:
1. Place the coefficients of the unknowns (the "heaps") in rows, with the total (the "result") on the right.
2. Multiply the rows and divide directly to eliminate variables, working step by step.
3. Solve for the remaining variables by substitution and elimination.

The answer says: Jia holds *a*(=75/2) qian, and Yi holds *b*(=25) qian.
"""

from fractions import Fraction

# Let 甲持錢 be x (Jia's money) and 乙持錢 be y (Yi's money).
# Equation 1: x + y/2 = 50
# Equation 2: y + (3/2)x = 50

# Rewrite the equations:
# Equation 1: 2x + y = 100
# Equation 2: 3x + 2y = 100

# Step 1: Eliminate y by aligning coefficients.
# Multiply Equation 1 by 2: 4x + 2y = 200
# Subtract Equation 2: (4x + 2y) - (3x + 2y) = 200 - 100
# Result: x = 100

# Step 2: Solve for y using Equation 1.
# Substitute x = 100 into 2x + y = 100:
# 2(100) + y = 100
# y = 100 - 200

"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
