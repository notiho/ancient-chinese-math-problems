"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
Suppose there is a tax distribution of millet among five counties:
- County A has 20,520 households, with a millet cost of 1 hu and 20 qian, and they deliver to their own county.
- County B has 12,312 households, with a millet cost of 1 hu and 10 qian, and they deliver to a location 200 li away.
- County C has 7,182 households, with a millet cost of 1 hu and 12 qian, and they deliver to a location 150 li away.
- County D has 13,338 households, with a millet cost of 1 hu and 17 qian, and they deliver to a location 250 li away.
- County E has 5,130 households, with a millet cost of 1 hu and 13 qian, and they deliver to a location 150 li away.

In total, the five counties must deliver 10,000 hu of millet. One cart carries 25 hu, and the transport cost is 1 qian per li. It is desired to distribute the millet among the counties such that the labor and costs are equalized.

The procedure says: Multiply the transport cost per li by the distance to the delivery location. Divide by the amount carried by one cart (25 hu), and add the cost of 1 hu of millet. This gives the cost of delivering 1 hu of millet. Multiply this cost by the number of households in each county to obtain the "weight" (衰) for each county. Add all weights together to obtain the divisor (法). Multiply the total millet to be delivered by the weight of each county to obtain the dividend (實). Divide the dividend by the divisor to obtain the amount of millet for each county.

The weights (衰) are:
- County A: 1,026
- County B: 684
- County C: 399
- County D: 494
- County E: 270

Answer: County A delivers *a* hu, County B delivers *b* hu, County C delivers *c* hu, County D delivers *d* hu, and County E delivers *e* hu.
"""

from fractions import Fraction

# Data for each county
households = [20520, 12312, 7182, 13338, 5130]
millet_costs = [120, 110, 112, 117, 113]  # Cost of 1 hu in qian
distances = [0, 200, 150, 250, 150]  # Distance to delivery location in li
cart_capacity = 25  # Cart capacity in hu
transport_cost_per_li = 1  # Cost per li in qian
total_millet = 10000  # Total millet to be delivered in hu

# Calculate weights (衰) for each county
weights = []
for i in range(len(households)):
    transport_cost = (distances[i] * transport_cost_per_li) / cart_capacity
    total_cost_per_hu = transport_cost + millet_costs[i]
    weight = total_cost_per_hu * households[i]
    weights.append(weight)

# Calculate the divisor (法)
法 = sum(weights)

# Calculate the amount of millet for each county
results = []
for weight in weights:
    实 = total_millet * weight
    amount = Fraction(实, 法)
    results.append(amount)

# Assign results to variables
a, b, c, d, e = results
"""
Code error: both arguments should be Rational instances"""
