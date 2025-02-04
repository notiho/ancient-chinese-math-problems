"""
今有馬六千二百四十三匹，匹給粟五升三合。問：計㡬何？
術曰：列馬六千二百四十三匹，以五升三合乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount of grain required for 6,243 horses, where each horse is given 5升 (shēng) and 3合 (hép). 

1斛 = 10斗, 1斗 = 10升, and 1升 = 10合. Therefore, 5升3合 = 5.3升.

The calculation involves multiplying the number of horses (6,243) by the grain amount per horse (5.3升), then converting the result into 斛.

Here is the Python code:


"""


from fractions import Fraction

# Number of horses
horses = 6243

# Grain per horse in 升 (5升3合 = 5.3升)
grain_per_horse = Fraction(53, 10)  # 5.3升

# Total grain in 升
total_grain_sheng = horses * grain_per_horse

# Convert 升 to 斛 (1斛 = 100升)
a = total_grain_sheng / 100

# Result
a  # Total grain in 斛


"""


The variable `a` will contain the total amount of grain in 斛.
"""


"""
"""
