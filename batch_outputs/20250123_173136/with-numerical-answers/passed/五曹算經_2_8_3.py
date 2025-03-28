"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
術曰：列米三千二百四十六斛八斗七升，以四百八十二文乘之即得。
答曰： a(=78249567/50000)貫 。
"""

"""
Suppose there is military grain, 3246 hu, 8 dou, and 7 sheng. Each hu is worth 482 wen.
Question: what is the total value?

The procedure says: Place the grain, 3246 hu, 8 dou, and 7 sheng. Multiply it by 482 wen to obtain the total.

Answer: *a*(=78249567/50000) guan.
"""

from fractions import Fraction

# 米三千二百四十六斛八斗七升
斛 = 3246
斗 = 8
升 = 7

# Convert all to 升 (1 斛 = 10 斗, 1 斗 = 10 升)
總升 = 斛 * 10 * 10 + 斗 * 10 + 升

# 每斛直錢四百八十二文
每斛價值 = 482

# Convert 每斛價值 to 每升價值 (1 斛 = 100 升)
每升價值 = Fraction(每斛價值, 100)

# 以四百八十二文乘之即得
總價值文 = 總升 * 每升價值

# Convert 文 to 貫 (1 貫 = 1000 文)
a = Fraction(總價值文, 1000)  # 78249567/50000 貫
"""
"""
