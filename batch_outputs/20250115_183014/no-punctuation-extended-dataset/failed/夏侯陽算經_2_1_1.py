"""
今有田一畞計稅穀三升問一步合計幾何
術曰置穀三升再上十之為三百勺以二百四十步為法除之即得
答曰 a步 b勺
"""

"""
Suppose there is a field of 1 mu, and the tax grain is 3 sheng.
Question: how much tax grain corresponds to one bu?

The procedure says: Place the grain of 3 sheng, multiply it by 10, obtaining 300 zhuo.
Take 240 bu as the divisor, divide it, and obtain the result.

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

# 分解為整步和餘勺
a = 每步穀 // 100  # 每步的整數部分（升）
b = 每步穀 % 100  # 每步的餘數部分（勺）
"""
Variable 'a' has wrong value. Expected: 1, Actual: 0"""
