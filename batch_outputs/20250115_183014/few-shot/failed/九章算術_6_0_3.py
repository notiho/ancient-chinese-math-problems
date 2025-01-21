"""
今有均輸粟：甲縣一萬戶，行道八日；乙縣九千五百戶，行道十日；丙縣一萬二千三百五十戶，行道十三日；丁縣一萬二千二百戶，行道二十日，各到輸所。凡四縣賦，當輸二十五萬斛，用車一萬乘。欲以道里遠近，戶數多少，衰出之。問︰粟、車各幾何？
均輸術曰：令縣戶數，各如其本行道日數而一，以為衰。甲衰一百二十五，乙、丙衰各九十五，丁衰六十一，副并為法。以賦粟、車數乘未并者，各自為實。實如法得一車。有分者，上下輩之。以二十五斛乘車數，即粟數。
荅曰：甲縣粟 a斛 ，車 b乘 。乙縣粟 c斛 ，車 d乘 。丙縣粟 e斛 ，車 f乘 。丁縣粟 g斛 ，車 h乘 。
"""

"""
Suppose there is a grain transport task: 
County A has 10,000 households and takes 8 days to reach the delivery location.
County B has 9,500 households and takes 10 days to reach the delivery location.
County C has 12,350 households and takes 13 days to reach the delivery location.
County D has 12,200 households and takes 20 days to reach the delivery location.
The total grain to be delivered by the four counties is 250,000 hu, using 10,000 carts.
It is desired to distribute the grain and carts based on the distance (days) and the number of households in each county.

The procedure for equal transport says: 
Let the number of households in each county be multiplied by the number of days it takes to reach the delivery location, forming the "weight" (衰).
The weights for County A, B, C, and D are 125, 95, 95, and 61, respectively.
Add these weights together to form the divisor (法).
Multiply the total grain and total carts by the weights of each county to form the dividends (實).
Divide the dividends by the divisor to obtain the number of carts for each county.
If there is a remainder, adjust the result by rounding up or down.
Multiply the number of carts by 25 hu to obtain the amount of grain for each county.

Answer: County A delivers *a* hu of grain using *b* carts.
County B delivers *c* hu of grain using *d* carts.
County C delivers *e* hu of grain using *f* carts.
County D delivers *g* hu of grain using *h* carts.
"""

# 各縣戶數和行道日數
甲戶數, 甲日數 = 10000, 8
乙戶數, 乙日數 = 9500, 10
丙戶數, 丙日數 = 12350, 13
丁戶數, 丁日數 = 12200, 20

# 賦粟和車數
總粟 = 250000
總車 = 10000

# 令縣戶數，各如其本行道日數而一，以為衰
甲衰 = 甲戶數 * 甲日數
乙衰 = 乙戶數 * 乙日數
丙衰 = 丙戶數 * 丙日數
丁衰 = 丁戶數 * 丁日數

# 副并為法
法 = 甲衰 + 乙衰 + 丙衰 + 丁衰

# 以賦粟、車數乘未并者，各自為實
甲車實 = 總車 * 甲衰
乙車實 = 總車 * 乙衰
丙車實 = 總車 * 丙衰
丁車實 = 總車 * 丁衰

# 實如法得一車
甲車 = Fraction(甲車實, 法)
乙車 = Fraction(乙車實, 法)
丙車 = Fraction(丙車實, 法)
丁車 = Fraction(丁車實, 法)

# 以二十五斛乘車數，即粟數
甲粟 = 25 * 甲車
乙粟 = 25 * 乙車
丙粟 = 25 * 丙車
丁粟 = 25 * 丁車

# 答案
a, b = 甲粟, 甲車
c, d = 乙粟, 乙車
e, f = 丙粟, 丙車
g, h = 丁粟, 丁車
"""
Variable 'a' has wrong value. Expected: 83100, Actual: 400000000/11591
Variable 'b' has wrong value. Expected: 3324, Actual: 16000000/11591
Variable 'c' has wrong value. Expected: 63175, Actual: 475000000/11591
Variable 'd' has wrong value. Expected: 2527, Actual: 19000000/11591
Variable 'e' has wrong value. Expected: 63175, Actual: 802750000/11591
Variable 'f' has wrong value. Expected: 2527, Actual: 32110000/11591
Variable 'g' has wrong value. Expected: 40550, Actual: 1220000000/11591
Variable 'h' has wrong value. Expected: 1622, Actual: 48800000/11591"""
