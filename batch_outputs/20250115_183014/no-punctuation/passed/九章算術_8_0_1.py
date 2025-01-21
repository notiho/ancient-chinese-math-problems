"""
今有上禾三秉中禾二秉下禾一秉實三十九斗上禾二秉中禾三秉下禾一秉實三十四斗上禾一秉中禾二秉下禾三秉實二十六斗問上中下禾實一秉各幾何
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾 a秉  b斗 中禾 c秉  d斗 下禾 e秉  f斗 
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. The problem involves solving for the yield of one bundle of upper, middle, and lower grain based on the given relationships. Let's translate the procedure into Python code step by step.


"""


from fractions import Fraction

# Given data
# First equation: 上禾 3 秉, 中禾 2 秉, 下禾 1 秉, total 39 斗
eq1_upper = 3
eq1_middle = 2
eq1_lower = 1
eq1_total = 39

# Second equation: 上禾 2 秉, 中禾 3 秉, 下禾 1 秉, total 34 斗
eq2_upper = 2
eq2_middle = 3
eq2_lower = 1
eq2_total = 34

# Third equation: 上禾 1 秉, 中禾 2 秉, 下禾 3 秉, total 26 斗
eq3_upper = 1
eq3_middle = 2
eq3_lower = 3
eq3_total = 26

# Step 1: Solve for 下禾 (lower grain)
# Using the 方程術 procedure:
# Multiply the first equation by the 下禾 coefficient of the second equation (1),
# and subtract the second equation multiplied by the 下禾 coefficient of the first equation (1).
# This eliminates 下禾 from the first two equations.

# Eliminate 下禾 between eq1 and eq2
factor1 = eq2_lower
factor2 = eq1_lower
new_eq1_upper = eq1_upper * factor1 - eq2_upper * factor2
new_eq1_middle = eq1_middle * factor1 - eq2_middle * factor2
new_eq1_total = eq1_total * factor1 - eq2_total * factor2

# Eliminate 下禾 between eq2 and eq3
factor1 = eq3_lower
factor2 = eq2_lower
new_eq2_upper = eq2_upper * factor1 - eq3_upper * factor2
new_eq2_middle = eq2_middle * factor1 - eq3_middle * factor2
new_eq2_total = eq2_total * factor1 - eq3_total * factor2

# Step 2: Solve for 中禾 (middle grain)
# Eliminate 中禾 between the two new equations
factor1 = new_eq2_middle
factor2 = new_eq1_middle
final_upper = new_eq1_upper * factor1 - new_eq2_upper * factor2
final_total = new_eq1_total * factor1 - new_eq2_total * factor2

# Solve for 上禾 (upper grain)
upper_grain = Fraction(final_total, final_upper)

# Back-substitute to solve for 中禾
middle_grain = Fraction(new_eq1_total - new_eq1_upper * upper_grain, new_eq1_middle)

# Back-substitute to solve for 下禾
lower_grain = Fraction(eq1_total - eq1_upper * upper_grain - eq1_middle * middle_grain, eq1_lower)

# Results
a, b = 1, upper_grain  # 上禾: 1 bundle, `b` dou per bundle
c, d = 1, middle_grain  # 中禾: 1 bundle, `d` dou per bundle
e, f = 1, lower_grain  # 下禾: 1 bundle, `f` dou per bundle

print(f"上禾 {a}秉 {b}斗 中禾 {c}秉 {d}斗 下禾 {e}秉 {f}斗")


"""


### Explanation of the Code:
1. **Input the equations**: The three equations are represented with their coefficients for upper, middle, and lower grain, along with the total yield.
2. **Eliminate variables**: Following the procedure, we eliminate one variable at a time (starting with 下禾, then 中禾) by multiplying and subtracting equations.
3. **Back-substitution**: Once we isolate one variable (上禾), we substitute it back into the reduced equations to solve for the other variables.
4. **Output the results**: The yield per bundle for each type of grain is calculated and displayed.

### Answer:
The output will provide the yield per bundle for 上禾, 中禾, and 下禾 in terms of dou.
"""


"""
"""
