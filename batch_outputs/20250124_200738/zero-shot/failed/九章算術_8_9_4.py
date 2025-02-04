"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves two unknowns, \( a \) (money held by person 甲) and \( b \) (money held by person 乙). The conditions are:

1. If 甲 gets half of 乙's money, 甲 will have 50 units of money.
2. If 乙 gets more than half of 甲's money, 乙 will also have 50 units of money.

We will use the `Fraction` class to handle any fractional results.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Let a be the money held by 甲, and b be the money held by 乙.

# Equation 1: a + b/2 = 50
# Equation 2: b + (3/2)*a = 50

# Solve for a and b
# From Equation 1: a = 50 - b/2
# Substitute into Equation 2: b + (3/2)*(50 - b/2) = 50

# Simplify Equation 2:
# b + (3/2)*50 - (3/2)*(b/2) = 50
# b + 75/2 - 3b/4 = 50
# Multiply through by 4 to eliminate fractions:
# 4b + 150 - 3b = 200
# b = 200 - 150
# b = 50

# Substitute b = 50 into Equation 1:
# a + 50/2 = 50
# a + 25 = 50
# a = 50 - 25
# a = 25

a = Fraction(25)  # Money held by 甲
b = Fraction(50)  # Money held by 乙

# Results
print(f"甲持 {a} 錢")
print(f"乙持 {b} 錢")
#----- content ends here -----


"""


### Explanation:
- We first express the problem as two equations:
  1. \( a + \frac{b}{2} = 50 \)
  2. \( b + \frac{3}{2}a = 50 \)
- We solve these equations step by step to find \( a \) and \( b \).
- The solution is \( a = 25 \) and \( b = 50 \).
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 25
Variable 'b' has wrong value. Expected: 25, Actual: 50"""
