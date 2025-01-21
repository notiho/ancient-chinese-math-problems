"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical methods, which resemble modern elimination techniques. Let's translate the problem and procedure into Python code.

### Problem Description:
We are given two conditions:
1. 3 bundles of upper millet (上禾) plus an additional 6 dou of grain are equivalent to 10 bundles of lower millet (下禾).
2. 5 bundles of lower millet plus an additional 1 dou of grain are equivalent to 2 bundles of upper millet.

We need to determine how much grain (in dou) is produced by one bundle of upper millet and one bundle of lower millet.

### Procedure:
The procedure involves setting up the equations, eliminating variables, and solving for the unknowns step by step.

### Translation into Python Code:


"""


from fractions import Fraction

# Define the coefficients of the equations based on the problem:
# Equation 1: 3上禾 - 10下禾 - 6 = 0
# Equation 2: -2上禾 + 5下禾 - 1 = 0

# Coefficients for the equations:
# [上禾系數, 下禾系數, 常數項]
equation1 = [3, -10, -6]
equation2 = [-2, 5, -1]

# Eliminate one variable (e.g., 上禾) using the elimination method:
# Multiply equation1 by 2 and equation2 by 3 to align the coefficients of 上禾:
multiplier1 = 2
multiplier2 = 3

eq1_scaled = [multiplier1 * term for term in equation1]  # 2 * equation1
eq2_scaled = [multiplier2 * term for term in equation2]  # 3 * equation2

# Subtract the scaled equations to eliminate 上禾:
# (2 * equation1) - (3 * equation2)
eliminated = [
    eq1_scaled[0] - eq2_scaled[0],  # 上禾系數 (should be 0)
    eq1_scaled[1] - eq2_scaled[1],  # 下禾系數
    eq1_scaled[2] - eq2_scaled[2],  # 常數項
]

# The resulting equation is in terms of 下禾:
# 下禾系數 * 下禾 + 常數項 = 0
下禾系數 = eliminated[1]
常數項 = eliminated[2]

# Solve for 下禾 (grain per bundle of lower millet):
下禾實 = Fraction(-常數項, 下禾系數)

# Substitute 下禾實 back into one of the original equations to solve for 上禾實:
# Using equation1: 3上禾 - 10下禾 - 6 = 0
上禾系數 = equation1[0]
下禾系數_in_eq1 = equation1[1]
常數項_in_eq1 = equation1[2]

上禾實 = Fraction(
    -(下禾系數_in_eq1 * 下禾實 + 常數項_in_eq1), 上禾系數
)

# Results:
a = 1  # One bundle of upper millet
b = 上禾實  # Grain per bundle of upper millet
c = 1  # One bundle of lower millet
d = 下禾實  # Grain per bundle of lower millet

# Output the results:
print(f"上禾 {a}秉 實 {b}斗 ，下禾 {c}秉 實 {d}斗 。")


"""


### Explanation of the Code:
1. **Equation Setup**: The two equations are represented as lists of coefficients.
2. **Elimination**: The elimination method is used to remove one variable (上禾) by scaling and subtracting the equations.
3. **Solve for 下禾**: The resulting equation is solved for 下禾 (grain per bundle of lower millet).
4. **Substitute Back**: The value of 下禾 is substituted into one of the original equations to solve for 上禾 (grain per bundle of upper millet).
5. **Output**: The results are displayed in the required format.

### Answer:
The code will compute the values of `b` (grain per bundle of upper millet) and `d` (grain per bundle of lower millet).
"""


"""
Variable 'b' has wrong value. Expected: 8, Actual: 8/7
Variable 'd' has wrong value. Expected: 3, Actual: -9/35"""
