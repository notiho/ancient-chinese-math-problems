"""
今有田一畞計稅穀三升問一步合計幾何
術曰置穀三升再上十之為三百勺以二百四十步為法除之即得
答曰一步 a勺
"""

"""
Suppose there is a field of 1 mu, and the tax grain is 3 sheng.
Question: how much grain corresponds to one bu?

The procedure says: Place the grain as 3 sheng, then multiply it by 10, obtaining 300 zhu.
Take 240 bu as the divisor and divide it, obtaining the result.

Answer: one bu corresponds to *a* zhu.
"""

# 穀三升
穀 = 3

# 再上十之，為三百勺
穀勺 = 10 * 穀 * 10  # 1升 = 10勺

# 以二百四十步為法
法 = 240

# 除之，即得
a = Fraction(穀勺, 法)
"""
"""
