"""
今有均輸粟：甲縣一萬戶，行道八日；乙縣九千五百戶，行道十日；丙縣一萬二千三百五十戶，行道十三日；丁縣一萬二千二百戶，行道二十日，各到輸所。凡四縣賦，當輸二十五萬斛，用車一萬乘。欲以道里遠近，戶數多少，衰出之。問︰粟、車各幾何？
均輸術曰：令縣戶數，各如其本行道日數而一，以為衰。甲衰一百二十五，乙、丙衰各九十五，丁衰六十一，副并為法。以賦粟、車數乘未并者，各自為實。實如法得一車。有分者，上下輩之。以二十五斛乘車數，即粟數。
荅曰：甲縣粟 a斛 ，車 b乘 。乙縣粟 c斛 ，車 d乘 。丙縣粟 e斛 ，車 f乘 。丁縣粟 g斛 ，車 h乘 。
"""

#----- content starts here -----
"""
Suppose there is a grain transport system involving four counties:

- County A has 10,000 households and takes 8 days to reach the delivery location.
- County B has 9,500 households and takes 10 days to reach the delivery location.
- County C has 12,350 households and takes 13 days to reach the delivery location.
- County D has 12,200 households and takes 20 days to reach the delivery location.

The total grain to be transported is 250,000 hu, using 10,000 carts. The goal is to distribute the grain and carts proportionally based on the distance (days) and the number of households in each county.

The procedure for equal transport says:
1. Multiply the number of households in each county by the number of days it takes to reach the delivery location. This gives the "weight" (衰) for each county.
2. Add all the weights together to get the divisor (法).
3. Multiply the total grain and total carts by the weight of each county to get the dividend (實) for each county.
4. Divide the dividend by the divisor to get the number of carts for each county.
5. Multiply the number of carts by 25 hu (the amount of grain per cart) to get the amount of grain for each county.

The answer says:
- County A gets *a* hu of grain and *b* carts.
- County B gets *c* hu of grain and *d* carts.
- County C gets *e* hu of grain and *f* carts.
- County D gets *g* hu of grain and *h* carts.
"""

from fractions import Fraction

# Data for each county
counties = {
    "A": {"households": 10000, "days": 8},
    "B": {"households": 9500, "days": 10},
    "C": {"households": 12350, "days": 13},
    "D": {"households": 12200, "days": 20},
}

# Total grain and carts
total_grain = 250000  # hu
total_carts = 10000

# Step 1: Calculate weights (衰) for each county
for county, data in counties.items():
    data["weight"] = data["households"] * data["days"]

# Step 2: Calculate the divisor (法)
法 = sum(data["weight"] for data in counties.values())

# Step 3: Calculate the number of carts (車) for each county
for county, data in counties.items():
    data["carts"] = Fraction(data["weight"] * total_carts, 法)

# Step 4: Calculate the amount of grain (粟) for each county
for county, data in counties.items():
    data["grain"] = data["carts"] * 25

# Extract results
a, b = counties["A"]["grain"], counties["A"]["carts"]
c, d = counties["B"]["grain"], counties["B"]["carts"]
e, f = counties["C"]["grain"], counties["C"]["carts"]
g, h = counties["D"]["grain"], counties["D"]["carts"]#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 83100, Actual: 400000000/11591
Variable 'b' has wrong value. Expected: 3324, Actual: 16000000/11591
Variable 'c' has wrong value. Expected: 63175, Actual: 475000000/11591
Variable 'd' has wrong value. Expected: 2527, Actual: 19000000/11591
Variable 'e' has wrong value. Expected: 63175, Actual: 802750000/11591
Variable 'f' has wrong value. Expected: 2527, Actual: 32110000/11591
Variable 'g' has wrong value. Expected: 40550, Actual: 1220000000/11591
Variable 'h' has wrong value. Expected: 1622, Actual: 48800000/11591"""
