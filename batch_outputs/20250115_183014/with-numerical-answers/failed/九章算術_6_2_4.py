"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a(=10260000/2873)斛 。乙縣 b(=6840000/2873)斛 。丙縣 c(=3990000/2873)斛 。丁縣 d(=380000/221)斛 。戊縣 e(=2700000/2873)斛 。
"""

"""
Suppose there is a tax distribution of millet among five counties:
- County A has 20,520 households, and the cost of millet is 1 hu and 20 qian per hu, transported within the county.
- County B has 12,312 households, and the cost of millet is 1 hu and 10 qian per hu, transported 200 li to the delivery location.
- County C has 7,182 households, and the cost of millet is 1 hu and 12 qian per hu, transported 150 li to the delivery location.
- County D has 13,338 households, and the cost of millet is 1 hu and 17 qian per hu, transported 250 li to the delivery location.
- County E has 5,130 households, and the cost of millet is 1 hu and 13 qian per hu, transported 150 li to the delivery location.

In total, the tax requires 10,000 hu of millet to be transported. A single cart carries 25 hu of millet, and the transportation cost is 1 qian per li. 
It is desired to distribute the millet among the counties such that the labor cost is equalized. 
Question: how much millet should each county contribute?

The procedure says: Multiply the transportation cost per li by the distance to the delivery location. Divide by the 25 hu carried by one cart, and add the cost of 1 hu of millet to obtain the cost of delivering 1 hu. 
For each county, multiply this cost by the number of households to obtain the "weight" (衰). 
The weights are:
- County A: 1026
- County B: 684
- County C: 399
- County D: 494
- County E: 270
Sum these weights to obtain the divisor (法). 
Multiply the total tax millet by each weight to obtain the dividend (實). 
Divide each dividend by the divisor to obtain the millet contribution for each county.

Answer:
- County A contributes *a*(=10260000/2873) hu.
- County B contributes *b*(=6840000/2873) hu.
- County C contributes *c*(=3990000/2873) hu.
- County D contributes *d*(=380000/221) hu.
- County E contributes *e*(=2700000/2873) hu.
"""

# Data for each county
戶數 = [20520, 12312, 7182, 13338, 5130]  # Households
粟價 = [120, 110, 112, 117, 113]  # Cost of 1 hu of millet in qian
距離 = [0, 200, 150, 250, 150]  # Distance to delivery location in li
載量 = 25  # Cart capacity in hu
僦價每里 = 1  # Transportation cost per li in qian
總賦粟 = 10000  # Total tax millet in hu

# Calculate the "weight" (衰) for each county
衰 = []
for i in range(len(戶數)):
    運費 = (僦價每里 * 距離[i]) / 載量  # Transportation cost per hu
    致費 = 運費 + 粟價[i]  # Total cost of delivering 1 hu
    衰.append(戶數[i] * 致費)

# 副并為法 (Sum weights to get the divisor)
法 = sum(衰)

# 所賦粟乘未并者，各自為實 (Calculate the dividend for each county)
實 = [總賦粟 * s for s in 衰]

# 實如法得一 (Divide each dividend by the divisor to get the millet contribution)
a, b, c, d, e = [Fraction(s, 法) for s in 實]  # Contributions for counties A, B, C, D, E

# Results:
# a = 10260000/2873
# b = 6840000/2873
# c = 3990000/2873
# d = 380000/221
# e = 2700000/2873
"""
Code error: both arguments should be Rational instances"""
