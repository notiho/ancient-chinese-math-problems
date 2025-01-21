"""
今有田一畞計稅穀三升問一步合計幾何
術曰置穀三升再上十之為三百勺以二百四十步為法除之即得
答曰 a步 b勺
"""

"""
Suppose there is 1 mu of field, and the tax is calculated as 3 sheng of grain.
Question: how much grain corresponds to one bu?

The procedure says: Place the 3 sheng of grain, multiply it by 10, giving 300 zhuo.
Take 240 bu as the divisor and divide it, obtaining the result.

Answer: *a* bu and *b* zhuo.
"""

from fractions import Fraction

# 穀三升
穀 = 3

# 再上十之，為三百勺
穀勺 = 穀 * 10 * 10  # 1 sheng = 10 ge, 1 ge = 10 zhuo, so 1 sheng = 100 zhuo

# 以二百四十步為法
法 = 240

# 除之，即得
每步穀 = Fraction(穀勺, 法)

# 分離整步與餘勺
a = 每步穀 // 10  # 整數部分為步數 (1 bu = 10 zhuo)
b = 每步穀 % 10  # 餘數部分為勺數
"""
Variable 'a' has wrong value. Expected: 1, Actual: 0"""
