"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
To solve the problem, we need to translate the ancient Chinese math problem into Python code. The problem states that the combined weight of five sparrows (雀) and six swallows (燕) is one jin (16 liang). Additionally, the weight of one sparrow equals the weight of one swallow when balanced on a scale.

We will use the following variables:
- `a`: weight of one sparrow in liang
- `b`: weight of one swallow in liang

The equations derived from the problem are:
1. \( 5a + 6b = 16 \) (total weight is 1 jin or 16 liang)
2. \( a = b \) (one sparrow balances one swallow)

Let's solve this using Python:


"""

#----- content starts here -----

from fractions import Fraction

# Equation 1: 5a + 6b = 16
# Equation 2: a = b

# Substituting a = b into Equation 1
# 5a + 6a = 16
# 11a = 16
# a = 16 / 11

a = Fraction(16, 11)  # Weight of one sparrow in liang
b = a  # Weight of one swallow in liang

# Results
a, b
#----- content ends here -----


"""


This code computes the weights of one sparrow (`a`) and one swallow (`b`) in liang. The solution is:

- \( a = \frac{16}{11} \) liang
- \( b = \frac{16}{11} \) liang
"""


"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
