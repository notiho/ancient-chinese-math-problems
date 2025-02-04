"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
術曰：列米三千二百四十六斛八斗七升，以四百八十二文乘之即得。
答曰： a貫 。
"""

"""
To solve this problem, we need to calculate the total cost of the given amount of rice. The amount of rice is 3246斛8斗7升, and the price per 斛 is 482文. Note that 1斛 = 10斗 and 1斗 = 10升. Therefore, we first convert the total amount of rice into a single unit (斛) and then multiply it by the price per 斛.

Here is the Python code:


"""


from fractions import Fraction

# Given data
rice_in_hu = 3246  # 斛
rice_in_dou = 8    # 斗
rice_in_sheng = 7  # 升
price_per_hu = 482  # 文 per 斛

# Convert the total rice amount to 斛
total_rice_in_hu = rice_in_hu + Fraction(rice_in_dou, 10) + Fraction(rice_in_sheng, 100)

# Calculate the total cost in 文
total_cost_in_wen = total_rice_in_hu * price_per_hu

# Convert the total cost to 貫 (1貫 = 1000文)
a = total_cost_in_wen / 1000

# The answer is stored in variable 'a'


"""


The variable `a` contains the total cost in 貫.
"""


"""
"""
