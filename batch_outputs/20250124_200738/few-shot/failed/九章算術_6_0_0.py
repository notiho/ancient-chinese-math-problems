"""
今有均輸粟：甲縣一萬戶，行道八日；乙縣九千五百戶，行道十日；丙縣一萬二千三百五十戶，行道十三日；丁縣一萬二千二百戶，行道二十日，各到輸所。凡四縣賦，當輸二十五萬斛，用車一萬乘。欲以道里遠近，戶數多少，衰出之。問︰粟、車各幾何？
均輸術曰：令縣戶數，各如其本行道日數而一，以為衰。甲衰一百二十五，乙、丙衰各九十五，丁衰六十一，副并為法。以賦粟、車數乘未并者，各自為實。實如法得一車。有分者，上下輩之。以二十五斛乘車數，即粟數。
荅曰：甲縣粟 a斛 ，車 b乘 。乙縣粟 c斛 ，車 d乘 。丙縣粟 e斛 ，車 f乘 。丁縣粟 g斛 ，車 h乘 。
"""

#----- content starts here -----
"""
Suppose there is a grain transportation task: 
County A has 10,000 households and takes 8 days to reach the destination.
County B has 9,500 households and takes 10 days to reach the destination.
County C has 12,350 households and takes 13 days to reach the destination.
County D has 12,200 households and takes 20 days to reach the destination.
The total grain to be transported is 250,000 hu, using 10,000 carts.
It is desired to distribute the grain and carts proportionally based on the distance and the number of households.

The procedure for equal transportation says: 
Let the number of households in each county be multiplied by the number of days they travel, to determine their weight (衰).
The weights are: County A = 125, County B = 95, County C = 95, County D = 61.
Add these weights together to form the divisor (法).
Multiply the total grain and cart numbers by the weights of each county to form the dividends (實).
Divide the dividends by the divisor to determine the number of carts for each county.
For any remainder, adjust by rounding up or down.
Multiply the number of carts by 25 hu to determine the amount of grain for each county.

Answer: County A transports *a* hu of grain using *b* carts.
County B transports *c* hu of grain using *d* carts.
County C transports *e* hu of grain using *f* carts.
County D transports *g* hu of grain using *h* carts.
"""

from fractions import Fraction

# 各縣戶數與行道日數
戶數 = [10000, 9500, 12350, 12200]
行道日數 = [8, 10, 13, 20]

# 賦粟與車總數
總粟 = 250000
總車 = 10000

# 令縣戶數，各如其本行道日數而一，以為衰
衰 = [戶數[i] * 行道日數[i] for i in range(4)]

# 副并為法
法 = sum(衰)

# 以賦粟、車數乘未并者，各自為實
粟實 = [總粟 * 衰[i] for i in range(4)]
車實 = [總車 * 衰[i] for i in range(4)]

# 實如法得一車
車數 = [Fraction(車實[i], 法) for i in range(4)]

# 以二十五斛乘車數，即粟數
粟數 = [25 * 車數[i] for i in range(4)]

# 解答
a, b = 粟數[0], 車數[0]
c, d = 粟數[1], 車數[1]
e, f = 粟數[2], 車數[2]
g, h = 粟數[3], 車數[3]#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 83100, Actual: 400000000/11591
Variable 'b' has wrong value. Expected: 3324, Actual: 16000000/11591
Variable 'c' has wrong value. Expected: 63175, Actual: 475000000/11591
Variable 'd' has wrong value. Expected: 2527, Actual: 19000000/11591
Variable 'e' has wrong value. Expected: 63175, Actual: 802750000/11591
Variable 'f' has wrong value. Expected: 2527, Actual: 32110000/11591
Variable 'g' has wrong value. Expected: 40550, Actual: 1220000000/11591
Variable 'h' has wrong value. Expected: 1622, Actual: 48800000/11591"""
