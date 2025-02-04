"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the weights of a sparrow ("雀") and a swallow ("燕") in "兩" (liang), where 1斤 = 16兩.

We are given:
1. The weight of one sparrow plus one swallow equals 1斤 (16兩).
2. The weight of one sparrow equals the weight of one swallow when exchanged on a balance.

Let the weight of a sparrow be `a` (in 兩) and the weight of a swallow be `b` (in 兩). Using the given conditions, we can set up the equations:
1. \( a + b = 16 \)
2. \( a = b \)

We will solve these equations in Python.


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations
# a + b = 16
# a = b

# Solve for a and b
a = Fraction(16, 2)  # a = 16 / 2
b = Fraction(16, 2)  # b = 16 / 2

# The weights of the sparrow and swallow
a  # Weight of the sparrow in 兩
b  # Weight of the swallow in 兩
#----- content ends here -----


"""


The solution is:
- \( a = 8 \)兩 (weight of the sparrow)
- \( b = 8 \)兩 (weight of the swallow)
"""


"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 8
Variable 'b' has wrong value. Expected: 24/19, Actual: 8"""
