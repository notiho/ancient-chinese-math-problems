"""
今有甲乙丙三人持錢不知多少甲言我得乙大半得丙少半可滿一百乙言我得甲大半得丙半可滿一百丙言我得甲乙各大半可滿一百問甲乙丙持錢各幾何
術曰三甲二乙一丙錢三百四甲六乙三丙錢六百二甲二乙三丙錢三百如方程即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
答曰甲 a 乙 b 丙 c
"""

#----- content starts here -----
"""
Suppose there are three people, Jia, Yi, and Bing, each holding an unknown amount of money.

Jia says: If I take more than half of Yi's money and less than half of Bing's money, I can make 100.
Yi says: If I take more than half of Jia's money and half of Bing's money, I can make 100.
Bing says: If I take more than half of both Jia's and Yi's money, I can make 100.

Question: How much money do Jia, Yi, and Bing each hold?

The procedure says: 
- Form equations based on the statements:
  3 Jia + 2 Yi + 1 Bing = 300
  4 Jia + 6 Yi + 3 Bing = 600
  2 Jia + 2 Yi + 3 Bing = 300
- Solve the system of equations using the method of elimination.

Answer: Jia holds *a*, Yi holds *b*, and Bing holds *c*.
"""

from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 3甲 + 2乙 + 1丙 = 300
eq1_jia = 3
eq1_yi = 2
eq1_bing = 1
eq1_total = 300

# Equation 2: 4甲 + 6乙 + 3丙 = 600
eq2_jia = 4
eq2_yi = 6
eq2_bing = 3
eq2_total = 600

# Equation 3: 2甲 + 2乙 + 3丙 = 300
eq3_jia = 2
eq3_yi = 2
eq3_bing = 3
eq3_total = 300

# Step 1: Eliminate one variable (丙) using equations 1 and 2
# Multiply eq1 by 3 and eq2 by 1 to align 丙 coefficients
eq1_mult = 3
eq2_mult = 1

new_eq1_jia = eq1_jia * eq1_mult
new_eq1_yi = eq1_yi * eq1_mult
new_eq1_bing = eq1_bing * eq1_mult
new_eq1_total = eq1_total * eq1_mult

new_eq2_jia = eq2_jia * eq2_mult
new_eq2_yi = eq2_yi * eq2_mult
new_eq2_bing = eq2_bing * eq2_mult
new_eq2_total = eq2_total * eq2_mult

# Subtract the equations to eliminate 丙
eliminated_eq1_jia = new_eq2_jia - new_eq1_jia
eliminated_eq1_yi = new_eq2_yi - new_eq1_yi
eliminated_eq1_total = new_eq2_total - new_eq1_total

# Step 2: Eliminate 丙 using equations 1 and 3
# Multiply eq1 by 3 and eq3 by 1 to align 丙 coefficients
eq3_mult = 1

new_eq3_jia = eq3_jia * eq3_mult
new_eq3_yi = eq3_yi * eq3_mult
new_eq3_bing = eq3_bing * eq3_mult
new_eq3_total = eq3_total * eq3_mult

# Subtract the equations to eliminate 丙
eliminated_eq2_jia = new_eq3_jia - new_eq1_jia
eliminated_eq2_yi = new_eq3_yi - new_eq1_yi
eliminated_eq2_total = new_eq3_total - new_eq1_total

# Step 3: Solve for 乙 using the two reduced equations
# Combine the two reduced equations
# Equation A: eliminated_eq1_jia * 甲 + eliminated_eq1_yi * 乙 = eliminated_eq1_total
# Equation B: eliminated_eq2_jia * 甲 + eliminated_eq2_yi * 乙 = eliminated_eq2_total

# Multiply to align coefficients of 甲
eqA_mult = eliminated_eq2_jia
eqB_mult = eliminated_eq1_jia

aligned_eqA_yi = eliminated_eq1_yi * eqA_mult
aligned_eqA_total = eliminated_eq1_total * eqA_mult

aligned_eqB_yi = eliminated_eq2_yi * eqB_mult
aligned_eqB_total = eliminated_eq2_total * eqB_mult

# Subtract the equations to eliminate 甲
final_yi_coeff = aligned_eqA_yi - aligned_eqB_yi
final_yi_total = aligned_eqA_total - aligned_eqB_total

# Solve for 乙
yi = Fraction(final_yi_total, final_yi_coeff)

# Step 4: Solve for 甲 using one of the reduced equations
jia = Fraction(eliminated_eq1_total - (eliminated_eq1_yi * yi), eliminated_eq1_jia)

# Step 5: Solve for 丙 using the original equation 1
bing = Fraction(eq1_total - (eq1_jia * jia) - (eq1_yi * yi), eq1_bing)

# Final results
a = jia
b = yi
c = bing#----- content ends here -----

"""
"""
