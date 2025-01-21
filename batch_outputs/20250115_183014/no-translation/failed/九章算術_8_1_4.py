"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
To solve this problem, we need to follow the ancient Chinese method of solving simultaneous equations, as described in the procedure. Here's the Python implementation:


"""


from fractions import Fraction

# Define the problem as simultaneous equations:
# Let x = the amount of grain per秉 for 上禾 (upper grain)
# Let y = the amount of grain per秉 for 下禾 (lower grain)

# Equation 1: 7x - 1 + 2y = 10
# Equation 2: 8y + 1 + 2x = 10

# Rearrange the equations to standard form:
# 7x + 2y = 11  (from Equation 1)
# 2x + 8y = 9   (from Equation 2)

# Solve using the elimination method:
# Multiply the first equation by 8 and the second equation by 2 to align coefficients of y:
# 56x + 16y = 88
# 4x + 16y = 18

# Subtract the second equation from the first:
# 56x - 4x = 88 - 18
# 52x = 70
x = Fraction(70, 52)  # Simplify the fraction
x = Fraction(35, 26)

# Substitute x back into the first equation to solve for y:
# 7x + 2y = 11
# 2y = 11 - 7x
# y = (11 - 7x) / 2
y = Fraction(11 - 7 * x, 2)

# Results:
a = 7  # 上禾秉数
b = x  # 上禾每秉实
c = 8  # 下禾秉数
d = y  # 下禾每秉实

# Output the results:
print(f"上禾 {a}秉 实 {b}斗")
print(f"下禾 {c}秉 实 {d}斗")


"""


### Explanation:
1. The problem is modeled as two simultaneous equations based on the given conditions.
2. The elimination method is used to solve for `x` (the grain per秉 for 上禾) and `y` (the grain per秉 for 下禾).
3. The results are expressed as fractions to maintain precision, as required by the ancient method.

### Final Answer:
- 上禾 7秉 实 \( \frac{35}{26} \)斗
- 下禾 8秉 实 \( \frac{51}{26} \)斗
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Variable 'c' has wrong value. Expected: 1, Actual: 8"""
