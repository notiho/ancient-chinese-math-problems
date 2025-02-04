"""
今有地收穀一千二百六十三斛九斗六升七合三勺斛别加二升耗問正耗共計幾何
術曰置穀以隔位加二即得
答曰 a斛
"""

"""
Suppose there is land that yields 1263 hu, 9 dou, 6 sheng, 7 ge, and 3 shao of grain.
Additionally, 2 sheng of wastage is added to each hu.
Question: what is the total wastage?

The procedure says: Place the grain yield, and for each unit of hu, add 2 sheng to the corresponding position. This gives the total.

Answer: the total wastage is *a* hu.
"""

from fractions import Fraction

# Initial grain yield in various units
穀_斛 = 1263
穀_斗 = 9
穀_升 = 6
穀_合 = 7
穀_勺 = 3

# Conversion factors between units
一斛 = 10  # 1 hu = 10 dou
一斗 = 10  # 1 dou = 10 sheng
一升 = 10  # 1 sheng = 10 ge
一合 = 10  # 1 ge = 10 shao

# Convert everything to sheng for easier calculation
穀_總升 = (
    穀_斛 * 一斛 * 一斗 +
    穀_斗 * 一斗 +
    穀_升 +
    穀_合 / 一合 +
    穀_勺 / (一合 * 一升)
)

# Add 2 sheng of wastage per hu
耗_總升 = 穀_斛 * 2

# Total grain yield including wastage in sheng
總升 = 穀_總升 + 耗_總升

# Convert back to hu
a = Fraction(總升, 一斛 * 一斗)  # Convert total sheng to hu
"""
Code error: both arguments should be Rational instances"""
