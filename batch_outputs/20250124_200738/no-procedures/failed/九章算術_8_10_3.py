"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
荅曰：馬價 a錢 ，牛價 b錢 。
"""

#----- content starts here -----
"""
Suppose the price of 2 horses and 1 cow exceeds 10,000 by the price of half a horse.
And the price of 1 horse and 2 cows is less than 10,000 by the price of half a cow.
Question: What are the prices of a horse and a cow?

Answer: The price of a horse is *a* qian, and the price of a cow is *b* qian.
"""

# Let the price of a horse be x (馬價)
# Let the price of a cow be y (牛價)

# Equations:
# 2x + y = 10000 + x/2
# x + 2y = 10000 - y/2

# Simplify the equations:
# (1) 4x + 2y = 20000 + x
# (2) 2x + 4y = 20000 - y

# Solve for x and y:
from fractions import Fraction

# From (1): 4x + 2y = 20000 + x
# 3x + 2y = 20000  --> y = (20000 - 3x) / 2
def solve():
#----- content ends here -----

"""
Code error: expected an indented block after function definition on line 26 (<string>, line 26)"""
