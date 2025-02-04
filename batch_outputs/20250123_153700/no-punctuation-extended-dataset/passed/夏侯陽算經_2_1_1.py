"""
今有田一畞計稅穀三升問一步合計幾何
術曰置穀三升再上十之為三百勺以二百四十步為法除之即得
答曰一步 a勺
"""

"""
Suppose there is 1 mu of land, which is taxed 3 sheng of grain.
Question: how much grain corresponds to one bu of land?

The procedure says: Place the grain, 3 sheng. Multiply it by 10, giving 300 zhuo.
Take 240 bu as the divisor. Divide it, and the result is obtained.

Answer: one bu corresponds to *a* zhuo.
"""

# 穀三升
穀 = 3

# 再上十之，為三百勺
穀勺 = 10 * 10 * 穀

# 以二百四十步為法
法 = 240

# 除之，即得
a = Fraction(穀勺, 法)
"""
"""
