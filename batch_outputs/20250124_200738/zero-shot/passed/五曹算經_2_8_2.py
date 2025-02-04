"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
術曰：列米三千二百四十六斛八斗七升，以四百八十二文乘之即得。
答曰： a貫 。
"""

"""
To solve this problem, we need to calculate the total cost of the given amount of rice. The amount of rice is 3246斛8斗7升, and the price per 斛 is 482文. 

In ancient Chinese measurements:
- 1斛 = 10斗
- 1斗 = 10升

We first convert the total amount of rice into a single unit (升), then calculate the total cost.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Convert the rice amount into 升
total_rice_in_sheng = 3246 * 10 * 10 + 8 * 10 + 7  # 斛 to 升, 斗 to 升, and add 升

# Price per 升 (since 1斛 = 100升, price per 升 = 482文 / 100)
price_per_sheng = Fraction(482, 100)

# Total cost in 文
total_cost_in_wen = total_rice_in_sheng * price_per_sheng

# Convert 文 to 貫 (1貫 = 1000文)
a = total_cost_in_wen / 1000

# Result
a  # This is the total cost in 貫
#----- content ends here -----


"""


The variable `a` will contain the total cost in 貫.
"""


"""
"""
