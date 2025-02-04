"""
今有地收穀一千二百六十三斛九斗六升七合三勺斛别加二升耗問正耗共計幾何
術曰置穀以隔位加二即得
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there is a harvest of 1263 hu, 9 dou, 6 sheng, 7 ge, and 3 shao of grain. 
For each hu, an additional 2 sheng is considered as wastage.
Question: what is the total wastage?

The procedure says: Place the grain harvest, and for each positional unit (hu), add 2 [sheng]. This gives the total wastage.

Answer: *a* hu.
"""

from fractions import Fraction

# Initial grain harvest
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
穀_in_斛 = (
    穀_斛
    + Fraction(穀_斗, 斗_to_斛)
    + Fraction(穀_升, 斗_to_斛 * 升_to_斗)
    + Fraction(穀_合, 斗_to_斛 * 升_to_斗 * 合_to_升)
    + Fraction(穀_勺, 斗_to_斛 * 升_to_斗 * 合_to_升 * 勺_to_合)
)

# Add 2 sheng wastage per hu
耗_in_升 = 2 * 穀_斛  # Only the hu contributes to wastage
耗_in_斛 = Fraction(耗_in_升, 升_to_斗 * 斗_to_斛)

# Total wastage
a = 耗_in_斛
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 644623323/500000, Actual: 1263/50"""
