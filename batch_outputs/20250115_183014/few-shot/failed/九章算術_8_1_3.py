"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
This problem involves solving a system of equations to determine the yield per unit (秉) of upper and lower millet. Let's break it down step by step and translate the ancient procedure into Python code.

### Problem Setup:
- Upper millet (上禾) has 7 bundles (秉), loses 1 dou, and gains 2 bundles of lower millet (下禾), resulting in a total of 10 dou.
- Lower millet (下禾) has 8 bundles, gains 1 dou, and 2 bundles of upper millet, also resulting in a total of 10 dou.
- We need to find the yield per bundle (秉) of upper millet and lower millet.

### Procedure:
The ancient text describes a method similar to solving simultaneous linear equations. Let's translate this into Python code.


"""


from fractions import Fraction

# 上禾 (upper millet) and 下禾 (lower millet) variables
# Let x = yield per bundle of upper millet (上禾實一秉)
# Let y = yield per bundle of lower millet (下禾實一秉)

# Equation 1: 7x - 1 + 2y = 10
# Simplify: 7x + 2y = 11
eq1_coeff_upper = 7  # Coefficient of x in equation 1
eq1_coeff_lower = 2  # Coefficient of y in equation 1
eq1_constant = 11    # Constant term in equation 1

# Equation 2: 8y + 1 + 2x = 10
# Simplify: 2x + 8y = 9
eq2_coeff_upper = 2  # Coefficient of x in equation 2
eq2_coeff_lower = 8  # Coefficient of y in equation 2
eq2_constant = 9     # Constant term in equation 2

# Solve the system of equations using substitution or elimination
# Multiply equation 1 by 8 and equation 2 by 2 to align coefficients of y
multiplier_eq1 = 8
multiplier_eq2 = 2

# New equations after multiplying:
# 56x + 16y = 88  (from equation 1)
# 4x + 16y = 18   (from equation 2)

# Subtract the second equation from the first to eliminate y
numerator_x = (56 - 4)  # Coefficient of x
constant_diff = (88 - 18)  # Difference of constants
x = Fraction(constant_diff, numerator_x)  # Solve for x (yield per bundle of upper millet)

# Substitute x back into one of the original equations to solve for y
# Use equation 1: 7x + 2y = 11
substituted_constant = eq1_constant - (eq1_coeff_upper * x)
y = Fraction(substituted_constant, eq1_coeff_lower)  # Solve for y (yield per bundle of lower millet)

# Results
a = 7  # Upper millet bundles
b = x  # Yield per bundle of upper millet
c = 8  # Lower millet bundles
d = y  # Yield per bundle of lower millet

print(f"上禾 {a}秉 實 {b}斗 ，下禾 {c}秉 實 {d}斗 。")


"""


### Explanation of the Code:
1. **Define the equations**: The problem gives us two equations based on the relationships between upper and lower millet yields.
2. **Align coefficients**: To eliminate one variable, we align the coefficients of `y` by multiplying the equations appropriately.
3. **Solve for one variable**: Using elimination, we solve for `x` (yield per bundle of upper millet).
4. **Substitute back**: Substitute the value of `x` into one of the original equations to solve for `y` (yield per bundle of lower millet).
5. **Output the results**: The solution gives the yield per bundle for both upper and lower millet.

### Final Answer:
The code will output the values of `a`, `b`, `c`, and `d` as required.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Variable 'c' has wrong value. Expected: 1, Actual: 8"""
