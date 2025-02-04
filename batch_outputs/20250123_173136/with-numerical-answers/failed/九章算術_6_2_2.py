"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a(=10260000/2873)斛 。乙縣 b(=6840000/2873)斛 。丙縣 c(=3990000/2873)斛 。丁縣 d(=380000/221)斛 。戊縣 e(=2700000/2873)斛 。
"""

"""
Suppose there is an equal distribution of grain tax among counties:
County A has 20,520 households, and each household pays 1 hu and 20 qian of grain, delivered to its own county.
County B has 12,312 households, and each household pays 1 hu and 10 qian of grain, delivered 200 li to the delivery site.
County C has 7,182 households, and each household pays 1 hu and 12 qian of grain, delivered 150 li to the delivery site.
County D has 13,338 households, and each household pays 1 hu and 17 qian of grain, delivered 250 li to the delivery site.
County E has 5,130 households, and each household pays 1 hu and 13 qian of grain, delivered 150 li to the delivery site.
In total, the grain tax is 10,000 hu. One cart carries 25 hu, and the transport cost is 1 qian per li.
It is desired to distribute the grain tax among the counties such that the labor cost is equalized.
Question: how much grain does each county contribute?

The procedure says: Multiply the transport cost per li by the distance to the delivery site, and divide by the 25 hu carried by one cart.
Add the grain cost per hu, obtaining the cost of delivering 1 hu of grain.
For each county, multiply this cost by the number of households, obtaining the "weight" for that county.
Add all weights together to obtain the divisor.
Multiply the total grain tax by the weight of each county, obtaining the dividend for each county.
Divide the dividend by the divisor to obtain the grain contribution for each county.

Answer: County A contributes *a*(=10260000/2873) hu, County B contributes *b*(=6840000/2873) hu, County C contributes *c*(=3990000/2873) hu, County D contributes *d*(=380000/221) hu, County E contributes *e*(=2700000/2873) hu.
"""

from fractions import Fraction

# Data for each county
counties = [
    {"households": 20520, "grain_cost": Fraction(120, 100), "distance": 0},    # County A
    {"households": 12312, "grain_cost": Fraction(110, 100), "distance": 200},  # County B
    {"households": 7182, "grain_cost": Fraction(112, 100), "distance": 150},   # County C
    {"households": 13338, "grain_cost": Fraction(117, 100), "distance": 250},  # County D
    {"households": 5130, "grain_cost": Fraction(113, 100), "distance": 150},   # County E
]

# Constants
cart_capacity = 25  # hu per cart
transport_cost_per_li = 1  # qian per li
total_grain_tax = 10000  # hu

# Calculate the "weight" (衰) for each county
weights = []
for county in counties:
    transport_cost = Fraction(transport_cost_per_li * county["distance"], cart_capacity)
    total_cost_per_hu = county["grain_cost"] + transport_cost
    weight = total_cost_per_hu * county["households"]
    weights.append(weight)

# Calculate the divisor (法)
divisor = sum(weights)

# Calculate the grain contribution for each county
contributions = []
for weight in weights:
    contribution = Fraction(total_grain_tax) * weight / divisor
    contributions.append(contribution)

# Assign contributions to variables for clarity
a, b, c, d, e = contributions

# Results
a, b, c, d, e  # County A, B, C, D, E contributions in hu
"""
Variable 'a' has wrong value. Expected: 10260000/2873, Actual: 800000/1213
Variable 'b' has wrong value. Expected: 6840000/2873, Actual: 3640000/1213
Variable 'c' has wrong value. Expected: 3990000/2873, Actual: 4984000/3639
Variable 'd' has wrong value. Expected: 380000/221, Actual: 14521000/3639
Variable 'e' has wrong value. Expected: 2700000/2873, Actual: 3565000/3639"""
