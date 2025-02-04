"""
今有均賦粟甲縣二萬五百二十戶粟一斛二十錢自輸其縣乙縣一萬二千三百一十二戶粟一斛一十錢至輸所二百里丙縣七千一百八十二戶粟一斛一十二錢至輸所一百五十里丁縣一萬三千三百三十八戶粟一斛一十七錢至輸所二百五十里戊縣五千一百三十戶粟一斛一十三錢至輸所一百五十里凡五縣賦輸粟一萬斛一車載二十五斛與僦一里一錢欲以縣戶輸粟令費勞等問縣各粟幾何
術曰以一里僦價乘至輸所里以一車二十五斛除之加一斛粟價則致一斛之費各以約其戶數為衰甲衰一千二十六乙衰六百八十四丙衰三百九十九丁衰四百九十四戊衰二百七十副并為法所賦粟乘未并者各自為實實如法得一
荅曰甲縣 a斛 乙縣 b斛 丙縣 c斛 丁縣 d斛 戊縣 e斛 
"""

#----- content starts here -----
"""
Suppose there are five counties tasked with transporting millet, with the goal of equalizing labor and costs. The details are as follows:

- County A: 20,520 households, millet cost 1 hu 20 qian, distance to the delivery site 200 li.
- County B: 12,312 households, millet cost 1 hu 10 qian, distance to the delivery site 200 li.
- County C: 7,182 households, millet cost 1 hu 12 qian, distance to the delivery site 150 li.
- County D: 13,338 households, millet cost 1 hu 17 qian, distance to the delivery site 250 li.
- County E: 5,130 households, millet cost 1 hu 13 qian, distance to the delivery site 150 li.

The total millet to be transported is 10,000 hu. One cart carries 25 hu, and the transport cost is 1 qian per li per cart. The goal is to distribute the millet among the counties such that the labor and costs are equalized. 

The procedure says:
1. Multiply the transport cost per li by the distance to the delivery site.
2. Divide by the amount carried by one cart (25 hu).
3. Add the cost of 1 hu of millet to obtain the cost of transporting 1 hu.
4. Use the number of households in each county to calculate the "weight" (衰) for each county:
   - County A: 1,026
   - County B: 684
   - County C: 399
   - County D: 494
   - County E: 270
5. Add the weights together to form the divisor (法).
6. Multiply the total millet by the weights of each county to form the dividend (實).
7. Divide the dividend by the divisor to obtain the amount of millet each county should transport.

The answer says: County A transports *a* hu, County B transports *b* hu, County C transports *c* hu, County D transports *d* hu, County E transports *e* hu.
"""

# Data for each county
counties = [
    {"households": 20520, "millet_cost": 120, "distance": 200},  # County A
    {"households": 12312, "millet_cost": 110, "distance": 200},  # County B
    {"households": 7182, "millet_cost": 112, "distance": 150},   # County C
    {"households": 13338, "millet_cost": 117, "distance": 250},  # County D
    {"households": 5130, "millet_cost": 113, "distance": 150},   # County E
]

# Constants
cart_capacity = 25  # One cart carries 25 hu
transport_cost_per_li = 1  # 1 qian per li per cart
total_millet = 10000  # Total millet to be transported

# Step 1: Calculate the weight (衰) for each county
for county in counties:
    # Multiply transport cost per li by distance
    transport_cost = transport_cost_per_li * county["distance"]
    # Divide by cart capacity
    transport_cost_per_hu = transport_cost / cart_capacity
    # Add the cost of 1 hu of millet
    total_cost_per_hu = transport_cost_per_hu + county["millet_cost"]
    # Use the number of households to calculate the weight
    county["weight"] = county["households"] / total_cost_per_hu

# Step 2: Calculate the divisor (法)
divisor = sum(county["weight"] for county in counties)

# Step 3: Calculate the dividend (實) for each county
for county in counties:
    county["dividend"] = total_millet * county["weight"]

# Step 4: Divide the dividend by the divisor to get the amount of millet for each county
results = [Fraction(county["dividend"], divisor) for county in counties]

# Assign results to variables
a, b, c, d, e = results#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
