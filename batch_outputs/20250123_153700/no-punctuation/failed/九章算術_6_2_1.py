"""
今有均賦粟甲縣二萬五百二十戶粟一斛二十錢自輸其縣乙縣一萬二千三百一十二戶粟一斛一十錢至輸所二百里丙縣七千一百八十二戶粟一斛一十二錢至輸所一百五十里丁縣一萬三千三百三十八戶粟一斛一十七錢至輸所二百五十里戊縣五千一百三十戶粟一斛一十三錢至輸所一百五十里凡五縣賦輸粟一萬斛一車載二十五斛與僦一里一錢欲以縣戶輸粟令費勞等問縣各粟幾何
術曰以一里僦價乘至輸所里以一車二十五斛除之加一斛粟價則致一斛之費各以約其戶數為衰甲衰一千二十六乙衰六百八十四丙衰三百九十九丁衰四百九十四戊衰二百七十副并為法所賦粟乘未并者各自為實實如法得一
荅曰甲縣 a斛 乙縣 b斛 丙縣 c斛 丁縣 d斛 戊縣 e斛 
"""

"""
Suppose there are five counties contributing millet for taxation. The details are as follows:
- County A: 20,520 households, millet cost is 1 hu and 20 qian, distance to the delivery site is 200 li.
- County B: 12,312 households, millet cost is 1 hu and 10 qian, distance to the delivery site is 200 li.
- County C: 7,182 households, millet cost is 1 hu and 12 qian, distance to the delivery site is 150 li.
- County D: 13,338 households, millet cost is 1 hu and 17 qian, distance to the delivery site is 250 li.
- County E: 5,130 households, millet cost is 1 hu and 13 qian, distance to the delivery site is 150 li.

The total millet to be delivered is 10,000 hu. Each cart carries 25 hu, and the cost of transportation is 1 qian per li per cart. It is desired to distribute the millet among the counties such that the labor and cost are equalized.

The procedure says:
1. Multiply the transportation cost per li by the distance to the delivery site.
2. Divide by the amount carried by one cart (25 hu).
3. Add the cost of 1 hu of millet to obtain the cost of delivering 1 hu of millet.
4. Use this cost to weight the household numbers of each county, obtaining the "declining sequence" for each county.
5. Add these weights together to form the divisor.
6. Multiply the total millet to be delivered by the weights (before summing) to form the dividend for each county.
7. Divide the dividend by the divisor to obtain the amount of millet each county should deliver.

The answer says:
- County A delivers *a* hu.
- County B delivers *b* hu.
- County C delivers *c* hu.
- County D delivers *d* hu.
- County E delivers *e* hu.
"""

from fractions import Fraction

# County data
households = [20520, 12312, 7182, 13338, 5130]  # Number of households in each county
millet_costs = [120, 110, 112, 117, 113]  # Cost of 1 hu of millet in qian
distances = [200, 200, 150, 250, 150]  # Distance to the delivery site in li
cart_capacity = 25  # Cart capacity in hu
transport_cost_per_li = 1  # Cost of transporting 1 cart 1 li in qian
total_millet = 10000  # Total millet to be delivered in hu

# Step 1: Calculate the cost of delivering 1 hu of millet for each county
delivery_costs = []
for i in range(len(households)):
    transport_cost = (distances[i] * transport_cost_per_li) / cart_capacity  # Transportation cost per hu
    total_cost = transport_cost + millet_costs[i]  # Total cost per hu
    delivery_costs.append(total_cost)

# Step 2: Weight the household numbers by the delivery costs
weights = []
for i in range(len(households)):
    weight = households[i] / delivery_costs[i]
    weights.append(weight)

# Step 3: Calculate the divisor (sum of weights)
divisor = sum(weights)

# Step 4: Calculate the dividend for each county
dividends = []
for i in range(len(weights)):
    dividend = total_millet * weights[i]
    dividends.append(dividend)

# Step 5: Divide the dividend by the divisor to get the amount of millet each county should deliver
results = []
for dividend in dividends:
    result = Fraction(dividend, divisor)
    results.append(result)

# Assign results to variables
a, b, c, d, e = results

# Output the results
a, b, c, d, e
"""
Code error: both arguments should be Rational instances"""
