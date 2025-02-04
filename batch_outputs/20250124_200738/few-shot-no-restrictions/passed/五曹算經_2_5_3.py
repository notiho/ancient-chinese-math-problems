"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a疋 。
"""

#----- content starts here -----
"""
Suppose there are 1,362 soldiers, and each soldier is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

The procedure says: Place the 1,362 soldiers, and multiply by 28 chi and 5 cun (convert to chi first).
This gives the total number of chi.
Divide the total by 40 chi (1 bolt of silk = 40 chi), and the result is the number of bolts.

Answer: *a* bolts.
"""

from fractions import Fraction

# Constants for unit conversion
ZHANG_TO_CHI = 10  # 1 zhang = 10 chi
CHI_TO_CUN = 10    # 1 chi = 10 cun
BOLT_LENGTH = 40   # 1 bolt = 40 chi

# Number of soldiers
兵 = 1362

# Silk given to each soldier: 2 zhang, 8 chi, 5 cun
絹_per_soldier = (2 * ZHANG_TO_CHI) + 8 + Fraction(5, CHI_TO_CUN)  # Convert to chi

# Total silk in chi
總絹 = 兵 * 絹_per_soldier

# Convert total chi to bolts
a = Fraction(總絹, BOLT_LENGTH)

# Output the result
a#----- content ends here -----

"""
"""
