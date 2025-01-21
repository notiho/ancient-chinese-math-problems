"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
To solve the problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves solving a system of linear equations using the given relationships. Let's compute the values step by step.

Here is the Python code:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Equation 1: 3a - 10c = -6
# Equation 2: -2a + 5c = -1

# Solve for 'a' (the amount of grain per秉 for 上禾) and 'c' (the amount of grain per秉 for 下禾):
# Step 1: Solve for 'c' in terms of 'a' using Equation 1
# 3a - 10c = -6
# 10c = 3a + 6
# c = (3a + 6) / 10

# Step 2: Substitute 'c' into Equation 2
# -2a + 5c = -1
# -2a + 5((3a + 6) / 10) = -1
# Multiply through by 10 to eliminate fractions:
# -20a + 15a + 30 = -10
# -5a + 30 = -10
# -5a = -40
# a = 8

# Step 3: Substitute 'a' back into the expression for 'c'
# c = (3a + 6) / 10
# c = (3(8) + 6) / 10
# c = (24 + 6) / 10
# c = 30 / 10
# c = 3

# Step 4: Compute the actual grain amounts per秉 for 上禾 and 下禾:
# 上禾实 per秉 (b) = a = 8斗
# 下禾实 per秉 (d) = c = 3斗

# Assign the results to variables
a = Fraction(8)  # 上禾秉数
b = Fraction(8)  # 上禾实 per秉
c = Fraction(3)  # 下禾秉数
d = Fraction(3)  # 下禾实 per秉


"""


### Results:
- 上禾秉数 \( a = 8 \)
- 上禾实 per秉 \( b = 8斗 \)
- 下禾秉数 \( c = 3 \)
- 下禾实 per秉 \( d = 3斗 \)
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 8
Variable 'c' has wrong value. Expected: 1, Actual: 3"""
