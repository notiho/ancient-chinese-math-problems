"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，中禾 c秉 實 d斗 ，下禾 e秉 實 f斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves determining the actual contents (in斗) of one秉 (bundle) of 上禾 (upper grain), 中禾 (middle grain), and 下禾 (lower grain). The solution will use the `Fraction` class to handle fractional values.

Here is the Python code:


"""


from fractions import Fraction

# Given data
# 上禾 (a秉), 中禾 (c秉), 下禾 (e秉)
a = 2  # 秉
c = 3  # 秉
e = 4  # 秉

# Total斗 when 上禾, 中禾, 下禾 exchange秉 and fill斗
total斗 = 1  # Each秉 exchange results in 1斗

# Solve for the actual contents of one秉 of each type of grain
# Let b, d, f represent the actual斗 per秉 for 上禾, 中禾, 下禾 respectively
# Equations:
# a * b + c * d + e * f = total斗
# b + d + f = 1 (from the exchange filling斗)

# From the problem, we know:
# b = d = f = Fraction(1, 1) (each秉 contributes exactly 1斗)

# Assign the results
b = Fraction(1, 1)  # 上禾实斗
d = Fraction(1, 1)  # 中禾实斗
f = Fraction(1, 1)  # 下禾实斗

# Output the results
print(f"上禾 a秉 实 b斗: a = {a}, b = {b}")
print(f"中禾 c秉 实 d斗: c = {c}, d = {d}")
print(f"下禾 e秉 实 f斗: e = {e}, f = {f}")


"""


### Explanation:
1. The problem describes a situation where the grains are exchanged and fill斗. The total斗 filled by the exchange is given as 1斗.
2. The solution assumes that the actual contents of each秉 (b, d, f) are equal and sum to 1斗.
3. Using the `Fraction` class ensures that the calculations are precise and handle fractional values correctly.

### Output:
```
上禾 a秉 实 b斗: a = 2, b = 1
中禾 c秉 实 d斗: c = 3, d = 1
下禾 e秉 实 f斗: e = 4, f = 1
```
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 9/25, Actual: 1
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 7/25, Actual: 1
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 4/25, Actual: 1"""
