"""
今有甲乙二人持錢不知其數甲得乙半而錢五十乙得甲太半而亦錢五十問甲乙持錢各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰甲持 a錢 乙持 b錢 
"""

"""
Suppose there are two people, Jia and Yi, holding an unknown amount of money.
Jia takes half of Yi's money and has 50 qian.
Yi takes more than half of Jia's money and also has 50 qian.
Question: how much money does Jia and Yi each hold?

The procedure says: Solve it using the method of simultaneous equations ("fangcheng") and the principle of balancing gains and losses.

The answer says: Jia holds *a* qian, and Yi holds *b* qian.
"""

# Let Jia's money be 甲錢 and Yi's money be 乙錢.

# Equation 1: Jia takes half of Yi's money and has 50 qian.
# 甲 + 乙/2 = 50
# Equation 2: Yi takes more than half of Jia's money and also has 50 qian.
# 乙 + (3/2)甲 = 50

from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 甲 + 乙/2 = 50
coeff_1甲 = 1
coeff_1乙 = Fraction(1, 2)
const_1 = 50

# Equation 2: 乙 + (3/2)甲 = 50
coeff_2甲 = Fraction(3, 2)
coeff_2乙 = 1
const_2 = 50

# Solve using substitution or elimination
# Multiply Equation 1 by 2 to eliminate fractions
coeff_1甲 *= 2
coeff_1乙 *= 2
const_1 *= 2

# Updated Equation 1: 2甲 + 乙 = 100
# Equation 2 remains: (3/2)甲 + 乙 = 50

# Eliminate 乙 by subtracting Equation 2 from Equation 1
# (2甲 + 乙) - ((3/2)甲 + 乙) = 100 - 50
eliminated_甲 = 2 - Fraction(3, 2)
eliminated_const = 100 - 50

# Solve for 甲
甲 = eliminated_const / eliminated_甲

# Substitute 甲 back into Equation 1 to solve for 乙
乙 = const_1 - coeff_1甲 * 甲

# Final answers
a = 甲
b = 乙
"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
