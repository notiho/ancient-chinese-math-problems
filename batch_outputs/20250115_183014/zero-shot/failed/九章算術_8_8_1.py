"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
To solve this problem, we need to translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given:
# 1. One sparrow (雀) and one swallow (燕) balance the scale.
# 2. The combined weight of all sparrows and swallows is 1斤 (16兩).

# Let the weight of one sparrow be "a" (in 兩) and the weight of one swallow be "b" (in 兩).
# There are 5 sparrows and 6 swallows.

# Equation 1: a + b = 16 / (5 + 6)
# Equation 2: a = b

# Solve for a and b
a = Fraction(16, 11)
b = a

# Output the results
a, b


"""


### Explanation:
1. The problem states that the combined weight of 5 sparrows and 6 swallows is 1斤 (16兩). This gives the equation:
   \[
   5a + 6b = 16
   \]
2. It also states that one sparrow and one swallow balance the scale, implying:
   \[
   a = b
   \]
3. Substituting \( a = b \) into the first equation:
   \[
   5a + 6a = 16 \implies 11a = 16 \implies a = \frac{16}{11}
   \]
4. Since \( a = b \), the weight of one sparrow and one swallow is both \( \frac{16}{11} \)兩.

### Final Answer:
- \( a = \frac{16}{11} \)兩 (weight of one sparrow)
- \( b = \frac{16}{11} \)兩 (weight of one swallow)
"""


"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
