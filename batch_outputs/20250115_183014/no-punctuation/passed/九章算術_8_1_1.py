"""
今有上禾七秉損實一斗益之下禾二秉而實一十斗下禾八秉益實一斗與上禾二秉而實一十斗問上下禾實一秉各幾何
術曰如方程損之曰益益之曰損損實一斗者其實過一十斗也益實一斗者其實不滿一十斗也
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b斗 下禾 c秉 實 d斗 
"""

"""
This problem involves solving a system of equations to determine the yield per unit of "upper millet" (上禾) and "lower millet" (下禾). The procedure uses a method similar to elimination and substitution to solve the equations step by step.

### Problem Restatement:
There are two types of millet: upper millet (上禾) and lower millet (下禾). The relationships between their quantities and yields are given as follows:
1. 7 units of upper millet lose 1 dou of yield, but when combined with 2 units of lower millet, the total yield is 10 dou.
2. 8 units of lower millet gain 1 dou of yield, but when combined with 2 units of upper millet, the total yield is 10 dou.

The goal is to determine the yield per unit of upper millet and lower millet.

### Procedure:
The procedure involves setting up and solving equations based on the relationships provided. The steps are as follows:
1. Represent the yield per unit of upper millet as \( x \) and the yield per unit of lower millet as \( y \).
2. Translate the problem into equations:
   - From the first condition: \( 7x - 1 + 2y = 10 \)
   - From the second condition: \( 8y + 1 + 2x = 10 \)
3. Solve the system of equations using substitution or elimination.

### Solution in Python Code:


"""


from fractions import Fraction

# Define the equations based on the problem statement:
# 7x - 1 + 2y = 10
# 8y + 1 + 2x = 10

# Rearrange the equations:
# Equation 1: 7x + 2y = 11
# Equation 2: 2x + 8y = 9

# Coefficients for the equations:
# Equation 1: 7x + 2y = 11
a1, b1, c1 = 7, 2, 11

# Equation 2: 2x + 8y = 9
a2, b2, c2 = 2, 8, 9

# Solve for x and y using elimination:
# Multiply the first equation by 8 and the second equation by 2 to align the coefficients of y:
# 8 * (7x + 2y) = 8 * 11 -> 56x + 16y = 88
# 2 * (2x + 8y) = 2 * 9  ->  4x + 16y = 18

# Subtract the second equation from the first:
# (56x + 16y) - (4x + 16y) = 88 - 18
# 52x = 70
x = Fraction(70, 52)

# Simplify x:
x = Fraction(35, 26)

# Substitute x into one of the original equations to solve for y:
# Use Equation 1: 7x + 2y = 11
# 7 * (35/26) + 2y = 11
# 245/26 + 2y = 11
# 2y = 11 - 245/26
# 2y = (286/26) - (245/26)
# 2y = 41/26
y = Fraction(41, 52)

# Final results:
a = 1  # Upper millet units (上禾秉)
b = x  # Yield per unit of upper millet (上禾實)
c = 1  # Lower millet units (下禾秉)
d = y  # Yield per unit of lower millet (下禾實)

# Output the results:
print(f"上禾 {a}秉 實 {b}斗")
print(f"下禾 {c}秉 實 {d}斗")


"""


### Explanation of the Code:
1. The equations are derived from the problem statement and rearranged for simplicity.
2. The elimination method is used to solve for \( x \) (yield per unit of upper millet).
3. The value of \( x \) is substituted back into one of the equations to solve for \( y \) (yield per unit of lower millet).
4. The results are presented as fractions for precision.

### Final Answer:
- Upper millet: \( a = 1 \) unit, \( b = \frac{35}{26} \) dou per unit.
- Lower millet: \( c = 1 \) unit, \( d = \frac{41}{52} \) dou per unit.
"""


"""
"""
