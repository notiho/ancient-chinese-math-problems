"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a(=1)秉 實 b(=35/26)斗 ，下禾 c(=1)秉 實 d(=41/52)斗 。
"""

"""
This problem is a classic system of linear equations problem, where the relationships between the quantities of upper and lower grains (上禾 and 下禾) are described. The solution involves solving the equations step by step using the method described in the ancient Chinese text.

Let's break this down into Python code:


"""


from fractions import Fraction

# Problem setup:
# 上禾 (upper grain) and 下禾 (lower grain) quantities are unknown.
# We are given two equations based on the problem description.

# Equation 1: 7 上禾 - 1 + 2 下禾 = 10
# Equation 2: 8 下禾 + 1 + 2 上禾 = 10

# Rewrite the equations:
# 7a - 1 + 2b = 10  ->  7a + 2b = 11
# 8b + 1 + 2a = 10  ->  2a + 8b = 9

# Step 1: Solve for one variable in terms of the other.
# Multiply the first equation by 4 to align coefficients of `a`:
# 28a + 8b = 44
# Subtract the second equation from this:
# (28a + 8b) - (2a + 8b) = 44 - 9
# 26a = 35
a = Fraction(35, 26)  # Value of 上禾 per 秉

# Step 2: Substitute `a` into one of the original equations to solve for `b`.
# Using the first equation: 7a + 2b = 11
# 7 * (35/26) + 2b = 11
# 245/26 + 2b = 11
# 2b = 11 - 245/26
# 2b = (286/26) - (245/26)
# 2b = 41/26
# b = (41/26) / 2
b = Fraction(41, 52)  # Value of 下禾 per 秉

# Final results:
# 上禾實一秉 (a) = 35/26 斗
# 下禾實一秉 (b) = 41/52 斗

print(f"上禾實一秉: {a} 斗")
print(f"下禾實一秉: {b} 斗")


"""


### Explanation of the Code:
1. The problem is translated into two linear equations:
   - \( 7a + 2b = 11 \)
   - \( 2a + 8b = 9 \)
2. The first equation is scaled to align the coefficients of \( b \), and the second equation is subtracted to isolate \( a \).
3. Once \( a \) is solved, it is substituted back into one of the original equations to solve for \( b \).
4. The results are expressed as fractions using the `Fraction` class to maintain exactness.

### Final Answer:
- 上禾實一秉: \( \frac{35}{26} \) 斗
- 下禾實一秉: \( \frac{41}{52} \) 斗
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 35/26
Variable 'b' has wrong value. Expected: 35/26, Actual: 41/52
Missing variable in output: 'c'
Missing variable in output: 'd'"""
