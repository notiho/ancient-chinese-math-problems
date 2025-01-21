"""
今有上禾七秉損實一斗益之下禾二秉而實一十斗下禾八秉益實一斗與上禾二秉而實一十斗問上下禾實一秉各幾何
術曰如方程損之曰益益之曰損損實一斗者其實過一十斗也益實一斗者其實不滿一十斗也
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b斗 下禾 c秉 實 d斗 
"""

"""
This is a complex problem involving a system of equations to determine the yield per sheaf of upper and lower millet. Let's break it down step by step and encode it in Python according to the procedure.

### Problem Breakdown:
- There are two types of millet: upper millet (上禾) and lower millet (下禾).
- The problem provides relationships between the number of sheaves (秉) and the total yield (實) for different combinations of upper and lower millet.
- The goal is to determine the yield per sheaf (實一秉) for both upper and lower millet.

### Procedure:
The procedure involves solving a system of linear equations using the ancient Chinese method of elimination (方程術). The steps are described in the problem and will be implemented in Python.

---


"""


from fractions import Fraction

# Given relationships:
# 1. 上禾 7 秉損實 1 斗益之下禾 2 秉而實 10 斗
#    => 7 * 上禾 - 1 + 2 * 下禾 = 10
# 2. 下禾 8 秉益實 1 斗與上禾 2 秉而實 10 斗
#    => 8 * 下禾 + 1 + 2 * 上禾 = 10

# Representing the equations:
# Let 上禾實 = x (yield per sheaf of upper millet)
# Let 下禾實 = y (yield per sheaf of lower millet)
# Equation 1: 7x - 1 + 2y = 10
# Equation 2: 8y + 1 + 2x = 10

# Simplify the equations:
# Equation 1: 7x + 2y = 11
# Equation 2: 2x + 8y = 9

# Step 1: Eliminate one variable using 方程術
# Multiply Equation 1 by 4 (to match the coefficient of y in Equation 2):
# 28x + 8y = 44
# Subtract Equation 2 from this:
# (28x + 8y) - (2x + 8y) = 44 - 9
# 26x = 35
x = Fraction(35, 26)  # Yield per sheaf of upper millet

# Step 2: Solve for y using Equation 1
# 7x + 2y = 11
# 2y = 11 - 7x
# y = (11 - 7x) / 2
y = Fraction(11 - 7 * x, 2)  # Yield per sheaf of lower millet

# Results:
a = 1  # Upper millet sheaf count (given in the problem)
b = x  # Yield per sheaf of upper millet
c = 1  # Lower millet sheaf count (given in the problem)
d = y  # Yield per sheaf of lower millet

print(f"上禾 {a} 秉 實 {b} 斗 下禾 {c} 秉 實 {d} 斗")


"""


### Explanation of the Code:
1. The problem is translated into a system of linear equations.
2. The elimination method (方程術) is used to solve for one variable at a time.
3. The results are expressed as fractions using the `Fraction` class to maintain precision.

### Answer:
The yield per sheaf for upper millet (上禾) and lower millet (下禾) is calculated and displayed as fractions.
"""


"""
"""
