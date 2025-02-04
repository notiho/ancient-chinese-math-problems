"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that the total weight of five sparrows (雀) and six swallows (燕) is one jin (斤), and that one sparrow and one swallow balance each other on a scale. We need to find the weight of one sparrow (`a` 两) and one swallow (`b` 两).

We will use the `Fraction` class to handle the calculations.


"""


from fractions import Fraction

# Total weight of 5 sparrows and 6 swallows is 1 jin (16 两 per jin)
total_weight = Fraction(16)  # in 两

# Weight of 1 sparrow = a 两, weight of 1 swallow = b 两
# Equation 1: 5a + 6b = 16
# Equation 2: a = b (from the balance condition)

# Solving the equations
# From Equation 2: a = b
# Substitute a = b into Equation 1: 5a + 6a = 16
# Simplify: 11a = 16
a = total_weight / 11  # a = 16 / 11 两
b = a  # b = a

# Results
print(f"Weight of one sparrow (a): {a} 两")
print(f"Weight of one swallow (b): {b} 两")


"""


### Explanation:
1. The total weight of 5 sparrows and 6 swallows is given as 1 jin, which is equivalent to 16 两.
2. The balance condition states that one sparrow and one swallow weigh the same, so `a = b`.
3. Substituting `a = b` into the total weight equation `5a + 6b = 16`, we get `11a = 16`.
4. Solving for `a`, we find `a = 16 / 11`.
5. Since `a = b`, the weight of one swallow is also `16 / 11`.

### Output:
```
Weight of one sparrow (a): 16/11 两
Weight of one swallow (b): 16/11 两
```
"""


"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
