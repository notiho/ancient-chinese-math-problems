"""
今有均輸粟：甲縣一萬戶，行道八日；乙縣九千五百戶，行道十日；丙縣一萬二千三百五十戶，行道十三日；丁縣一萬二千二百戶，行道二十日，各到輸所。凡四縣賦，當輸二十五萬斛，用車一萬乘。欲以道里遠近，戶數多少，衰出之。問︰粟、車各幾何？
均輸術曰：令縣戶數，各如其本行道日數而一，以為衰。甲衰一百二十五，乙、丙衰各九十五，丁衰六十一，副并為法。以賦粟、車數乘未并者，各自為實。實如法得一車。有分者，上下輩之。以二十五斛乘車數，即粟數。
荅曰：甲縣粟 a(=83100)斛 ，車 b(=3324)乘 。乙縣粟 c(=63175)斛 ，車 d(=2527)乘 。丙縣粟 e(=63175)斛 ，車 f(=2527)乘 。丁縣粟 g(=40550)斛 ，車 h(=1622)乘 。
"""

#----- content starts here -----
"""
Suppose there is a grain transport system: County A has 10,000 households and takes 8 days to reach the destination; County B has 9,500 households and takes 10 days; County C has 12,350 households and takes 13 days; County D has 12,200 households and takes 20 days. All counties deliver to the same destination. The total grain to be transported is 250,000 hu, using 10,000 carts. It is desired to distribute the grain and carts proportionally based on the distance and the number of households.

The procedure for equal transport says: Let the number of households in each county be multiplied by the number of days it takes to reach the destination. This gives the weight (衰) for each county. County A's weight is 125, County B's and County C's weights are 95 each, and County D's weight is 61. Add these weights together to form the divisor (法). Multiply the total grain and total carts by the weights of each county to form the dividends (實). Divide the dividends by the divisor to obtain the number of carts for each county. If there are fractions, adjust them up or down. Multiply the number of carts by 25 hu to obtain the amount of grain for each county.

Answer: County A delivers *a*(=83100) hu of grain using *b*(=3324) carts. County B delivers *c*(=63175) hu of grain using *d*(=2527) carts. County C delivers *e*(=63175) hu of grain using *f*(=2527) carts. County D delivers *g*(=40550) hu of grain using *h*(=1622) carts.
"""

from fractions import Fraction

# 各縣戶數與行道日數
甲戶數, 甲日數 = 10000, 8
乙戶數, 乙日數 = 9500, 10
丙戶數, 丙日數 = 12350, 13
丁戶數, 丁日數 = 12200, 20

# 賦粟與車總數
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

# 四舍五入取整
甲車 = round(甲車)
乙車 = round(乙車)
丙車 = round(丙車)
丁車 = round(丁車)

# 以二十五斛乘車數，即粟數
甲粟 = 25 * 甲車
乙粟 = 25 *乙車
丙粟 = 25丁#----- content ends here -----

"""
Code error: invalid decimal literal (<string>, line 52)"""
