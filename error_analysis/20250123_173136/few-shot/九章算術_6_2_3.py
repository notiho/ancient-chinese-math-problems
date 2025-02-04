"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
Suppose there is a tax distribution of millet among five counties:
- County A has 20,520 households, with a millet cost of 1 hu and 20 qian, and the millet is delivered directly to the county.
- County B has 12,312 households, with a millet cost of 1 hu and 10 qian, and the delivery distance is 200 li.
- County C has 7,182 households, with a millet cost of 1 hu and 12 qian, and the delivery distance is 150 li.
- County D has 13,338 households, with a millet cost of 1 hu and 17 qian, and the delivery distance is 250 li.
- County E has 5,130 households, with a millet cost of 1 hu and 13 qian, and the delivery distance is 150 li.

In total, the five counties must deliver 10,000 hu of millet. Each cart carries 25 hu, and the transportation cost is 1 qian per li. 
It is desired to distribute the millet among the counties such that the labor and costs are equalized. 
Question: how much millet does each county deliver?

The procedure says:
- Multiply the transportation cost per li by the delivery distance in li.
- Divide by the amount carried by one cart (25 hu), and add the cost of 1 hu of millet. This gives the cost of delivering 1 hu of millet.
- Multiply this cost by the number of households in each county to obtain the "weight" for each county.
- The weights are: County A = 1026, County B = 684, County C = 399, County D = 494, County E = 270.
- Add the weights together to obtain the divisor.
- Multiply the total millet to be delivered by the weights of each county to obtain the dividend for each county.
- Divide the dividend by the divisor to obtain the amount of millet each county delivers.

Answer: County A delivers *a* hu, County B delivers *b* hu, County C delivers *c* hu, County D delivers *d* hu, County E delivers *e* hu.
"""

# Data for each county
#ERR: misunderstood expression
# 粟一斛一十錢 -> a millet cost of 1 hu and 10 qian etc.
"""counties = [
    {"households": 20520, "millet_cost": 120, "distance": 0},   # County A
    {"households": 12312, "millet_cost": 110, "distance": 200}, # County B
    {"households": 7182, "millet_cost": 112, "distance": 150},  # County C
    {"households": 13338, "millet_cost": 117, "distance": 250}, # County D
    {"households": 5130, "millet_cost": 113, "distance": 150},  # County E
]"""
counties = [
    {"households": 20520, "millet_cost": 20, "distance": 0},   # County A
    {"households": 12312, "millet_cost": 10, "distance": 200}, # County B
    {"households": 7182, "millet_cost": 12, "distance": 150},  # County C
    {"households": 13338, "millet_cost": 17, "distance": 250}, # County D
    {"households": 5130, "millet_cost": 13, "distance": 150},  # County E
]

# Constants
cart_capacity = 25  # A cart carries 25 hu
transport_cost_per_li = 1  # 1 qian per li
total_millet = 10000  # Total millet to be delivered

# Calculate the weights for each county
weights = []
for county in counties:
    # Calculate the cost of delivering 1 hu of millet
#ERR: code error (fractions)
    #transport_cost = (transport_cost_per_li * county["distance"]) / cart_capacity
    transport_cost = Fraction(transport_cost_per_li * county["distance"], cart_capacity)
    total_cost_per_hu = transport_cost + county["millet_cost"]
    
    # Calculate the weight for the county
#ERR: misunderstood expression
    #以約其戶數 -> Multiply this cost by the number of households
    #weight = total_cost_per_hu * county["households"]
    weight = county["households"] / total_cost_per_hu
    weights.append(weight)

print(weights)

# Calculate the divisor (sum of weights)
divisor = sum(weights)

# Calculate the amount of millet each county delivers
results = []
for weight in weights:
    millet_delivered = Fraction(weight * total_millet, divisor)
    results.append(millet_delivered)

# Assign results to variables
a, b, c, d, e = results
"""
Code error: both arguments should be Rational instances"""
