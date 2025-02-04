"""
今有均輸粟甲縣一萬戶行道八日乙縣九千五百戶行道十日丙縣一萬二千三百五十戶行道十三日丁縣一萬二千二百戶行道二十日各到輸所凡四縣賦當輸二十五萬斛用車一萬乘欲以道里遠近戶數多少衰出之問粟車各幾何
均輸術曰令縣戶數各如其本行道日數而一以為衰甲衰一百二十五乙丙衰各九十五丁衰六十一副并為法以賦粟車數乘未并者各自為實實如法得一車有分者上下輩之以二十五斛乘車數即粟數
荅曰甲縣粟 a斛 車 b乘 乙縣粟 c斛 車 d乘 丙縣粟 e斛 車 f乘 丁縣粟 g斛 車 h乘 
"""

"""
Suppose there are four counties, each with a different number of households and distances to the delivery location. The total tax grain to be delivered is 250,000 hu, using 10,000 carts. The grain and carts should be distributed proportionally based on the distance and the number of households in each county.

The procedure for equal distribution says: Let the number of households in each county remain as they are, and multiply them by the number of travel days. Use these as the weights (衰). 
For County A, the weight is 125. For Counties B and C, the weights are 95 each. For County D, the weight is 61.
Add these weights together to form the divisor (法). Multiply the total grain and cart numbers by the weights of each county to form the dividends (實). Divide the dividends by the divisor to obtain the number of carts for each county. If there are fractional carts, round up or down to the nearest integer. Multiply the number of carts by 25 hu (the capacity of one cart) to obtain the grain amount.

The answer says: County A delivers *a* hu of grain using *b* carts. County B delivers *c* hu of grain using *d* carts. County C delivers *e* hu of grain using *f* carts. County D delivers *g* hu of grain using *h* carts.
"""

from fractions import Fraction

# 各縣戶數和行道日數
甲戶數, 甲日數 = 10000, 8
乙戶數, 乙日數 = 9500, 10
丙戶數, 丙日數 = 12350, 13
丁戶數, 丁日數 = 12200, 20

# 賦粟總數和車總數
賦粟總數 = 250000
車總數 = 10000

# 令縣戶數各如其本行道日數而一以為衰
甲衰 = 甲戶數 * 甲日數
乙衰 = 乙戶數 * 乙日數
丙衰 = 丙戶數 * 丙日數
丁衰 = 丁戶數 * 丁日數

# 副并為法
法 = 甲衰 + 乙衰 + 丙衰 + 丁衰

# 以賦粟車數乘未并者各自為實
甲車實 = 車總數 * 甲衰
乙車實 = 車總數 * 乙衰
丙車實 = 車總數 * 丙衰
丁車實 = 車總數 * 丁衰

# 實如法得一車
甲車 = Fraction(甲車實, 法)
乙車 = Fraction(乙車實, 法)
丙車 = Fraction(丙車實, 法)
丁車 = Fraction(丁車實, 法)

# 有分者上下輩之 (round to nearest integer)
甲車 = round(甲車)
乙車 = round(乙車)
丙車 = round(丙車)
丁車 = round(丁車)

# 以二十五斛乘車數即粟數
甲粟 = 25 * 甲車
乙粟 = 25 *乙車
丙粟 =25丁car
"""
Code error: invalid decimal literal (<string>, line 54)"""
