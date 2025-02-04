"""
今有地收穀一千二百六十三斛九斗六升七合三勺斛别加二升耗問正耗共計幾何
術曰置穀以隔位加二即得
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there is a harvest of grain totaling 1263 hu, 9 dou, 6 sheng, 7 ge, and 3 shao. 
For each hu, an additional 2 sheng is added as wastage.
Question: what is the total wastage?

The procedure says: Place the grain, and for each positional unit, add 2 [sheng]. This gives the result.

Answer: the total wastage is *a* hu.
"""

from fractions import Fraction

# Initial grain harvest
穀_斛 = 1263
穀_斗 = 9
穀_升 = 6
穀_合 = 7
穀_勺 = 3

# Conversion factors
一斛 = 10  # 1 斛 = 10 斗
一斗 = 10  # 1 斗 = 10 升
一升 = 10  # 1 升 = 10 合
一合 = 10  # 1 合 = 10 勺

# Convert everything to sheng (升) for easier calculation
穀_總升 = (
    穀_斛 * 一斛 * 一斗 +
    穀_斗 * 一斗 +
    穀_升 +
    穀_合 / 一合 +
    穀_勺 / (一合 * 一升)
)

# Wastage: 2 sheng per hu
耗_升 = 穀_斛 * 2

# Add wastage to the total grain
總耗_升 = 穀_總升 + 耗_升

# Convert back to hu, dou, sheng, etc.
a_斛 = int(總耗_升 // (一斛 * 一斗))
剩餘升 = 總耗_升 % (一斛 * 一斗)

a_斗 = int(剩餘升 // 一斗)
剩餘升 %= 一斗

a_升 = int(剩餘升)
剩餘升 -= a_升

a_合 = int(剩餘升 * 一合)
剩餘升 -= a_合 / 一合

a_勺 = int(剩餘升 * 一合 * 一升)

a = Fraction(a_斛)  # Final result in hu
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 644623323/500000, Actual: 1289"""
