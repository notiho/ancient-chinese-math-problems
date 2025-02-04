"""
今有糙米三千四百六十四斛五斗七升三合四勺毎斗舂得熟米九升問熟米幾何
術曰先置米數九因退之即得
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there are 3464 hu, 5 dou, 7 sheng, 3 ge, and 4 shao of coarse rice.
For every dou, 9 sheng of cooked rice are obtained after pounding.
Question: how much cooked rice is obtained?

The procedure says: First, place the amount of rice. Multiply it by 9 and divide by 10 to convert coarse rice into cooked rice.

Answer: *a* hu.
"""

from fractions import Fraction

# 糙米數
糙米_斛 = 3464
糙米_斗 = 5
糙米_升 = 7
糙米_合 = 3
糙米_勺 = 4

# Convert everything to sheng (1 hu = 10 dou, 1 dou = 10 sheng, 1 sheng = 10 ge, 1 ge = 10 shao)
糙米_升總 = (
    (糙米_斛 * 10 * 10) +  # Convert hu to sheng
    (糙米_斗 * 10) +       # Convert dou to sheng
    糙米_升 +               # Add sheng
    Fraction(糙米_合, 10) + # Convert ge to sheng
    Fraction(糙米_勺, 100)  # Convert shao to sheng
)

# 每斗舂得熟米九升 (1 dou = 10 sheng, so 9/10 of the coarse rice becomes cooked rice)
熟米_升總 = 糙米_升總 * Fraction(9, 10)

# Convert cooked rice back to hu (1 hu = 10 dou, 1 dou = 10 sheng)
熟米_斛 = 熟米_升總 / (10 * 10)

a = 熟米_斛#----- content ends here -----

"""
"""
