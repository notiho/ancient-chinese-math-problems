"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
術曰：列米三千二百四十六斛八斗七升，以四百八十二文乘之即得。
答曰： a貫 。
"""

"""
To solve this problem, we need to calculate the total cost of the given amount of rice. The amount of rice is 3246斛8斗7升, and the price per 斛 is 482文. 

First, we need to convert the entire amount of rice into a single unit (升). Since:
- 1斛 = 10斗
- 1斗 = 10升

The total amount of rice in terms of 升 is:
3246斛 = 3246 * 10 * 10升  
8斗 = 8 * 10升  
7升 = 7升  

The total cost is then calculated by multiplying the total amount of rice (in 升) by the price per 斛 (converted to 升). The price per 升 is 482文 / (10 * 10).

Finally, the result is converted into 貫, where 1貫 = 1000文.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
rice_in_hu = 3246  # 斛
rice_in_dou = 8    # 斗
rice_in_sheng = 7  # 升
price_per_hu = 482 # 文 per 斛

# Conversion factors
hu_to_sheng = 10 * 10  # 1斛 = 100升
dou_to_sheng = 10      # 1斗 = 10升
sheng_to_wen = Fraction(price_per_hu, hu_to_sheng)  # 文 per 升

# Total rice in 升
total_rice_in_sheng = (rice_in_hu * hu_to_sheng) + (rice_in_dou * dou_to_sheng) + rice_in_sheng

# Total cost in 文
total_cost_in_wen = total_rice_in_sheng * sheng_to_wen

# Convert cost to 貫 (1貫 = 1000文)
a = total_cost_in_wen / 1000

# Result
a
#----- content ends here -----


"""


The variable `a` will store the total cost in 貫.
"""


"""
"""
