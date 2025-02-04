"""
今有田一畞計稅穀三升問一步合計幾何
術曰置穀三升再上十之為三百勺以二百四十步為法除之即得
答曰一步 a勺
"""

"""
Suppose there is one mu of field, and the tax is 3 sheng of grain.
Question: how much grain corresponds to one bu of the field?

The procedure says: Place the 3 sheng of grain, multiply it by 10, obtaining 300 zhu.
Use 240 bu as the divisor, divide it, and obtain the result.

Answer: one bu corresponds to *a* zhu.
"""

# 穀三升
穀 = 3

# 再上十之，為三百勺
穀勺 = 穀 * 10 * 10  # 1 sheng = 10 ge, 1 ge = 10 zhu, so 1 sheng = 100 zhu
穀勺 = 300

# 以二百四十步為法
法 = 240

# 除之，即得
a = Fraction(穀勺, 法)
"""
"""
