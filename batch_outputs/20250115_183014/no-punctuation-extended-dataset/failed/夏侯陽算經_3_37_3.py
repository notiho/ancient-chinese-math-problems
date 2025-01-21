"""
今有糙米三千四百六十四斛五斗七升三合四勺毎斗舂得熟米九升問熟米幾何
術曰先置米數九因退之即得
答曰 a斛
"""

"""
Suppose there are 3464 hu, 5 dou, 7 sheng, 3 ge, and 4 shao of coarse rice.
Each dou of coarse rice yields 9 sheng of cooked rice.
Question: how much cooked rice is obtained?

The procedure says: First, place the amount of coarse rice. Multiply it by 9 and then divide it by 10. The result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 糙米數量
糙米_斛 = 3464
糙米_斗 = 5
糙米_升 = 7
糙米_合 = 3
糙米_勺 = 4

# 將所有單位轉換為升 (1 斛 = 10 斗, 1 斗 = 10 升, 1 升 = 10 合, 1 合 = 10 勺)
糙米_升總數 = (
    (糙米_斛 * 10 * 10 * 10) +  # 斛轉為升
    (糙米_斗 * 10 * 10) +       # 斗轉為升
    (糙米_升 * 10) +            # 升保持不變
    (糙米_合) +                 # 合轉為升
    (Fraction(糙米_勺, 10))      # 勺轉為升
)

# 每斗舂得熟米 9 升，等於每 10 升糙米得 9 升熟米
熟米_升總數 = (糙米_升總數 * 9) / 10

# 將熟米轉換回斛 (1 斛 = 10 斗, 1 斗 = 10 升)
熟米_斛 = 熟米_升總數 / (10 * 10)

a = 熟米_斛
"""
Variable 'a' has wrong value. Expected: 155905803/50000, Actual: 155905803/5000"""
