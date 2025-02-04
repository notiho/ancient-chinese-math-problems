"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

#----- content starts here -----
"""
Suppose there is a tax distribution of millet among five counties:
- County A has 20,520 households, and the cost of millet is 1 hu and 20 qian, transported within the county.
- County B has 12,312 households, and the cost of millet is 1 hu and 10 qian, transported 200 li to the delivery location.
- County C has 7,182 households, and the cost of millet is 1 hu and 12 qian, transported 150 li to the delivery location.
- County D has 13,338 households, and the cost of millet is 1 hu and 17 qian, transported 250 li to the delivery location.
- County E has 5,130 households, and the cost of millet is 1 hu and 13 qian, transported 150 li to the delivery location.

In total, the five counties must deliver 10,000 hu of millet. One cart carries 25 hu, and the transport cost is 1 qian per li. The goal is to distribute the millet such that the labor and costs are equalized among the counties.

The procedure says:
- Multiply the transport cost per li by the distance to the delivery location.
- Divide by the amount carried by one cart (25 hu), and add the cost of 1 hu of millet. This gives the cost of delivering 1 hu of millet.
- Multiply this cost by the number of households in each county to get the "weight" (衰) for each county.
- The weights for the counties are:
  - County A: 1,026
  - County B: 684
  - County C: 399
  - County D: 494
  - County E: 270
- Add these weights together to get the divisor (法).
- Multiply the total millet to be delivered (10,000 hu) by the weight of each county to get the dividend (實) for each county.
- Divide the dividend by the divisor to get the amount of millet each county must deliver.

The answer says:
- County A delivers *a* hu.
- County B delivers *b* hu.
- County C delivers *c* hu.
- County D delivers *d* hu.
- County E delivers *e* hu.
"""

# Data for each county
households = [20520, 12312, 7182, 13338, 5130]  # Number of households
millet_costs = [120, 110, 112, 117, 113]  # Cost of 1 hu of millet in qian
distances = [0, 200, 150, 250, 150]  # Distance to the delivery location in li
cart_capacity = 25  # One cart carries 25 hu
transport_cost_per_li = 1  # Cost of transport per li in qian
total_millet = 10000  # Total millet to be delivered in hu

# Calculate the weight (衰) for each county
weights = []
for i in range(5):
    transport_cost = distances[i] * transport_cost_per_li  # Transport cost for the distance
    cost_per_hu = transport_cost / cart_capacity + millet_costs[i]  # Cost of delivering 1 hu
    weight = cost_per_hu * households[i]  # Weight for the county
    weights.append(weight)

# Calculate the divisor (法)
法 = sum(weights)

# Calculate the amount of millet each county must deliver
results = [Fraction(total_millet * weight, 法) for weight in weights]

# Assign results to each county
a, b, c, d, e = results#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
