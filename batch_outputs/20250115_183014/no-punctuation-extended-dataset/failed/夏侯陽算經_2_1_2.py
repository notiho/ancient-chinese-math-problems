"""
今有田一畞計稅穀三升問一步合計幾何
術曰置穀三升再上十之為三百勺以二百四十步為法除之即得
答曰 a步 b勺
"""

"""
Suppose there is 1 mu of land, and the tax grain is 3 sheng.
Question: how much grain corresponds to one bu?

The procedure says: Place the grain, 3 sheng, and multiply it by 10, giving 300 zhao.
Take 240 bu as the divisor and divide it, obtaining the result.

Answer: *a* bu and *b* zhao.
"""

from fractions import Fraction

# 穀三升
穀 = 3

# 再上十之，為三百勺
穀勺 = 穀 * 10 * 10  # 1 sheng = 10 ge, 1 ge = 10 zhao, so 1 sheng = 100 zhao

# 以二百四十步為法
法 = 240

# 除之，即得
每步穀 = Fraction(穀勺, 法)

# 分解為步和勺
a = 每步穀 // 10  # 每步穀的整數部分為步 (1步 = 10勺)
b = 每步穀 % 10   # 每步穀的餘數部分為勺

a = int(a)
b = int(b)


"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'b' has wrong value. Expected: 5/4, Actual: 1"""
