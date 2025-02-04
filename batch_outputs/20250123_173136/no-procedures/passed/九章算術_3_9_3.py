"""
今有絲一斤，價直二百四十。今有錢一千三百二十八，問︰得絲幾何？
荅曰： a斤 。
"""

"""
Suppose there is 1 jin of silk, priced at 240 qian. Now, there are 1328 qian available.
Question: how much silk can be obtained?

Answer: *a* jin.
"""

# 絲一斤價直二百四十
絲價 = 240  # qian per jin

# 錢一千三百二十八
錢 = 1328  # total qian available

# Calculate the amount of silk that can be obtained
a = Fraction(錢, 絲價)  # in jin

a
"""
"""
