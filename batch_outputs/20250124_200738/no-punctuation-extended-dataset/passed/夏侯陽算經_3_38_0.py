"""
今有麻三千四百七十五斛四斗五升毎三斛三斗作油一斛問油幾何
術曰以三斛三斗除得油數不盡約之為命分
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there are 3475 hu, 4 dou, and 5 sheng of sesame. 
For every 3 hu and 3 dou, 1 hu of oil is produced.
Question: how much oil is obtained?

The procedure says: Divide by 3 hu and 3 dou to obtain the amount of oil. 
If there is a remainder, reduce it to a fractional part.

Answer: *a* hu.
"""

from fractions import Fraction

# 麻三千四百七十五斛四斗五升
麻_斛 = 3475
麻_斗 = 4
麻_升 = 5

# Convert everything to sheng (1 hu = 10 dou, 1 dou = 10 sheng)
麻_升_total = 麻_斛 * 100 + 麻_斗 * 10 + 麻_升

# 每三斛三斗作油一斛
# Convert 3 hu and 3 dou to sheng
油率_升 = 3 * 100 + 3 * 10  # 3 hu = 300 sheng, 3 dou = 30 sheng

# 以三斛三斗除得油數
油數 = Fraction(麻_升_total, 油率_升)

# 答曰 a斛
a = 油數#----- content ends here -----

"""
"""
