"""
今有地收穀一千二百六十三斛九斗六升七合三勺斛别加二升耗問正耗共計幾何
術曰置穀以隔位加二即得
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there is land that yields 1263 hu, 9 dou, 6 sheng, 7 ge, and 3 shao of grain.
For every hu, an additional 2 sheng of wastage is added.
Question: what is the total wastage?

The procedure says: Place the grain yield, and for each positional unit, add 2 [sheng] to it. This gives the total.

Answer: *a* hu.
"""

from fractions import Fraction

# Initial grain yield in various units
穀_斛 = 1263
穀_斗 = 9
穀_升 = 6
穀_合 = 7
穀_勺 = 3

# Conversion factors
斗_to_斛 = 10
升_to_斗 = 10
合_to_升 = 10
勺_to_合 = 10

# Convert all units to hu
穀_total_斛 = (
    穀_斛
    + 穀_斗 / 斗_to_斛
    + 穀_升 / (斗_to_斛 * 升_to_斗)
    + 穀_合 / (斗_to_斛 * 升_to_斗 * 合_to_升)
    + 穀_勺 / (斗_to_斛 * 升_to_斗 * 合_to_升 * 勺_to_合)
)

# Wastage: 2 sheng per hu
耗_per_斛 = 2 / (斗_to_斛 * 升_to_斗)

# Total wastage
正耗 = 穀_total_斛 * 耗_per_斛

# Total grain yield including wastage
a = 穀_total_斛 + 正耗#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 644623323/500000, Actual: 1289.246646"""
