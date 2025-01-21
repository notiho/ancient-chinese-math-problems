"""
今有甲乙丙三人持錢不知多少甲言我得乙大半得丙少半可滿一百乙言我得甲大半得丙半可滿一百丙言我得甲乙各大半可滿一百問甲乙丙持錢各幾何
術曰三甲二乙一丙錢三百四甲六乙三丙錢六百二甲二乙三丙錢三百如方程即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗答曰甲 a 乙 b 丙 c
"""

"""
Suppose there are three people, Jia, Yi, and Bing, each holding an unknown amount of money.
Jia says: If I take more than half of Yi's money and less than half of Bing's money, I will have exactly 100.
Yi says: If I take more than half of Jia's money and half of Bing's money, I will have exactly 100.
Bing says: If I take more than half of Jia's money and more than half of Yi's money, I will have exactly 100.
Question: How much money does each of Jia, Yi, and Bing hold?

The procedure says: 
- Form three equations:
  3 Jia + 2 Yi + 1 Bing = 300
  4 Jia + 6 Yi + 3 Bing = 600
  2 Jia + 2 Yi + 3 Bing = 300
- Solve these equations using the method of elimination.

The elimination method says:
- Place the coefficients of the unknowns (Jia, Yi, Bing) in rows, and place the constants on the right-hand side.
- Use the first row to eliminate the coefficients of Jia in the second and third rows.
- Use the second row to eliminate the coefficients of Yi in the third row.
- Solve for Bing, then back-substitute to find Yi and Jia.

Answer: Jia has *a*, Yi has *b*, and Bing has *c*.
"""

from fractions import Fraction

# Coefficients and constants from the equations
# 3 Jia + 2 Yi + 1 Bing = 300
# 4 Jia + 6 Yi + 3 Bing = 600
# 2 Jia + 2 Yi + 3 Bing = 300

# Initial coefficients
A1, B1, C1, D1 = 3, 2, 1, 300
A2, B2, C2, D2 = 4, 6, 3, 600
A3, B3, C3, D3 = 2, 2, 3, 300

# Step 1: Eliminate Jia from the second and third equations
# Multiply the first equation by 4 and subtract the second equation
factor = Fraction(A2, A1)
A2 -= factor * A1
B2 -= factor * B1
C2 -= factor * C1
D2 -= factor * D1

# Multiply the first equation by 2 and subtract the third equation
factor = Fraction(A3, A1)
A3 -= factor * A1
B3 -= factor * B1
C3 -= factor * C1
D3 -= factor * D1

# Step 2: Eliminate Yi from the third equation
# Multiply the second equation by the appropriate factor
factor = Fraction(B3, B2)
A3 -= factor * A2
B3 -= factor * B2
C3 -= factor * C2
D3 -= factor * D2

# Step 3: Solve for Bing (C3)
c = Fraction(D3, C3)

# Step 4: Back-substitute to find Yi (B2)
b = Fraction(D2 - C2 * c, B2)

# Step 5: Back-substitute to find Jia (A1)
a = Fraction(D1 - B1 * b - C1 * c, A1)

# Results
a, b, c  # Jia, Yi, Bing
"""
"""
