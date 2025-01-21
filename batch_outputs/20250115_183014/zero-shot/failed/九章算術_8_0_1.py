"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾 a秉 ， b斗 ，中禾 c秉 ， d斗 ，下禾 e秉 ， f斗 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem describes a system of linear equations, and we will solve it step by step using the given method. Here's the Python code:


"""


from fractions import Fraction

# Define the equations based on the problem:
# 3a + 2c + 1e = 39
# 2a + 3c + 1e = 34
# 1a + 2c + 3e = 26

# Step 1: Solve for e (下禾)
# Multiply the first equation by 2 and the second equation by 3, then subtract:
# 6a + 4c + 2e = 78
# 6a + 9c + 3e = 102
# Subtracting gives: -5c - e = -24 -> e = -5c + 24

# Step 2: Substitute e into the first two equations to solve for a and c:
# Substitute e = -5c + 24 into the first equation:
# 3a + 2c + (-5c + 24) = 39 -> 3a - 3c + 24 = 39 -> 3a - 3c = 15 -> a - c = 5 -> a = c + 5

# Substitute e = -5c + 24 into the second equation:
# 2a + 3c + (-5c + 24) = 34 -> 2a - 2c + 24 = 34 -> 2a - 2c = 10 -> a - c = 5 -> a = c + 5

# Step 3: Solve for c:
# Substitute a = c + 5 into the third equation:
# 1a + 2c + 3e = 26
# (c + 5) + 2c + 3(-5c + 24) = 26
# c + 5 + 2c - 15c + 72 = 26
# -12c + 77 = 26
# -12c = -51
c = Fraction(-51, -12)  # Simplify the fraction
c = Fraction(17, 4)  # 中禾 (c 秉)

# Step 4: Solve for a:
a = c + 5  # 上禾 (a 秉)
a = Fraction(17, 4) + 5
a = Fraction(37, 4)

# Step 5: Solve for e:
e = -5 * c + 24  # 下禾 (e 秉)
e = -5 * Fraction(17, 4) + 24
e = Fraction(-85, 4) + 24
e = Fraction(11, 4)

# Step 6: Solve for the斗 (斗 values):
# Substitute the 秉 values into the equations to find the斗 values:
b = a  # 上禾 (b 斗)
d = c  # 中禾 (d 斗)
f = e  # 下禾 (f 斗)

# Final results:
a = Fraction(37, 4)  # 上禾 秉
b = Fraction(37, 4)  # 上禾 斗
c = Fraction(17, 4)  # 中禾 秉
d = Fraction(17, 4)  # 中禾 斗
e = Fraction(11, 4)  # 下禾 秉
f = Fraction(11, 4)  # 下禾 斗


"""


### Explanation of the Results:
- `a` and `b` represent the number of 秉 and 斗 for 上禾 (upper grain).
- `c` and `d` represent the number of 秉 and 斗 for 中禾 (middle grain).
- `e` and `f` represent the number of 秉 and 斗 for 下禾 (lower grain).

The final values are:
- 上禾: `a = 37/4`, `b = 37/4`
- 中禾: `c = 17/4`, `d = 17/4`
- 下禾: `e = 11/4`, `f = 11/4`
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 37/4
Variable 'c' has wrong value. Expected: 1, Actual: 17/4
Variable 'e' has wrong value. Expected: 1, Actual: 11/4"""
