"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to find the values of `a` (the amount of grain per unit for the upper field) and `b` (the amount of grain per unit for the lower field). Here's the Python code:


"""


from fractions import Fraction

# Define the equations based on the problem:
# 3a - 10b = -6
# -2a + 5b = -1

# Solve the system of equations using substitution or elimination.
# Multiply the first equation by 5 and the second equation by 10 to eliminate b:
# 15a - 50b = -30
# -20a + 50b = -10

# Add the two equations:
# (15a - 50b) + (-20a + 50b) = -30 + (-10)
# -5a = -40
a = Fraction(-40, -5)  # Simplify
a = Fraction(8)  # Upper field grain per unit

# Substitute a = 8 into the first equation to solve for b:
# 3a - 10b = -6
# 3(8) - 10b = -6
# 24 - 10b = -6
# -10b = -6 - 24
# -10b = -30
b = Fraction(-30, -10)  # Simplify
b = Fraction(3)  # Lower field grain per unit

# Results
print(f"Upper field grain per unit (a): {a}斗")
print(f"Lower field grain per unit (b): {b}斗")


"""


### Explanation of the Code:
1. The problem is represented as a system of linear equations:
   - \( 3a - 10b = -6 \)
   - \( -2a + 5b = -1 \)
2. We eliminate one variable (in this case, \( b \)) by multiplying the equations and adding them together.
3. After solving for \( a \), we substitute its value back into one of the original equations to find \( b \).
4. The results are stored in the variables `a` and `b` as fractions.

### Final Answer:
- \( a = 8 \)斗 (upper field grain per unit)
- \( b = 3 \)斗 (lower field grain per unit)
"""


"""
"""
