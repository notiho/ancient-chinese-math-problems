"""
今有均輸粟：甲縣一萬戶，行道八日；乙縣九千五百戶，行道十日；丙縣一萬二千三百五十戶，行道十三日；丁縣一萬二千二百戶，行道二十日，各到輸所。凡四縣賦，當輸二十五萬斛，用車一萬乘。欲以道里遠近，戶數多少，衰出之。問︰粟、車各幾何？
均輸術曰：令縣戶數，各如其本行道日數而一，以為衰。甲衰一百二十五，乙、丙衰各九十五，丁衰六十一，副并為法。以賦粟、車數乘未并者，各自為實。實如法得一車。有分者，上下輩之。以二十五斛乘車數，即粟數。
荅曰：甲縣粟 a斛 ，車 b乘 。乙縣粟 c斛 ，車 d乘 。丙縣粟 e斛 ，車 f乘 。丁縣粟 g斛 ，車 h乘 。
"""

"""

"""


from fractions import Fraction

# 各縣戶數與行道日數
縣戶數 = [10000, 9500, 12350, 12200]
行道日數 = [8, 10, 13, 20]

# 賦粟總數與車總數
總粟數 = 250000
總車數 = 10000

# 令縣戶數，各如其本行道日數而一，以為衰
衰 = [戶數 * 日數 for 戶數, 日數 in zip(縣戶數, 行道日數)]

# 副并為法
法 = sum(衰)

# 以賦粟、車數乘未并者，各自為實
粟實 = [總粟數 * s for s in 衰]
車實 = [總車數 * s for s in 衰]

# 實如法得一車
車數 = [Fraction(實, 法) for 實 in 車實]

# 有分者，上下輩之
車數 = [round(車) for 車 in 車數]

# 以二十五斛乘車數，即粟數
粟數 = [25 * 車 for 車 in 車數]

# 結果
a, b = 粟數[0], 車數[0]
c, d = 粟數[1], 車數[1]
e, f = 粟數[2], 車數[2]
g, h = 粟數[3], 車數[3]


"""

"""


"""
Variable 'a' has wrong value. Expected: 83100, Actual: 34500
Variable 'b' has wrong value. Expected: 3324, Actual: 1380
Variable 'c' has wrong value. Expected: 63175, Actual: 40975
Variable 'd' has wrong value. Expected: 2527, Actual: 1639
Variable 'e' has wrong value. Expected: 63175, Actual: 69250
Variable 'f' has wrong value. Expected: 2527, Actual: 2770
Variable 'g' has wrong value. Expected: 40550, Actual: 105250
Variable 'h' has wrong value. Expected: 1622, Actual: 4210"""
