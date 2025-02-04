"""
今有均賦粟甲縣二萬五百二十戶粟一斛二十錢自輸其縣乙縣一萬二千三百一十二戶粟一斛一十錢至輸所二百里丙縣七千一百八十二戶粟一斛一十二錢至輸所一百五十里丁縣一萬三千三百三十八戶粟一斛一十七錢至輸所二百五十里戊縣五千一百三十戶粟一斛一十三錢至輸所一百五十里凡五縣賦輸粟一萬斛一車載二十五斛與僦一里一錢欲以縣戶輸粟令費勞等問縣各粟幾何
術曰以一里僦價乘至輸所里以一車二十五斛除之加一斛粟價則致一斛之費各以約其戶數為衰甲衰一千二十六乙衰六百八十四丙衰三百九十九丁衰四百九十四戊衰二百七十副并為法所賦粟乘未并者各自為實實如法得一
荅曰甲縣 a斛 乙縣 b斛 丙縣 c斛 丁縣 d斛 戊縣 e斛 
"""

#----- content starts here -----
"""
Suppose there are five counties tasked with transporting millet, with the goal of equalizing labor and cost. The details are as follows:

- County A: 20,520 households, millet cost 1 hu 20 qian, distance to the delivery site 200 li.
- County B: 12,312 households, millet cost 1 hu 10 qian, distance to the delivery site 200 li.
- County C: 7,182 households, millet cost 1 hu 12 qian, distance to the delivery site 150 li.
- County D: 13,338 households, millet cost 1 hu 17 qian, distance to the delivery site 250 li.
- County E: 5,130 households, millet cost 1 hu 13 qian, distance to the delivery site 150 li.

The total millet to be transported is 10,000 hu. One cart carries 25 hu, and the transport cost is 1 qian per li per cart. The goal is to distribute the millet among the counties such that the labor and cost are equalized.

The procedure says:
1. Multiply the transport cost per li by the distance to the delivery site.
2. Divide by the capacity of one cart (25 hu).
3. Add the cost of 1 hu of millet to this value, resulting in the cost of transporting 1 hu of millet.
4. Use this cost to weight the number of households in each county, producing a "declining sequence" for each county.
   - County A: 1,026
   - County B: 684
   - County C: 399
   - County D: 494
   - County E: 270
5. Add these weights together to form the divisor.
6. Multiply the total millet to be transported (10,000 hu) by the weights of each county, producing the dividend for each county.
7. Divide each dividend by the divisor to determine the amount of millet each county should transport.

The answer says: County A transports *a* hu, County B transports *b* hu, County C transports *c* hu, County D transports *d* hu, and County E transports *e* hu.
"""

# Data for each county
households = [20520, 12312, 7182, 13338, 5130]  # Number of households
millet_costs = [120, 110, 112, 117, 113]  # Cost of 1 hu of millet in qian
distances = [200, 200, 150, 250, 150]  # Distance to the delivery site in li
cart_capacity = 25  # One cart carries 25 hu
transport_cost_per_li = 1  # Cost of transport per li per cart in qian
total_millet = 10000  # Total millet to be transported in hu

# Calculate the declining sequence (weights) for each county
weights = []
for i in range(len(households)):
    # Multiply the transport cost per li by the distance
    transport_cost = transport_cost_per_li * distances[i]
    # Divide by the cart capacity
    transport_cost_per_hu = transport_cost / cart_capacity
    # Add the cost of 1 hu of millet
    total_cost_per_hu = transport_cost_per_hu + millet_costs[i]
    # Weight the number of households by the cost
    weight = households[i] / total_cost_per_hu
    weights.append(weight)

# Use the given weights for each county
weights = [1026, 684, 399, 494, 270]

# Add the weights together to form the divisor
divisor = sum(weights)

# Multiply the total millet by the weights to produce the dividend for each county
dividends = [total_millet * weight for weight in weights]

# Divide each dividend by the divisor to determine the amount of millet each county should transport
a, b, c, d, e = [Fraction(dividend, divisor) for dividend in dividends]#----- content ends here -----

"""
"""
