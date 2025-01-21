"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，中禾 c秉 實 d斗 ，下禾 e秉 實 f斗 。
"""

"""
This problem is a classic example of a system of linear equations in ancient Chinese mathematics. The solution involves solving for the amount of grain in each bundle of upper, middle, and lower-grade grain using the described method. Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# 上禾二秉，中禾三秉，下禾四秉
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 上取中，中取下，下取上各一秉而實滿斗
滿斗 = 1

# 方程術：設置未知數
# Let 上禾實 = x, 中禾實 = y, 下禾實 = z
# Equations:
# 1. x + y = 1 (上禾取中禾一秉，實滿斗)
# 2. y + z = 1 (中禾取下禾一秉，實滿斗)
# 3. z + x = 1 (下禾取上禾一秉，實滿斗)

# Solve the system of equations using substitution/elimination
# From equation 1: y = 1 - x
# Substitute y into equation 2: (1 - x) + z = 1 -> z = x
# Substitute z into equation 3: x + x = 1 -> 2x = 1 -> x = 1/2
x = Fraction(1, 2)  # 上禾實
z = x               # 下禾實
y = 1 - x           # 中禾實

# 上禾 a秉 實 b斗
a = 上禾秉數
b = x

# 中禾 c秉 實 d斗
c = 中禾秉數
d = y

# 下禾 e秉 實 f斗
e = 下禾秉數
f = z

print(f"上禾 {a}秉 實 {b}斗")
print(f"中禾 {c}秉 實 {d}斗")
print(f"下禾 {e}秉 實 {f}斗")


"""


### Explanation of the Code:
1. **Setting Up the Problem**:
   - The problem is modeled as a system of three linear equations based on the relationships between the bundles of grain.
   - Each equation represents the condition that the sum of two bundles equals one full dou.

2. **Solving the System**:
   - Using substitution and elimination, the values for `x` (upper-grade grain), `y` (middle-grade grain), and `z` (lower-grade grain) are determined.

3. **Output**:
   - The results are presented as the number of bundles and the amount of grain in each bundle.

### Final Answer:
- 上禾 2秉 實 1/2斗
- 中禾 3秉 實 1/2斗
- 下禾 4秉 實 1/2斗
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 9/25, Actual: 1/2
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 7/25, Actual: 1/2
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 4/25, Actual: 1/2"""
