"""
今有均輸粟甲縣一萬戶行道八日乙縣九千五百戶行道十日丙縣一萬二千三百五十戶行道十三日丁縣一萬二千二百戶行道二十日各到輸所凡四縣賦當輸二十五萬斛用車一萬乘欲以道里遠近戶數多少衰出之問粟車各幾何
均輸術曰令縣戶數各如其本行道日數而一以為衰甲衰一百二十五乙丙衰各九十五丁衰六十一副并為法以賦粟車數乘未并者各自為實實如法得一車有分者上下輩之以二十五斛乘車數即粟數
荅曰甲縣粟 a斛 車 b乘 乙縣粟 c斛 車 d乘 丙縣粟 e斛 車 f乘 丁縣粟 g斛 車 h乘 
"""

#----- content starts here -----
"""
Suppose there are four counties (甲, 乙, 丙, 丁) tasked with transporting grain to a central location. 
The details are as follows:
- County 甲 has 10,000 households and takes 8 days to reach the destination.
- County 乙 has 9,500 households and takes 10 days to reach the destination.
- County 丙 has 12,350 households and takes 13 days to reach the destination.
- County 丁 has 12,200 households and takes 20 days to reach the destination.

The total grain to be transported is 250,000 hu, using 10,000 carts. 
The task is to distribute the grain and carts proportionally based on the distance (days) and the number of households.

The procedure for equal transportation says:
- Multiply the number of households in each county by the number of days it takes to travel, and take this as the weight (衰).
- For 甲, the weight is 125; for 乙 and 丙, the weights are 95; and for 丁, the weight is 61.
- Add all the weights together to form the divisor (法).
- Multiply the total grain and cart numbers by the weights of each county to form the dividend (實).
- Divide the dividend by the divisor to determine the number of carts for each county.
- Multiply the number of carts by 25 hu (the capacity of one cart) to determine the amount of grain for each county.

The answer says:
- County 甲: *a* hu of grain, *b* carts.
- County 乙: *c* hu of grain, *d* carts.
- County 丙: *e* hu of grain, *f* carts.
- County 丁: *g* hu of grain, *h* carts.
"""

# County data
甲戶數 = 10000
甲日數 = 8

乙戶數 = 9500
乙日數 = 10

丙戶數 = 12350
丙日數 = 13

丁戶數 = 12200
丁日數 = 20

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

# Calculate carts for each county
甲車 = Fraction(總車 * 甲衰, 法)
乙車 = Fraction(總車 * 乙衰, 法)
丙車 = Fraction(總車 * 丙衰, 法)
丁車 = Fraction(總車 * 丁衰, 法)

# Calculate grain for each county
甲粟 = 甲車 * 25
乙粟 = 乙車 * 25
丙粟 = 丙車 * 25
丁粟 = 丁車 * 25

# Assign results
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
