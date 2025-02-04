"""
今有均輸粟甲縣一萬戶行道八日乙縣九千五百戶行道十日丙縣一萬二千三百五十戶行道十三日丁縣一萬二千二百戶行道二十日各到輸所凡四縣賦當輸二十五萬斛用車一萬乘欲以道里遠近戶數多少衰出之問粟車各幾何
均輸術曰令縣戶數各如其本行道日數而一以為衰甲衰一百二十五乙丙衰各九十五丁衰六十一副并為法以賦粟車數乘未并者各自為實實如法得一車有分者上下輩之以二十五斛乘車數即粟數
荅曰甲縣粟 a斛 車 b乘 乙縣粟 c斛 車 d乘 丙縣粟 e斛 車 f乘 丁縣粟 g斛 車 h乘 
"""

#----- content starts here -----
"""
Suppose there are four counties transporting grain to a central location:
- County A has 10,000 households and takes 8 days to travel.
- County B has 9,500 households and takes 10 days to travel.
- County C has 12,350 households and takes 13 days to travel.
- County D has 12,200 households and takes 20 days to travel.
The total grain to be transported is 250,000 hu, using 10,000 carts.
Question: How much grain and how many carts should each county contribute, considering the distance and household count?

The procedure for equal transportation says:
- Let the household count of each county be multiplied by its travel days, and take this as the weight (衰).
- For County A, the weight is 125; for Counties B and C, the weights are 95 each; and for County D, the weight is 61.
- Add these weights together to form the divisor (法).
- Multiply the total grain and cart count by the weights of each county to form the dividends (實).
- Divide the dividends by the divisor to determine the number of carts for each county.
- For fractional carts, adjust the grain amount by multiplying the cart count by 25 hu per cart.

The answer says:
- County A: *a* hu of grain, *b* carts.
- County B: *c* hu of grain, *d* carts.
- County C: *e* hu of grain, *f* carts.
- County D: *g* hu of grain, *h* carts.
"""

# 各縣戶數和行道日數
甲戶數, 甲日數 = 10000, 8
乙戶數, 乙日數 = 9500, 10
丙戶數, 丙日數 = 12350, 13
丁戶數, 丁日數 = 12200, 20

# 賦粟總數和車總數
總粟 = 250000
總車 = 10000

# 令縣戶數各如其本行道日數而一以為衰
甲衰 = 甲戶數 * 甲日數
乙衰 = 乙戶數 * 乙日數
丙衰 = 丙戶數 * 丙日數
丁衰 = 丁戶數 * 丁日數

# 副并為法
法 = 甲衰 + 乙衰 + 丙衰 + 丁衰

# 以賦粟車數乘未并者各自為實
甲車實 = 總車 * 甲衰
乙車實 = 總車 * 乙衰
丙車實 = 總車 * 丙衰
丁車實 = 總車 * 丁衰

# 實如法得一車
甲車 = Fraction(甲車實, 法)
乙車 = Fraction(乙車實, 法)
丙車 = Fraction(丙車實, 法)
丁車 = Fraction(丁車實, 法)

# 以二十五斛乘車數即粟數
甲粟 = 25 * 甲車
乙粟 = 25 * 乙車
丙粟 = 25 * 丙車
丁粟 = 25 * 丁車

# 答案
a, b = 甲粟, 甲車
c, d = 乙粟, 乙車
e, f = 丙粟, 丙車
g, h = 丁粟, 丁車#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 83100, Actual: 400000000/11591
Variable 'b' has wrong value. Expected: 3324, Actual: 16000000/11591
Variable 'c' has wrong value. Expected: 63175, Actual: 475000000/11591
Variable 'd' has wrong value. Expected: 2527, Actual: 19000000/11591
Variable 'e' has wrong value. Expected: 63175, Actual: 802750000/11591
Variable 'f' has wrong value. Expected: 2527, Actual: 32110000/11591
Variable 'g' has wrong value. Expected: 40550, Actual: 1220000000/11591
Variable 'h' has wrong value. Expected: 1622, Actual: 48800000/11591"""
