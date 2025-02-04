"""
今有均賦粟甲縣二萬五百二十戶粟一斛二十錢自輸其縣乙縣一萬二千三百一十二戶粟一斛一十錢至輸所二百里丙縣七千一百八十二戶粟一斛一十二錢至輸所一百五十里丁縣一萬三千三百三十八戶粟一斛一十七錢至輸所二百五十里戊縣五千一百三十戶粟一斛一十三錢至輸所一百五十里凡五縣賦輸粟一萬斛一車載二十五斛與僦一里一錢欲以縣戶輸粟令費勞等問縣各粟幾何
術曰以一里僦價乘至輸所里以一車二十五斛除之加一斛粟價則致一斛之費各以約其戶數為衰甲衰一千二十六乙衰六百八十四丙衰三百九十九丁衰四百九十四戊衰二百七十副并為法所賦粟乘未并者各自為實實如法得一
荅曰甲縣 a斛 乙縣 b斛 丙縣 c斛 丁縣 d斛 戊縣 e斛 
"""

#----- content starts here -----
"""
Suppose there are five counties tasked with transporting millet such that the labor and cost are equalized. The details are as follows:

- County A: 20,520 households, millet cost 1 hu and 20 qian, distance to the delivery point 200 li.
- County B: 12,312 households, millet cost 1 hu and 10 qian, distance to the delivery point 200 li.
- County C: 7,182 households, millet cost 1 hu and 12 qian, distance to the delivery point 150 li.
- County D: 13,338 households, millet cost 1 hu and 17 qian, distance to the delivery point 250 li.
- County E: 5,130 households, millet cost 1 hu and 13 qian, distance to the delivery point 150 li.

The total millet to be transported is 10,000 hu. One cart carries 25 hu, and the cost of transport is 1 qian per li per cart. The goal is to distribute the millet among the counties such that the labor and cost are equalized.

The procedure says:
1. Multiply the transport cost per li by the distance to the delivery point.
2. Divide by the amount carried by one cart (25 hu), and add the cost of 1 hu of millet. This gives the cost of transporting 1 hu of millet.
3. Use this cost to weight the household numbers of each county, creating a "weighted household count" for each county.
4. Add the weighted household counts together to form the divisor.
5. Multiply the total millet to be transported by the uncombined weighted household counts to form the dividend for each county.
6. Divide each dividend by the divisor to determine the amount of millet each county should transport.

The answer says: County A transports *a* hu, County B transports *b* hu, County C transports *c* hu, County D transports *d* hu, County E transports *e* hu.
"""

from fractions import Fraction

# Data for each county
households = [20520, 12312, 7182, 13338, 5130]
millet_costs = [Fraction(1, 1) + Fraction(20, 100),  # 1 hu 20 qian
                Fraction(1, 1) + Fraction(10, 100),  # 1 hu 10 qian
                Fraction(1, 1) + Fraction(12, 100),  # 1 hu 12 qian
                Fraction(1, 1) + Fraction(17, 100),  # 1 hu 17 qian
                Fraction(1, 1) + Fraction(13, 100)]  # 1 hu 13 qian
distances = [200, 200, 150, 250, 150]  # Distance to delivery point in li
cart_capacity = 25  # One cart carries 25 hu
transport_cost_per_li = 1  # 1 qian per li per cart
total_millet = 10000  # Total millet to be transported

# Step 1: Calculate the cost of transporting 1 hu of millet for each county
costs_per_hu = []
for i in range(len(households)):
    transport_cost = (transport_cost_per_li * distances[i]) / cart_capacity
    total_cost = transport_cost + millet_costs[i]
    costs_per_hu.append(total_cost)

# Step 2: Calculate the weighted household count for each county
weighted_households = []
for i in range(len(households)):
    weighted_households.append(households[i] / costs_per_hu[i])

# Step 3: Calculate the divisor (sum of weighted household counts)
divisor = sum(weighted_households)

# Step 4: Calculate the dividend for each county
dividends = []
for i in range(len(weighted_households)):
    dividends.append(total_millet * weighted_households[i])

# Step 5: Divide each dividend by the divisor to get the amount of millet for each county
results = []
for dividend in dividends:
    results.append(Fraction(dividend, divisor))

# Assign results to variables
a, b, c, d, e = results

# Output results
a, b, c, d, e#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
