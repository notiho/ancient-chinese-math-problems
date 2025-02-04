"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese procedure into Python code step by step. The problem involves solving a system of linear equations to determine the yield of one秉 (bundle) of 上禾 (upper grain) and 下禾 (lower grain). Here's the implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem statement:
# Equation 1: 7 * 上禾 - 1 + 2 * 下禾 = 10
# Equation 2: 8 * 下禾 + 1 + 2 * 上禾 = 10

# Rewrite the equations to standard form:
# 7 * 上禾 + 2 * 下禾 = 11
# 2 * 上禾 + 8 * 下禾 = 9

# Coefficients of the equations
a1, b1, c1 = 7, 2, 11  # Coefficients for the first equation
a2, b2, c2 = 2, 8, 9   # Coefficients for the second equation

# Solve using elimination method
# Multiply the first equation by b2 and the second equation by b1 to align 下禾 terms
mult1 = b2
mult2 = b1

new_a1 = a1 * mult1
new_b1 = b1 * mult1
new_c1 = c1 * mult1

new_a2 = a2 * mult2
new_b2 = b2 * mult2
new_c2 = c2 * mult2

# Subtract the second equation from the first to eliminate 下禾
final_a = new_a1 - new_a2
final_c = new_c1 - new_c2

# Solve for 上禾
上禾 = Fraction(final_c, final_a)

# Substitute 上禾 back into one of the original equations to solve for 下禾
下禾 = Fraction(c1 - a1 * 上禾, b1)

# Results
a = 上禾
b = 下禾

# Output the results
print(f"上禾一秉實 {a}斗 ，下禾一秉實 {b}斗 。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Equations Setup**: The problem provides two equations derived from the conditions of the yields of 上禾 and 下禾. These equations are rewritten in standard linear form.
2. **Elimination Method**: The elimination method is used to solve the system of equations. This involves aligning the coefficients of one variable (下禾) and subtracting the equations to solve for the other variable (上禾).
3. **Substitution**: Once 上禾 is determined, it is substituted back into one of the original equations to solve for 下禾.
4. **Fraction Representation**: The `Fraction` class is used to ensure exact arithmetic, as the results may not be integers.

### Output:
The code will output the yield of one秉 of 上禾 and 下禾 in斗.
"""


"""
"""
