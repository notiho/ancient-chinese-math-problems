"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
This is a classic problem involving a system of linear equations. Let's break it down and solve it step by step using Python.

### Problem Breakdown:
1. There are 5 sparrows (雀) and 6 swallows (燕). Sparrows all weigh the same, and swallows all weigh the same.
2. When one sparrow and one swallow are placed on opposite sides of a balance, the balance is level.
3. The total weight of all the sparrows and swallows together is 1 jin (16 liang).
4. We need to find the weight of one sparrow and one swallow.

### Mathematical Representation:
Let:
- \( x \) = weight of one sparrow (in liang),
- \( y \) = weight of one swallow (in liang).

From the problem, we have the following equations:
1. \( x = y \) (since one sparrow balances one swallow).
2. \( 5x + 6y = 16 \) (total weight of 5 sparrows and 6 swallows is 1 jin = 16 liang).

Substituting \( x = y \) into the second equation:
\[
5x + 6x = 16 \implies 11x = 16 \implies x = \frac{16}{11}, \, y = \frac{16}{11}.
\]

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Define the total weight in liang
total_weight = 16  # 1 jin = 16 liang

# Solve for the weight of one sparrow (x) and one swallow (y)
sparrow_weight = Fraction(total_weight, 11)  # x = 16 / 11
swallow_weight = Fraction(total_weight, 11)  # y = 16 / 11

# Output the results
a = sparrow_weight
b = swallow_weight

print(f"雀重 {a} 兩，燕重 {b} 兩。")
#----- content ends here -----


"""


### Explanation of the Code:
1. We use the `Fraction` class to ensure exact arithmetic with fractions.
2. The total weight of 16 liang is divided by 11 (since \( 11x = 16 \)) to find the weight of one sparrow and one swallow.
3. The result is printed in terms of liang.

### Answer:
The weight of one sparrow is \( a = \frac{16}{11} \) liang, and the weight of one swallow is \( b = \frac{16}{11} \) liang.
"""


"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
