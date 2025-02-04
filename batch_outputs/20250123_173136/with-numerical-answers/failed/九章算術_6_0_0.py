"""
今有均輸粟：甲縣一萬戶，行道八日；乙縣九千五百戶，行道十日；丙縣一萬二千三百五十戶，行道十三日；丁縣一萬二千二百戶，行道二十日，各到輸所。凡四縣賦，當輸二十五萬斛，用車一萬乘。欲以道里遠近，戶數多少，衰出之。問︰粟、車各幾何？
均輸術曰：令縣戶數，各如其本行道日數而一，以為衰。甲衰一百二十五，乙、丙衰各九十五，丁衰六十一，副并為法。以賦粟、車數乘未并者，各自為實。實如法得一車。有分者，上下輩之。以二十五斛乘車數，即粟數。
荅曰：甲縣粟 a(=83100)斛 ，車 b(=3324)乘 。乙縣粟 c(=63175)斛 ，車 d(=2527)乘 。丙縣粟 e(=63175)斛 ，車 f(=2527)乘 。丁縣粟 g(=40550)斛 ，車 h(=1622)乘 。
"""

"""
Suppose there is a grain transportation task: 
County A has 10,000 households and takes 8 days to reach the destination.
County B has 9,500 households and takes 10 days to reach the destination.
County C has 12,350 households and takes 13 days to reach the destination.
County D has 12,200 households and takes 20 days to reach the destination.
All counties together are to transport 250,000 hu of grain using 10,000 carts.
It is desired to distribute the grain and carts proportionally based on the distance (days) and the number of households.

The procedure for equal transportation says: 
Let the number of households in each county be multiplied by the number of days it takes to reach the destination, and take this as the weight.
The weights for A, B, C, and D are 125, 95, 95, and 61 respectively. Add these together to form the divisor.
Multiply the total grain and cart numbers by the weights of each county to form the dividends.
Divide the dividends by the divisor to obtain the number of carts for each county.
For fractional results, round up or down as needed.
Multiply the number of carts by 25 hu (grain per cart) to get the grain amount.

Answer:
County A: *a*(=83100) hu of grain, *b*(=3324) carts.
County B: *c*(=63175) hu of grain, *d*(=2527) carts.
County C: *e*(=63175) hu of grain, *f*(=2527) carts.
County D: *g*(=40550) hu of grain, *h*(=1622) carts.
"""

from fractions import Fraction

# 各縣戶數和行道日數
甲戶數, 甲日數 = 10000, 8
乙戶數, 乙日數 = 9500, 10
丙戶數, 丙日數 = 12350, 13
丁戶數, 丁日數 = 12200, 20

# 賦粟總數和車總數
總粟數 = 250000
總車數 = 10000

# 令縣戶數，各如其本行道日數而一，以為衰
甲衰 = 甲戶數 * 甲日數
乙衰 = 乙戶數 * 乙日數
丙衰 = 丙戶數 * 丙日數
丁衰 = 丁戶數 * 丁日數

# 副并為法
法 = 甲衰 + 乙衰 + 丙衰 + 丁衰

# 以賦粟、車數乘未并者，各自為實
甲車實 = 總車數 * 甲衰
乙車實 = 總車數 * 乙衰
丙車實 = 總車數 * 丙衰
丁車實 = 總車數 * 丁衰

# 實如法得一車
甲車 = Fraction(甲車實, 法)
乙車 = Fraction(乙車實, 法)
丙車 = Fraction(丙車實, 法)
丁車 = Fraction(丁車實, 法)

# 以二十五斛乘車數，即粟數
甲粟 = 25 * 甲車
乙粟 = 25 *乙車
丙粟 =25
"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'
Missing variable in output: 'g'
Missing variable in output: 'h'"""
