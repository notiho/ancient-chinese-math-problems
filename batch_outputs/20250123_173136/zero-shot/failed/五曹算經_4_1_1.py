"""
今有官田九百畝凡一步收粟三升二合。問：計㡬何？
術曰：列田九百畝以二百四十步乘之得二十一萬六千步以三升二合乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount of grain harvested from a field. The problem states that there are 900 畝 (mu) of land, each 畝 consisting of 240 steps (步), and each step yields 3 升 (sheng) and 2 合 (he) of grain. 

1 升 = 10 合, so 3 升 2 合 = 3.2 升.

Here's the Python code to calculate the total amount of grain in 斛 (hu), where 1 斛 = 10 升:


"""


from fractions import Fraction

# Given values
mu = 900  # 畝
steps_per_mu = 240  # steps per 畝
grain_per_step = Fraction(32, 10)  # 3 升 2 合 = 3.2 升 = 32/10 升
sheng_per_hu = 10  # 1 斛 = 10 升

# Total steps
total_steps = mu * steps_per_mu

# Total grain in 升
total_grain_sheng = total_steps * grain_per_step

# Convert to 斛
a = total_grain_sheng / sheng_per_hu

# Result
a  # This is the total grain in 斛


"""


The variable `a` will contain the total amount of grain in 斛.
"""


"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""
