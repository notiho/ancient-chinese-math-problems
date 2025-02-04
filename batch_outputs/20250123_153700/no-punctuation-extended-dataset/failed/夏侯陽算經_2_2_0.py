"""
今有地收穀一千二百六十三斛九斗六升七合三勺斛别加二升耗問正耗共計幾何
術曰置穀以隔位加二即得
答曰 a斛
"""

"""
Suppose there is land that yields 1263 hu, 9 dou, 6 sheng, 7 ge, and 3 shao of grain.
Additionally, 2 sheng of wastage is added to the hu separately.
Question: what is the total corrected wastage?

The procedure says: Place the grain yield, and add 2 [sheng] to the hu by shifting positions, then the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# Initial grain yield in various units
穀_斛 = 1263
穀_斗 = 9
穀_升 = 6
穀_合 = 7
穀_勺 = 3

# Convert all units to hu (1 hu = 10 dou, 1 dou = 10 sheng, 1 sheng = 10 ge, 1 ge = 10 shao)
穀 = (
    穀_斛
    + Fraction(穀_斗, 10)
    + Fraction(穀_升, 100)
    + Fraction(穀_合, 1000)
    + Fraction(穀_勺, 10000)
)

# Add 2 sheng to the hu (2 sheng = 2/100 hu)
耗 = Fraction(2, 100)

# Total corrected wastage
a = 穀 + 耗
"""
Variable 'a' has wrong value. Expected: 644623323/500000, Actual: 12639873/10000"""
