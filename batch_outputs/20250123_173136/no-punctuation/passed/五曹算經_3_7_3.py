"""
今有米一千五百七十七斛斛别加八斗三升問計㡬何
術曰列米一千五百七十七斛以加米一斛八斗三升乘之即得
答曰 a斛 
"""

"""
Suppose there are 1577 hu of rice, and for each hu, an additional 8 dou and 3 sheng are added.
Question: what is the total amount?

The procedure says: Place the 1577 hu of rice.
For each hu, multiply by the additional rice of 1 hu, 8 dou, and 3 sheng.
This gives the total.

Answer: *a* hu.
"""

# 米一千五百七十七斛
米 = 1577

# 一斛等於10斗，一斗等於10升
一斛 = 10 * 10  # 1 hu = 100 sheng
一斗 = 10  # 1 dou = 10 sheng

# 加米一斛八斗三升
加米 = 一斛 + 8 * 一斗 + 3  # Convert to sheng

# 乘之即得
總米 = 米 * 加米  # Total in sheng

# 將總米轉換回斛
a = Fraction(總米, 一斛)  # Convert back to hu
"""
"""
