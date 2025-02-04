"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
術曰：列米三千二百四十六斛八斗七升，以四百八十二文乘之即得。
答曰： a貫 。
"""

"""
To solve this problem, we need to calculate the total cost of the given amount of rice. The total amount of rice is 3246斛8斗7升, and the price per 斛 is 482文. We'll first convert the rice into a single unit (升), calculate the total cost in 文, and then convert the result into 貫 (1貫 = 1000文).

Here's the Python code:


"""


from fractions import Fraction

# Conversion factors
斗_to_升 = 10  # 1斗 = 10升
斛_to_升 = 100  # 1斛 = 100升
文_to_貫 = 1000  # 1貫 = 1000文

# Given data
rice_斛 = 3246
rice_斗 = 8
rice_升 = 7
price_per_斛 = 482  # in 文

# Convert total rice to 升
total_rice_升 = rice_斛 * 斛_to_升 + rice_斗 * 斗_to_升 + rice_升

# Calculate total cost in 文
total_cost_文 = total_rice_升 / 斛_to_升 * price_per_斛

# Convert total cost to 貫
a = Fraction(total_cost_文, 文_to_貫)

# Output the result
a


"""


The variable `a` will contain the total cost in 貫 as a `Fraction`.
"""


"""
Code error: both arguments should be Rational instances"""
