"""
今有馬六千二百四十三匹，匹給粟五升三合。問：計㡬何？
術曰：列馬六千二百四十三匹，以五升三合乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount of grain (in "斛") required for 6,243 horses, where each horse consumes 5升 (sheng) and 3合 (he) of grain. 

### Conversion:
1 斛 = 10 升  
1 升 = 10 合  

Thus, 5升3合 = 5 + 3/10 升 = 53/10 升.

### Calculation:
The total grain required is:  
6,243 horses × (53/10 升 per horse).

Finally, we convert the result from 升 to 斛 by dividing by 10 (since 1 斛 = 10 升).

Here is the Python code:


"""


from fractions import Fraction

# Given data
horses = 6243
grain_per_horse = Fraction(53, 10)  # 5升3合 = 53/10 升

# Total grain in 升
total_grain_sheng = horses * grain_per_horse

# Convert to 斛
a = total_grain_sheng / 10  # 1 斛 = 10 升

# Result
a  # Total grain in 斛


"""


The variable `a` will contain the total grain required in 斛.
"""


"""
Variable 'a' has wrong value. Expected: 330879/1000, Actual: 330879/100"""
