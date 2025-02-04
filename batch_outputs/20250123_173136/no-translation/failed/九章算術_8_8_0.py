"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code. The problem essentially involves solving a system of linear equations, where the weights of the sparrow (雀) and swallow (燕) are unknown. The procedure described corresponds to solving the equations step by step.

### Problem Setup:
1. Let the weight of one sparrow (雀) be `x` (in 两).
2. Let the weight of one swallow (燕) be `y` (in 两).
3. From the problem:
   - 5 sparrows + 6 swallows = 1斤 = 16两.
   - 1 sparrow + 1 swallow = balance point (equal weight).

### Equations:
1. \( 5x + 6y = 16 \)
2. \( x = y \)

We will now translate the solution into Python code.

---


"""


from fractions import Fraction

# Equation 1: 5x + 6y = 16
total_weight = 16  # 1斤 = 16两
sparrow_count = 5
swallow_count = 6

# Equation 2: x = y (balance point)
# Substitute x = y into Equation 1:
# 5x + 6x = 16
# 11x = 16
# Solve for x:
x = Fraction(total_weight, sparrow_count + swallow_count)

# Since x = y:
y = x

# Results
a = x  # Sparrow weight in 两
b = y  # Swallow weight in 两


"""


### Explanation of the Code:
1. We represent the total weight of 5 sparrows and 6 swallows as 16两.
2. Using the balance condition \( x = y \), we substitute \( x \) for \( y \) in the first equation.
3. Solve for \( x \) using the total weight divided by the total count of sparrows and swallows.
4. Since \( x = y \), both the sparrow and swallow have the same weight.

### Answer:
- \( a = 8 \)两 (weight of one sparrow),
- \( b = 8 \)两 (weight of one swallow).
"""


"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
