"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
Suppose there are five counties, each with a different number of households and distances to the delivery location. The goal is to distribute the total tax of 10,000 hu of millet among the counties such that the cost and labor are equalized.

The procedure says:
1. Multiply the cost per li of transport by the distance to the delivery location (in li).
2. Divide by the capacity of one cart (25 hu), then add the cost of one hu of millet. This gives the cost of delivering one hu of millet.
3. Multiply this cost by the number of households in each county to calculate the "weight" (衰) for each county.
4. Add up all the weights to form the divisor (法).
5. Multiply the total tax (10,000 hu) by the weight of each county to calculate the dividend (實).
6. Divide the dividend by the divisor to determine the amount of millet each county must deliver.

The answer says: County A delivers *a* hu, County B delivers *b* hu, County C delivers *c* hu, County D delivers *d* hu, and County E delivers *e* hu.
"""

from fractions import Fraction

# Data for each county
# Format: (households, cost per hu, distance to delivery location)
counties = {
    "甲": (20520, Fraction(120, 100), 200),
    "乙": (12312, Fraction(110, 100), 200),
    "丙": (7182, Fraction(112, 100), 150),
    "丁": (13338, Fraction(117, 100), 250),
    "戊": (5130, Fraction(113, 100), 150),
}

# Total tax to be distributed
total_tax = 10000

# Cart capacity and cost per li
cart_capacity = 25
cost_per_li = 1

# Step 1: Calculate the weight (衰) for each county
weights = {}
for county, (households, cost_per_hu, distance) in counties.items():
    # Calculate the cost of delivering one hu of millet
    delivery_cost = (cost_per_li * distance) / cart_capacity + cost_per_hu
    # Multiply by the number of households to get the weight
    weights[county] = households * delivery_cost

# Step 2: Calculate the divisor (法)
法 = sum(weights.values())

# Step 3: Calculate the amount of millet each county must deliver
results = {}
for county, weight in weights.items():
    results[county] = Fraction(total_tax * weight, 法)

# Assign results to variables
a = results["甲"]
b = results["乙"]
c = results["丙"]
d = results["丁"]
e = results["戊"]
"""
Code error: both arguments should be Rational instances"""
