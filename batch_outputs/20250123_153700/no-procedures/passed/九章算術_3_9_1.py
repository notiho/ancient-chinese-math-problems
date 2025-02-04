"""
今有絲一斤，價直二百四十。今有錢一千三百二十八，問︰得絲幾何？
荅曰： a斤 。
"""

"""
Suppose there is 1 jin of silk, priced at 240 coins. Now, there are 1328 coins.
Question: how much silk can be obtained?

Answer: *a* jin.
"""

# 絲一斤價直二百四十
絲價 = 240

# 錢一千三百二十八
錢 = 1328

# Divide the total money by the price per jin to calculate the amount of silk
a = Fraction(錢, 絲價)
"""
"""
