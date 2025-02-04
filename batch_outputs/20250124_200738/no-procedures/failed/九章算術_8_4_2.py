"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

#----- content starts here -----
"""
Suppose there are two types of grain, "upper grain" (上禾) and "lower grain" (下禾). The problem provides the following information:

1. Six bundles (秉) of upper grain lose 1 dou and 8 sheng (1斗8升) when processed, which is equivalent to 10 bundles of lower grain.
2. Fifteen bundles of lower grain lose 5 sheng (5升) when processed, which is equivalent to 5 bundles of upper grain.

Question: How much processed grain does one bundle of upper grain and one bundle of lower grain yield?

Answer: One bundle of upper grain yields *a* sheng, and one bundle of lower grain yields *b* sheng.
"""

from fractions import Fraction

# Information given in the problem
upper_grain_bundles_1 = 6  # 上禾 6 秉
upper_grain_loss_1 = 1 * 10 + 8  # 1斗8升 = 1*10 + 8 升
lower_grain_bundles_1 = 10  # 當下禾 10 秉

lower_grain_bundles_2 = 15  # 下禾 15 秉
lower_grain_loss_2 = 5  # 損實 5 升
upper_grain_bundles_2 = 5  # 當上禾 5 秉

# Let "a" be the processed grain from one bundle of upper grain (上禾一秉實 a升)
# Let "b" be the processed grain from one bundle of lower grain (下禾一秉實 b升)

# From the first condition:
# 6a = 10b + 1斗8升 = 10b + 18升
eq1 = 6 * Fraction(1, 1), 10 * Fraction(1, 1)#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
