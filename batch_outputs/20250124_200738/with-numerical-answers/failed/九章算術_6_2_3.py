"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a(=10260000/2873)斛 。乙縣 b(=6840000/2873)斛 。丙縣 c(=3990000/2873)斛 。丁縣 d(=380000/221)斛 。戊縣 e(=2700000/2873)斛 。
"""

#----- content starts here -----
"""
Suppose there is an equal distribution of grain tax among counties:
County A has 20,520 households, and the grain tax is 1 hu and 20 qian per household, delivered to its own county.
County B has 12,312 households, and the grain tax is 1 hu and 10 qian per household, delivered 200 li to the delivery location.
County C has 7,182 households, and the grain tax is 1 hu and 12 qian per household, delivered 150 li to the delivery location.
County D has 13,338 households, and the grain tax is 1 hu and 17 qian per household, delivered 250 li to the delivery location.
County E has 5,130 households, and the grain tax is 1 hu and 13 qian per household, delivered 150 li to the delivery location.

In total, the five counties must deliver 10,000 hu of grain. One cart carries 25 hu, and the cart rental cost is 1 qian per li.
It is desired to distribute the grain tax among the counties such that the transportation costs are equalized.
Question: how much grain does each county deliver?

The procedure says:
Take the cart rental cost per li, multiply it by the distance to the delivery location, and divide by the 25 hu carried by one cart.
Add the grain tax cost per hu to obtain the total cost per hu.
For each county, multiply this cost by the number of households to obtain the "weight" (衰).
The weights for each county are:
- County A: 1,026
- County B: 684
- County C: 399
- County D: 494
- County E: 270
Sum these weights to obtain the divisor (法).
Multiply the total grain tax by the weights (未并者) to obtain the dividend (實) for each county.
Divide the dividend by the divisor to obtain the grain tax for each county.

Answer:
- County A delivers *a*(=10260000/2873) hu.
- County B delivers *b*(=6840000/2873) hu.
- County C delivers *c*(=3990000/2873) hu.
- County D delivers *d*(=380000/221) hu.
- County E delivers *e*(=2700000/2873) hu.
"""

# 一車載二十五斛，與僦一里一錢
車載 = 25
僦價每里 = 1

# 各縣數據
縣數據 = {
    "甲": {"戶數": 20520, "粟價": 120, "距離": 0},
    "乙": {"戶數": 12312, "粟價": 110, "距離": 200},
    "丙": {"戶數": 7182, "粟價": 112, "距離": 150},
    "丁": {"戶數": 13338, "粟價": 117, "距離": 250},
    "戊": {"戶數": 5130, "粟價": 113, "距離": 150},
}

# 總輸粟
總粟 = 10000

# 計算各縣的衰
縣衰 = {}
for 縣, 數據 in 縣數據.items():
    戶數 = 數據["戶數"]
    粟價 = 數據["粟價"]
    距離 = 數據["距離"]
    致一斛費 = 粟價 + (僦價每里 * 距離) / 車載
    縣衰[縣] = 戶數 * 致一斛費

# 副并為法
法 = sum(縣衰.values())

# 所賦粟乘未并者，各自為實
縣實 = {縣: 縣衰[縣] * 總粟 for 縣 in 縣衰}

# 實如法得一
縣粟 = {縣: Fraction(實, 法) for 縣, 實 in 縣實.items()}

# 結果
a = 縣粟["甲"]  # 10260000/2873
b = 縣粟["乙"]  # 6840000/2873
c = 縣粟["丙"]  # 3990000/2873
d = 縣粟["丁"]  # 380000/221
e = 縣粟["戊"]  # 2700000/2873#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
