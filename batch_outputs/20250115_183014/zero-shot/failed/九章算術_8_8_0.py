"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the weights of a sparrow ("雀") and a swallow ("燕") in "兩" (liang), where 1斤 = 16兩.

We are given:
1. The weight of one sparrow plus one swallow equals 1斤 (16兩).
2. The weight of five sparrows equals the weight of six swallows.

We will solve for the weights of a sparrow (`a`) and a swallow (`b`) using these equations.

Here is the Python code:


"""


from fractions import Fraction

# Define the equations:
# 1. a + b = 16 (1斤 = 16兩)
# 2. 5a = 6b

# Solve for a and b
# From equation (1): b = 16 - a
# Substitute into equation (2): 5a = 6(16 - a)

# Simplify equation (2):
# 5a = 96 - 6a
# 11a = 96
a = Fraction(96, 11)  # Weight of one sparrow in 兩

# Substitute a into equation (1) to find b:
b = 16 - a  # Weight of one swallow in 兩

# Results
a  # Weight of one sparrow in 兩
b  # Weight of one swallow in 兩


"""


### Explanation of the solution:
1. The first equation is derived from the total weight of one sparrow and one swallow being 1斤 (16兩).
2. The second equation comes from the fact that the weight of five sparrows equals the weight of six swallows.
3. We solve these equations algebraically to find the weights of a sparrow (`a`) and a swallow (`b`).

### Final Answer:
- The weight of one sparrow (`a`) is \( \frac{96}{11} \) 兩.
- The weight of one swallow (`b`) is \( 16 - \frac{96}{11} = \frac{80}{11} \) 兩.
"""


"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 96/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 80/11"""
