"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，中禾 c秉 實 d斗 ，下禾 e秉 實 f斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the actual amount of grain in each type of bundle (上禾, 中禾, 下禾) such that the conditions are satisfied.

Here is the Python code:


"""


from fractions import Fraction

# Given information
# 上禾 (a 秉), 中禾 (c 秉), 下禾 (e 秉)
a = 2  # 上禾 bundles
c = 3  # 中禾 bundles
e = 4  # 下禾 bundles

# Total amount of grain when bundles are exchanged
# 上取中, 中取下, 下取上 each one bundle and all become full (1斗 each)
# Let b, d, f represent the actual amount of grain in one bundle of 上禾, 中禾, 下禾 respectively.

# Equations based on the problem:
# 1. b + d + d = 1 (上禾 takes one 中禾 bundle)
# 2. d + f + f = 1 (中禾 takes one 下禾 bundle)
# 3. f + b + b = 1 (下禾 takes one 上禾 bundle)

# Solve the equations
# From equation 1: b + 2d = 1
# From equation 2: d + 2f = 1
# From equation 3: f + 2b = 1

# Solve for b, d, f
d = Fraction(1, 3)  # From equation 2: d = 1 - 2f, substitute f = 1 - 2b into d = 1 - 2f
f = Fraction(1, 3)  # From equation 3: f = 1 - 2b
b = Fraction(1, 3)  # From equation 1: b = 1 - 2d

# Results
# 上禾 a秉 實 b斗
# 中禾 c秉 實 d斗
# 下禾 e秉 實 f斗

print(f"上禾 {a}秉 實 {b}斗")
print(f"中禾 {c}秉 實 {d}斗")
print(f"下禾 {e}秉 實 {f}斗")


"""


### Explanation of the Code:
1. The problem provides three equations based on the exchange of bundles and the total amount of grain in each bundle.
2. We solve these equations using substitution to find the values of `b`, `d`, and `f`, which represent the actual amount of grain in one bundle of 上禾, 中禾, and 下禾, respectively.
3. The results are printed in the required format.

### Output:
```
上禾 2秉 實 1/3斗
中禾 3秉 實 1/3斗
下禾 4秉 實 1/3斗
```
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 9/25, Actual: 1/3
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 7/25, Actual: 1/3
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 4/25, Actual: 1/3"""
