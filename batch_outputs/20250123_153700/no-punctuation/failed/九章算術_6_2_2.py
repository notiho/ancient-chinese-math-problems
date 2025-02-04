"""
今有均賦粟甲縣二萬五百二十戶粟一斛二十錢自輸其縣乙縣一萬二千三百一十二戶粟一斛一十錢至輸所二百里丙縣七千一百八十二戶粟一斛一十二錢至輸所一百五十里丁縣一萬三千三百三十八戶粟一斛一十七錢至輸所二百五十里戊縣五千一百三十戶粟一斛一十三錢至輸所一百五十里凡五縣賦輸粟一萬斛一車載二十五斛與僦一里一錢欲以縣戶輸粟令費勞等問縣各粟幾何
術曰以一里僦價乘至輸所里以一車二十五斛除之加一斛粟價則致一斛之費各以約其戶數為衰甲衰一千二十六乙衰六百八十四丙衰三百九十九丁衰四百九十四戊衰二百七十副并為法所賦粟乘未并者各自為實實如法得一
荅曰甲縣 a斛 乙縣 b斛 丙縣 c斛 丁縣 d斛 戊縣 e斛 
"""

"""
Suppose there are five counties tasked with transporting millet such that the labor and cost are equalized.

- County A has 20,520 households, each household contributing 1 hu and 20 qian of millet, and the transport distance is 200 li.
- County B has 12,312 households, each household contributing 1 hu and 10 qian of millet, and the transport distance is 200 li.
- County C has 7,182 households, each household contributing 1 hu and 12 qian of millet, and the transport distance is 150 li.
- County D has 13,338 households, each household contributing 1 hu and 17 qian of millet, and the transport distance is 250 li.
- County E has 5,130 households, each household contributing 1 hu and 13 qian of millet, and the transport distance is 150 li.

The total millet to be transported is 10,000 hu. Each cart carries 25 hu, and the transport cost is 1 qian per li per cart.

Question: How much millet should each county contribute to equalize the labor and cost?

The procedure says:
1. Multiply the transport distance (in li) by the cost per li (1 qian) and divide by the cart capacity (25 hu). Add the cost of 1 hu of millet to get the cost of transporting 1 hu of millet.
2. Use this cost to weight the household numbers for each county, obtaining the "declining sequence" (衰).
3. Add the declining sequences together to get the divisor (法).
4. Multiply the total millet by the declining sequence of each county to get the dividend (實).
5. Divide the dividend by the divisor to get the amount of millet each county should contribute.

Answer: County A contributes *a* hu, County B contributes *b* hu, County C contributes *c* hu, County D contributes *d* hu, and County E contributes *e* hu.
"""

# Data for each county
counties = [
    {"households": 20520, "millet_cost": 1 + Fraction(20, 100), "distance": 200},
    {"households": 12312, "millet_cost": 1 + Fraction(10, 100), "distance": 200},
    {"households": 7182, "millet_cost": 1 + Fraction(12, 100), "distance": 150},
    {"households": 13338, "millet_cost": 1 + Fraction(17, 100), "distance": 250},
    {"households": 5130, "millet_cost": 1 + Fraction(13, 100), "distance": 150},
]

# Constants
cart_capacity = 25  # hu
transport_cost_per_li = 1  # qian
total_millet = 10000  # hu

# Step 1: Calculate the cost of transporting 1 hu of millet for each county
for county in counties:
    transport_cost = (county["distance"] * transport_cost_per_li) / cart_capacity
    county["cost_per_hu"] = transport_cost + county["millet_cost"]

# Step 2: Use the cost to weight the household numbers (declining sequence)
for county in counties:
    county["declining_sequence"] = county["households"] / county["cost_per_hu"]

# Step 3: Add the declining sequences together to get the divisor (法)
法 = sum(county["declining_sequence"] for county in counties)

# Step 4: Multiply the total millet by the declining sequence of each county to get the dividend (實)
for county in counties:
    county["dividend"] = total_millet * county["declining_sequence"]

# Step 5: Divide the dividend by the divisor to get the amount of millet each county should contribute
for county in counties:
    county["millet_contribution"] = county["dividend"] / 法

# Extract results
a = counties[0]["millet_contribution"]
b = counties[1]["millet_contribution"]
c = counties[2]["millet_contribution"]
d = counties[3]["millet_contribution"]
e = counties[4]["millet_contribution"]
"""
Variable 'a' has wrong value. Expected: 10260000/2873, Actual: 3428.433717870159
Variable 'b' has wrong value. Expected: 6840000/2873, Actual: 2079.665288202558
Variable 'c' has wrong value. Expected: 3990000/2873, Actual: 1550.4995184749873
Variable 'd' has wrong value. Expected: 380000/221, Actual: 1835.4551148490193
Variable 'e' has wrong value. Expected: 2700000/2873, Actual: 1105.9463606032768"""
