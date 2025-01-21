"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
To solve the problem, we will translate the ancient Chinese mathematical description into Python code. The problem involves determining the weights of a sparrow ("雀") and a swallow ("燕") in units of "兩" (liang), where 16 liang = 1 jin (斤). The problem states that the total weight of 5 sparrows and 6 swallows is 1 jin (16 liang), and the weight of one sparrow equals the weight of one swallow when exchanged on a balance.

Here is the Python code:


"""


from fractions import Fraction

# Let the weight of a sparrow be "a" liang and the weight of a swallow be "b" liang.
# According to the problem:
# 1. 5a + 6b = 16 (total weight is 1 jin = 16 liang)
# 2. a = b (balance condition when one sparrow is exchanged for one swallow)

# From the second equation, substitute a = b into the first equation:
# 5a + 6a = 16
# 11a = 16
a = Fraction(16, 11)  # Weight of a sparrow in liang
b = a  # Weight of a swallow in liang (since a = b)

# The weights are:
# a = 16/11 liang
# b = 16/11 liang


"""


### Explanation:
1. The first equation comes from the total weight of 5 sparrows and 6 swallows being 1 jin (16 liang): \( 5a + 6b = 16 \).
2. The second equation comes from the balance condition: \( a = b \).
3. Substituting \( a = b \) into the first equation gives \( 11a = 16 \), solving for \( a \) yields \( a = \frac{16}{11} \).
4. Since \( a = b \), the weight of a swallow is also \( b = \frac{16}{11} \).

### Final Answer:
- The weight of a sparrow \( a \) is \( \frac{16}{11} \) liang.
- The weight of a swallow \( b \) is \( \frac{16}{11} \) liang.
"""


"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
