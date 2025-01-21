"""
今有均輸粟甲縣一萬戶行道八日乙縣九千五百戶行道十日丙縣一萬二千三百五十戶行道十三日丁縣一萬二千二百戶行道二十日各到輸所凡四縣賦當輸二十五萬斛用車一萬乘欲以道里遠近戶數多少衰出之問粟車各幾何
均輸術曰令縣戶數各如其本行道日數而一以為衰甲衰一百二十五乙丙衰各九十五丁衰六十一副并為法以賦粟車數乘未并者各自為實實如法得一車有分者上下輩之以二十五斛乘車數即粟數
荅曰甲縣粟 a斛 車 b乘 乙縣粟 c斛 車 d乘 丙縣粟 e斛 車 f乘 丁縣粟 g斛 車 h乘 
"""

"""
Suppose there is a grain transportation task involving four counties:
- County Jia has 10,000 households and takes 8 days to reach the destination.
- County Yi has 9,500 households and takes 10 days to reach the destination.
- County Bing has 12,350 households and takes 13 days to reach the destination.
- County Ding has 12,200 households and takes 20 days to reach the destination.

The total grain to be transported is 250,000 hu, and 10,000 carts are available for transportation.
The task is to distribute the grain and carts proportionally based on the distance (days of travel) and the number of households in each county.

The procedure for equal transportation says:
- For each county, multiply the number of households by the number of travel days to calculate the "weight" (衰).
- For Jia, the weight is 125; for Yi and Bing, the weights are 95; and for Ding, the weight is 61.
- Add these weights together to form the divisor (法).
- Multiply the total grain and total carts by the weights of each county to calculate the "dividends" (實).
- Divide the dividends by the divisor to calculate the number of carts for each county.
- If there are fractional carts, adjust them by rounding up or down.
- Multiply the number of carts by 25 hu (the capacity of one cart) to calculate the grain for each county.

The answer says:
- County Jia: *a* hu of grain, *b* carts.
- County Yi: *c* hu of grain, *d* carts.
- County Bing: *e* hu of grain, *f* carts.
- County Ding: *g* hu of grain, *h* carts.
"""

from fractions import Fraction

# County data
甲戶數, 甲日數 = 10000, 8
乙戶數, 乙日數 = 9500, 10
丙戶數, 丙日數 = 12350, 13
丁戶數, 丁日數 = 12200, 20

# Total grain and carts
總粟 = 250000
總車 = 10000

# Calculate weights (衰)
甲衰 = 甲戶數 * 甲日數
乙衰 = 乙戶數 * 乙日數
丙衰 = 丙戶數 * 丙日數
丁衰 = 丁戶數 * 丁日數

# Add weights to form the divisor (法)
法 = 甲衰 + 乙衰 + 丙衰 + 丁衰

# Calculate dividends (實) for carts
甲車實 = 總車 * 甲衰
乙車實 = 總車 * 乙衰
丙車實 = 總車 * 丙衰
丁車實 = 總車 * 丁衰

# Calculate carts for each county
b = Fraction(甲車實, 法)
d = Fraction(乙車實, 法)
f = Fraction(丙車實, 法)
h = Fraction(丁車實, 法)

# Calculate grain for each county
a = b * 25
c = d * 25
e = f * 25
g = h * 25

# Results
a, b = a, b
c, d = c, d
e, f = e, f
g, h = g, h
"""
Variable 'a' has wrong value. Expected: 83100, Actual: 400000000/11591
Variable 'b' has wrong value. Expected: 3324, Actual: 16000000/11591
Variable 'c' has wrong value. Expected: 63175, Actual: 475000000/11591
Variable 'd' has wrong value. Expected: 2527, Actual: 19000000/11591
Variable 'e' has wrong value. Expected: 63175, Actual: 802750000/11591
Variable 'f' has wrong value. Expected: 2527, Actual: 32110000/11591
Variable 'g' has wrong value. Expected: 40550, Actual: 1220000000/11591
Variable 'h' has wrong value. Expected: 1622, Actual: 48800000/11591"""
