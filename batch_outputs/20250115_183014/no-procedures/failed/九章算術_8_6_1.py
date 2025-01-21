"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
Suppose there are 5 cows and 2 sheep worth a total of 10 liang of gold.
Additionally, 2 cows and 5 sheep are worth a total of 8 liang of gold.
Question: how much is each cow and each sheep worth?

Answer: Each cow is worth *a* gold liang, and each sheep is worth *b* gold liang.
"""

# Let the price of a cow be x and the price of a sheep be y
# We have the following equations:
# 5x + 2y = 10
# 2x + 5y = 8

from fractions import Fraction

# Solve the system of equations using substitution or elimination
# Multiply the first equation by 2 and the second equation by 5 to eliminate x
# 10x + 4y = 20
# 10x + 25y = 40

# Subtract the first equation from the second
# 21y = 20 - 40 = 20
y = Fraction(20, 21)

# Substitute y back into the first equation to solve for x
# 5x + 2(Fraction(20,21)) = 10
#
"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'"""
