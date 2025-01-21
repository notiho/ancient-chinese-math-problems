"""
今有均輸粟甲縣一萬戶行道八日乙縣九千五百戶行道十日丙縣一萬二千三百五十戶行道十三日丁縣一萬二千二百戶行道二十日各到輸所凡四縣賦當輸二十五萬斛用車一萬乘欲以道里遠近戶數多少衰出之問粟車各幾何
均輸術曰令縣戶數各如其本行道日數而一以為衰甲衰一百二十五乙丙衰各九十五丁衰六十一副并為法以賦粟車數乘未并者各自為實實如法得一車有分者上下輩之以二十五斛乘車數即粟數
荅曰甲縣粟 a斛 車 b乘 乙縣粟 c斛 車 d乘 丙縣粟 e斛 車 f乘 丁縣粟 g斛 車 h乘 
"""

"""
Suppose there are four counties transporting grain:
- County Jia has 10,000 households and takes 8 days to reach the destination.
- County Yi has 9,500 households and takes 10 days to reach the destination.
- County Bing has 12,350 households and takes 13 days to reach the destination.
- County Ding has 12,200 households and takes 20 days to reach the destination.

The total grain to be transported is 250,000 hu, using 10,000 carts. 
It is desired to distribute the grain and carts proportionally based on the distance (days) and the number of households.

The procedure for equal transportation says:
- Let the number of households in each county be multiplied by the number of days it takes to travel, and take this as the weight (衰).
- For Jia, the weight is 125; for Yi and Bing, the weights are 95 each; for Ding, the weight is 61.
- Add these weights together to form the divisor (法).
- Multiply the total grain and cart numbers by the weights of each county to form the dividends (實).
- Divide the dividends by the divisor to obtain the number of carts for each county.
- For fractional carts, round up or down to the nearest integer.
- Multiply the number of carts by 25 hu (the capacity of one cart) to obtain the grain for each county.

The answer says:
- County Jia: *a* hu of grain, *b* carts.
- County Yi: *c* hu of grain, *d* carts.
- County Bing: *e* hu of grain, *f* carts.
- County Ding: *g* hu of grain, *h* carts.
"""

from fractions import Fraction

# County data
戶數 = [10000, 9500, 12350, 12200]  # Households for Jia, Yi, Bing, Ding
行道日數 = [8, 10, 13, 20]  # Travel days for Jia, Yi, Bing, Ding

# Total grain and carts
總粟 = 250000  # Total grain in hu
總車 = 10000  # Total carts

# Step 1: Calculate weights (衰)
衰 = [戶數[i] * 行道日數[i] for i in range(4)]

# Step 2: Add weights to form the divisor (法)
法 = sum(衰)

# Step 3: Calculate dividends (實) for carts
車實 = [總車 * 衰[i] for i in range(4)]

# Step 4: Divide dividends by the divisor to get carts for each county
車數 = [Fraction(車實[i], 法) for i in range(4)]

# Step 5: Calculate grain for each county
粟數 = [25 * 車數[i] for i in range(4)]

# Extract results
a, b = 粟數[0], 車數[0]
c, d = 粟數[1], 車數[1]
e, f = 粟數[2], 車數[2]
g, h = 粟數[3], 車數[3]
"""
Variable 'a' has wrong value. Expected: 83100, Actual: 400000000/11591
Variable 'b' has wrong value. Expected: 3324, Actual: 16000000/11591
Variable 'c' has wrong value. Expected: 63175, Actual: 475000000/11591
Variable 'd' has wrong value. Expected: 2527, Actual: 19000000/11591
Variable 'e' has wrong value. Expected: 63175, Actual: 802750000/11591
Variable 'f' has wrong value. Expected: 2527, Actual: 32110000/11591
Variable 'g' has wrong value. Expected: 40550, Actual: 1220000000/11591
Variable 'h' has wrong value. Expected: 1622, Actual: 48800000/11591"""
