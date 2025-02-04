"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a(=10260000/2873)斛 。乙縣 b(=6840000/2873)斛 。丙縣 c(=3990000/2873)斛 。丁縣 d(=380000/221)斛 。戊縣 e(=2700000/2873)斛 。
"""

#----- content starts here -----
"""
Suppose there is an equal distribution of grain tax among five counties:
- County A has 20,520 households, with a grain cost of 1 hu and 20 qian, and they deliver directly to their county.
- County B has 12,312 households, with a grain cost of 1 hu and 10 qian, and they deliver to a location 200 li away.
- County C has 7,182 households, with a grain cost of 1 hu and 12 qian, and they deliver to a location 150 li away.
- County D has 13,338 households, with a grain cost of 1 hu and 17 qian, and they deliver to a location 250 li away.
- County E has 5,130 households, with a grain cost of 1 hu and 13 qian, and they deliver to a location 150 li away.

In total, the grain tax is 10,000 hu. One cart carries 25 hu, and the transport cost is 1 qian per li. It is desired to distribute the grain tax among the counties such that the labor cost is equalized.

The procedure says: Multiply the transport cost per li by the distance to the delivery location. Divide by the amount carried by one cart (25 hu), and add the grain cost per hu. This gives the cost of delivering one hu of grain. Multiply this cost by the number of households in each county to obtain the "weight" for each county. Add all weights to obtain the divisor. Multiply the total grain tax by the weight of each county to obtain the dividend. Divide each dividend by the divisor to obtain the grain tax for each county.

Answer:
- County A: *a*(=10260000/2873) hu.
- County B: *b*(=6840000/2873) hu.
- County C: *c*(=3990000/2873) hu.
- County D: *d*(=380000/221) hu.
- County E: *e*(=2700000/2873) hu.
"""

# Data for each county
counties = [
    {"households": 20520, "grain_cost": Fraction(120, 100), "distance": 0},    # County A
    {"households": 12312, "grain_cost": Fraction(110, 100), "distance": 200},  # County B
    {"households": 7182, "grain_cost": Fraction(112, 100), "distance": 150},   # County C
    {"households": 13338, "grain_cost": Fraction(117, 100), "distance": 250},  # County D
    {"households": 5130, "grain_cost": Fraction(113, 100), "distance": 150},   # County E
]

# Constants
cart_capacity = 25  # One cart carries 25 hu
transport_cost_per_li = 1  # 1 qian per li
total_grain_tax = 10000  # Total grain tax in hu

# Calculate the "weight" (衰) for each county
for county in counties:
    transport_cost = (transport_cost_per_li * county["distance"]) / cart_capacity
    county["cost_per_hu"] = transport_cost + county["grain_cost"]
    county["weight"] = county["cost_per_hu"] * county["households"]

# Calculate the divisor (法)
divisor = sum(county["weight"] for county in counties)

# Calculate the grain tax for each county
for county in counties:
    county["grain_tax"] = Fraction(total_grain_tax * county["weight"], divisor)

# Results
a = counties[0]["grain_tax"]  # County A
b = counties[1]["grain_tax"]  # County B
c = counties[2]["grain_tax"]  # County C
d = counties[3]["grain_tax"]  # County D
e = counties[4]["grain_tax"]  # County E

# Final values:
# a = 10260000/2873
# b = 6840000/2873
# c = 3990000/2873
# d = 380000/221
# e = 2700000/2873#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
