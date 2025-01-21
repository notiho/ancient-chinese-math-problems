"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves two unknowns, \( a \) (money held by person 甲) and \( b \) (money held by person 乙). The conditions are:

1. If 甲 (a) takes half of 乙's (b) money, they will have 50 units of money.
   \[
   a + \frac{b}{2} = 50
   \]

2. If 乙 (b) takes more than half of 甲's (a) money, they will also have 50 units of money.
   \[
   b + \frac{3a}{2} = 50
   \]

We will solve these equations using Python.


"""


from fractions import Fraction

# Define the equations
# a + b/2 = 50
# b + 3a/2 = 50

# Solve for a and b
# From the first equation: b = 2 * (50 - a)
# Substitute b into the second equation:
# 2 * (50 - a) + 3a/2 = 50
# Simplify:
# 100 - 2a + 3a/2 = 50
# Multiply through by 2 to eliminate fractions:
# 200 - 4a + 3a = 100
# Simplify:
# -a = -100
# a = 100

# Substitute a = 100 into the first equation to find b:
# b = 2 * (50 - 100)
# b = 2 * (-50)
# b = -100

# Assign the results to variables
a = Fraction(100)  # 甲持錢
b = Fraction(-100)  # 乙持錢

# Output the results
a, b


"""


The solution is:
- \( a = 100 \) (甲持錢)
- \( b = -100 \) (乙持錢)


"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
