"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：雀重 a(=32/19)兩 ，燕重 b(=24/19)兩 。
"""

#----- content starts here -----
"""
Suppose there are 5 sparrows and 6 swallows. When placed on a balance, the sparrows are all equally heavy, and the swallows are all equally light.
When one sparrow and one swallow are exchanged, the balance is perfectly level.
The combined weight of all the sparrows and swallows is 1 jin.
Question: how much does one sparrow and one swallow weigh respectively?

The procedure says: Treat this as a system of equations. Solve by balancing the weights. Each weighs 8 liang.

The answer says: A sparrow weighs *a*(=32/19) liang, and a swallow weighs *b*(=24/19) liang.
"""

# Define the total weight in jin (1 jin = 16 liang)
總重 = 16  # in liang

# Define the number of sparrows and swallows
雀數 = 5
燕數 = 6

# Let the weight of one sparrow be x liang and one swallow be y liang
# Equation 1: 5x + 6y = 16
# Equation 2: x - y = 0 (from the balance condition when one sparrow and one swallow are exchanged)

# Solve for x and y
# From Equation 2: x = y + (x - y) = y + (1/19)
# Substitute x into Equation 1:
##----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
