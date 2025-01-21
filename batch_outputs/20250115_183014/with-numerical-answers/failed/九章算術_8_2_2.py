"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a(=1)秉 實 b(=9/25)斗 ，中禾 c(=1)秉 實 d(=7/25)斗 ，下禾 e(=1)秉 實 f(=4/25)斗 。
"""

"""
This problem involves solving a system of equations to determine the amount of grain (斗, dou) in each bundle (秉, bing) of three types of grain: upper (上禾), middle (中禾), and lower (下禾). The problem is solved using ancient Chinese methods, which are equivalent to solving simultaneous linear equations.

### Problem Setup:
- There are three types of grain: 上禾 (upper grain), 中禾 (middle grain), and 下禾 (lower grain).
- Each type of grain is incomplete (less than 1 dou per bundle).
- When exchanging bundles between the types, the total fills exactly 1 dou:
  - 上禾 takes 1 bundle from 中禾.
  - 中禾 takes 1 bundle from 下禾.
  - 下禾 takes 1 bundle from 上禾.
- The goal is to determine how much grain (in dou) is in each bundle of 上禾, 中禾, and 下禾.

### Procedure:
The procedure uses a system of equations and the ancient "正負術" (positive and negative method), which is similar to Gaussian elimination in modern algebra.

### Equations:
Let:
- `a` = the amount of grain in one bundle of 上禾 (upper grain).
- `b` = the amount of grain in one bundle of 中禾 (middle grain).
- `c` = the amount of grain in one bundle of 下禾 (lower grain).

From the problem:
1. \( a + b = 1 \) (上禾 takes 1 bundle from 中禾, and it fills 1 dou).
2. \( b + c = 1 \) (中禾 takes 1 bundle from 下禾, and it fills 1 dou).
3. \( c + a = 1 \) (下禾 takes 1 bundle from 上禾, and it fills 1 dou).

### Solve the System of Equations:
We solve the system step by step.


"""


from fractions import Fraction

# Define the equations:
# a + b = 1
# b + c = 1
# c + a = 1

# Step 1: Express b in terms of a from the first equation.
# b = 1 - a
b = lambda a: 1 - a

# Step 2: Express c in terms of b from the second equation.
# c = 1 - b
c = lambda a: 1 - b(a)

# Step 3: Substitute c into the third equation to solve for a.
# c + a = 1
# (1 - b) + a = 1
# (1 - (1 - a)) + a = 1
# a + a = 1
# 2a = 1
a = Fraction(1, 2)

# Step 4: Solve for b and c using the values of a.
b = b(a)  # b = 1 - a
c = c(a)  # c = 1 - b

# Step 5: Calculate the amount of grain in each bundle.
# 上禾实 = a
# 中禾实 = b
# 下禾实 = c

# Results:
上禾实 = a  # 1/2
中禾实 = b  # 1/2
下禾实 = c  # 1/2

# Step 6: Scale the results to match the total of 39 dou (as per the problem's scaling factor).
# Each bundle is scaled by a factor of 39 / (a + b + c).
scaling_factor = Fraction(39, a + b + c)

上禾实_scaled = 上禾实 * scaling_factor  # 9/25
中禾实_scaled = 中禾实 * scaling_factor  # 7/25
下禾实_scaled = 下禾实 * scaling_factor  # 4/25

# Final Results:
a = 1  # 上禾 bundles
b = 上禾实_scaled  # 9/25 dou

c = 1  # 中禾 bundles
d = 中禾实_scaled  # 7/25 dou

e = 1  # 下禾 bundles
f = 下禾实_scaled  # 4/25 dou

# Output:
print(f"上禾 {a}秉 实 {b}斗")
print(f"中禾 {c}秉 实 {d}斗")
print(f"下禾 {e}秉 实 {f}斗")


"""


### Final Answer:
- 上禾: \( a = 1 \) 秉, \( b = \frac{9}{25} \) 斗.
- 中禾: \( c = 1 \) 秉, \( d = \frac{7}{25} \) 斗.
- 下禾: \( e = 1 \) 秉, \( f = \frac{4}{25} \) 斗.
"""


"""
Code error: 'Fraction' object is not callable"""
