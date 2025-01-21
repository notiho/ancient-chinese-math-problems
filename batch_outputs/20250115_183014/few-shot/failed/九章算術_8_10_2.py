"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This is a classic simultaneous equations problem from ancient Chinese mathematics. The problem involves solving for the price of a horse and a cow using the method of elimination, which is described in the "fangcheng" (方程) procedure. Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# Problem setup
# 2馬 + 1牛 = 10000 (如半馬之價)
# 1馬 + 2牛 = 10000 (如半牛之價)

# Representing the equations:
# Let 馬 = x (price of a horse), 牛 = y (price of a cow)
# Equation 1: 2x + y = 10000
# Equation 2: x + 2y = 10000

# Step 1: Eliminate one variable (using 方程術)
# Multiply Equation 1 by 2 to align coefficients of y
eq1 = [2 * 2, 2 * 1, 2 * 10000]  # [4x, 2y, 20000]
eq2 = [1, 2, 10000]              # [x, 2y, 10000]

# Subtract Equation 2 from Equation 1 to eliminate y
# (4x + 2y) - (x + 2y) = 20000 - 10000
eliminated_eq = [eq1[0] - eq2[0], eq1[1] - eq2[1], eq1[2] - eq2[2]]  # [3x, 0, 10000]
# Result: 3x = 10000

# Step 2: Solve for x (price of a horse)
馬價 = Fraction(eliminated_eq[2], eliminated_eq[0])  # x = 10000 / 3

# Step 3: Substitute x back into one of the original equations to solve for y
# Using Equation 1: 2x + y = 10000
# y = 10000 - 2x
牛價 = Fraction(10000 - 2 * 馬價, 1)  # y = 10000 - 2 * (10000 / 3)

# Final results
a = 馬價
b = 牛價

# Output the results
print(f"馬價: {a} 錢")
print(f"牛價: {b} 錢")


"""


### Explanation of the Code:
1. **Equation Representation**: The two equations are represented in terms of `x` (price of a horse) and `y` (price of a cow).
2. **Elimination**: The coefficients of `y` are aligned by multiplying the first equation by 2. Then, the second equation is subtracted from the first to eliminate `y`.
3. **Solve for `x`**: The resulting equation is solved for `x` (price of a horse).
4. **Substitution**: The value of `x` is substituted back into one of the original equations to solve for `y` (price of a cow).
5. **Result**: The prices of the horse and cow are expressed as fractions for precision.

### Answer:
The price of a horse is `a` 錢, and the price of a cow is `b` 錢.
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 10000/3
Variable 'b' has wrong value. Expected: 20000/11, Actual: 10000/3"""
