"""
今有馬六千二百四十三匹，匹給粟五升三合。問：計㡬何？
術曰：列馬六千二百四十三匹，以五升三合乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount of grain (in "斛") required to feed 6,243 horses, where each horse consumes 5升 (sheng) and 3合 (he) of grain. 

1斛 = 10升, and 1升 = 10合. Therefore, 5升3合 = 5 + 3/10 = 53/10升.

### Python Code:

"""


from fractions import Fraction

# Given values
horses = 6243  # Number of horses
grain_per_horse = Fraction(53, 10)  # Grain per horse in 升

# Total grain in 升
total_grain_sheng = horses * grain_per_horse

# Convert 升 to 斛 (1斛 = 10升)
a = total_grain_sheng / 10

# Result
a  # Total grain in 斛


"""


The variable `a` will contain the total amount of grain in "斛".
"""


"""
Variable 'a' has wrong value. Expected: 330879/1000, Actual: 330879/100"""
