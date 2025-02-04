"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
術曰：列米三千二百四十六斛八斗七升，以四百八十二文乘之即得。
答曰： a貫 。
"""

"""
To solve this problem, we need to calculate the total cost of the given amount of rice. The amount of rice is 3246斛8斗7升, and the price per 斛 is 482文. 

First, we need to convert the rice amount into a consistent unit (升). Since:
- 1斛 = 10斗
- 1斗 = 10升

The total amount of rice in 升 is:
```
3246斛 = 3246 * 10 * 10 = 324600升
8斗 = 8 * 10 = 80升
7升 = 7升
Total = 324600 + 80 + 7 = 324687升
```

Next, we calculate the total cost in 文. Since the price is given per 斛, we first convert the total rice back to 斛:
```
Total rice in 斛 = 324687升 / (10 * 10) = 3246.87斛
```

The total cost in 文 is:
```
Total cost in 文 = 3246.87 * 482
```

Finally, we convert 文 to 貫. Since 1貫 = 1000文:
```
Total cost in 貫 = Total cost in 文 / 1000
```

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
rice_in_hu = 3246  # 斛
rice_in_dou = 8    # 斗
rice_in_sheng = 7  # 升
price_per_hu = 482  # 文 per 斛

# Convert rice to total 升
total_rice_in_sheng = rice_in_hu * 10 * 10 + rice_in_dou * 10 + rice_in_sheng

# Convert total rice to 斛
total_rice_in_hu = Fraction(total_rice_in_sheng, 10 * 10)

# Calculate total cost in 文
total_cost_in_wen = total_rice_in_hu * price_per_hu

# Convert total cost to 貫
a = total_cost_in_wen / 1000

# Output the result
a
#----- content ends here -----


"""


The variable `a` will contain the total cost in 貫.
"""


"""
"""
