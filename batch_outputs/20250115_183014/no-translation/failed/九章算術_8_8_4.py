"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
To solve this problem, we will use the given procedure to determine the weights of the sparrow (雀) and the swallow (燕). The problem is essentially a system of linear equations, and we will follow the ancient Chinese method described in the "方程術" to solve it.

### Problem Setup:
1. Let the weight of one sparrow (雀) be \( x \) (in 兩).
2. Let the weight of one swallow (燕) be \( y \) (in 兩).
3. The total weight of 5 sparrows and 6 swallows is 1斤 = 16兩:
   \[
   5x + 6y = 16
   \]
4. The weight of one sparrow and one swallow together balances the scale:
   \[
   x = y
   \]

We will now solve this system of equations using the described procedure.

---


"""


from fractions import Fraction

# Step 1: Define the equations
# Equation 1: 5x + 6y = 16
# Equation 2: x = y

# Step 2: Substitute x = y into Equation 1
# 5x + 6x = 16
# 11x = 16
x = Fraction(16, 11)  # Weight of one sparrow (雀)

# Step 3: Since x = y, the weight of one swallow (燕) is also:
y = x  # Weight of one swallow (燕)

# Final Answer
a = x  # Weight of one sparrow in 兩
b = y  # Weight of one swallow in 兩


"""


### Answer:
- 雀重 \( a = \frac{16}{11} \) 兩
- 燕重 \( b = \frac{16}{11} \) 兩
"""


"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
