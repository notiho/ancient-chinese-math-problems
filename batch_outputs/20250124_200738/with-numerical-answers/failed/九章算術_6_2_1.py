"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a(=10260000/2873)斛 。乙縣 b(=6840000/2873)斛 。丙縣 c(=3990000/2873)斛 。丁縣 d(=380000/221)斛 。戊縣 e(=2700000/2873)斛 。
"""

#----- content starts here -----
"""
Suppose there is an equal distribution of grain tax among counties:
County A has 20,520 households, and each household pays 1 hu and 20 qian of grain, delivering it directly to the county.
County B has 12,312 households, and each household pays 1 hu and 10 qian of grain, delivering it to a location 200 li away.
County C has 7,182 households, and each household pays 1 hu and 12 qian of grain, delivering it to a location 150 li away.
County D has 13,338 households, and each household pays 1 hu and 17 qian of grain, delivering it to a location 250 li away.
County E has 5,130 households, and each household pays 1 hu and 13 qian of grain, delivering it to a location 150 li away.
In total, the five counties are to deliver 10,000 hu of grain.
One cart carries 25 hu, and the transport cost is 1 qian per li.
It is desired to distribute the grain tax among the counties such that the labor cost is equalized.
Question: how much grain should each county deliver?

The procedure says: Multiply the transport cost per li by the distance to the delivery location.
Divide by the amount carried by one cart (25 hu), and add the cost of 1 hu of grain.
This gives the cost of delivering 1 hu of grain.
For each county, multiply this cost by the number of households to obtain the weight (衰).
The weights are: County A = 1026, County B = 684, County C = 399, County D = 494, County E = 270.
Sum the weights to obtain the divisor (法).
Multiply the total grain tax by the weights of each county to obtain the dividend (實).
Divide the dividend by the divisor to obtain the grain tax for each county.

Answer:
County A delivers *a*(=10260000/2873) hu.
County B delivers *b*(=6840000/2873) hu.
County C delivers *c*(=3990000/2873) hu.
County D delivers *d*(=380000/221) hu.
County E delivers *e*(=2700000/2873) hu.
"""

from fractions import Fraction

# Data for each county
counties = [
    {"households": 20520, "grain_cost": 120, "distance": 0},   # County A
    {"households": 12312, "grain_cost": 110, "distance": 200}, # County B
    {"households": 7182, "grain_cost": 112, "distance": 150},  # County C
    {"households": 13338, "grain_cost": 117, "distance": 250}, # County D
    {"households": 5130, "grain_cost": 113, "distance": 150},  # County E
]

# Constants
cart_capacity = 25  # One cart carries 25 hu
transport_cost_per_li = 1  # 1 qian per li
total_grain = 10000  # Total grain to be delivered

# Calculate weights (衰) for each county
for county in counties:
    transport_cost = (transport_cost_per_li * county["distance"]) / cart_capacity
    county["cost_per_hu"] = county["grain_cost"] + transport_cost
    county["weight"] = county["households"] * county["cost_per_hu"]

# Calculate the divisor (法)
法 = sum(county["weight"] for county in counties)

# Calculate the grain tax (實) for each county
for county in counties:
    county["grain"] = Fraction(total_grain * county["weight"], 法)

# Extract results
a = counties[0]["grain"]  # County A
b = counties[1]["grain"]  # County B
c = counties[2]["grain"]  # County C
d = counties[3]["grain"]  # County D
e = counties[4]["grain"]  # County E

# Results
a, b, c, d, e  # County A, B, C, D, E grain tax#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
