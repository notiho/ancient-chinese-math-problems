"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the weights of a sparrow ("雀") and a swallow ("燕") in units of "兩" (liang). The given conditions are:

1. A sparrow and a swallow balance each other on a scale.
2. The combined weight of all sparrows and swallows is 1 jin (16 liang).

We will use the `Fraction` class to ensure precise calculations.

Here is the Python code:


"""


from fractions import Fraction

# Let the weight of a sparrow be "a" liang and the weight of a swallow be "b" liang.
# Condition 1: a + b = 16 (since 1 jin = 16 liang)
# Condition 2: a = b (since they balance each other on the scale)

# Solving the equations:
a = Fraction(16, 2)  # Weight of a sparrow in liang
b = Fraction(16, 2)  # Weight of a swallow in liang

# Results:
# a = 8 liang
# b = 8 liang


"""


### Explanation:
- The first condition states that the total weight of all sparrows and swallows is 16 liang.
- The second condition states that the weight of a sparrow equals the weight of a swallow.
- Solving these equations gives `a = 8` liang and `b = 8` liang.

Thus, the solution is:
- Sparrow weight (`a`): 8 liang
- Swallow weight (`b`): 8 liang
"""


"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 8
Variable 'b' has wrong value. Expected: 24/19, Actual: 8"""
