"""
今有米一千五百七十七斛，斛别加八斗三升。問：計㡬何？
術曰：列米一千五百七十七斛，以加米一斛八斗三升乘之即得。
答曰： a斛 。
"""


# 米一千五百七十七斛
米 = 1577

# 加米一斛八斗三升
# 1斛 = 10斗, 1斗 = 10升
加米 = 1 + Fraction(8, 10) + Fraction(3, 100)

# 以加米一斛八斗三升乘之即得
a = 米 * 加米
"""
"""
