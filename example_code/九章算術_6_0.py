#今有均輸粟甲縣一萬戸行道八日乙縣九千五百戸行道十日丙縣一萬二千三百五十戸行道十三日丁縣一萬二千二百戸行道二十日各到輸所凡四縣賦當輸二十五萬斛用車一萬乘欲以道里遠近戸數多少衰出之問粟車各幾何
#均輸術曰令縣戸數各如其本行道日數而一以爲衰甲衰一百二十五乙丙衰各九十五丁衰六十一副并爲法以賦粟車數乘未并者各自爲實實如法得一車有分者上下軰之以二十五斛乘車數卽粟數
#荅曰甲縣粟 a斛 車 b乘 乙縣粟 c斛 車 d乘 丙縣粟 e斛 車 f乘 丁縣粟 g斛 車 h乘

from fractions import Fraction

# 甲縣一萬戸行道八日乙縣九千五百戸行道十日丙縣一萬二千三百五十戸行道十三日丁縣一萬二千二百戸行道二十日
戸數 = [10000, 9500, 12350, 12200]
行道日數 = [8, 10, 13, 20]

# 用車一萬乘
車數 = 10000

# 令縣戸數各如其本行道日數而一爲衰
衰 = [Fraction(x, y) for x, y in zip(戸數, 行道日數)]

# 副并爲法
法 = sum(衰)

# 以賦粟車數乘未并者各自爲實
實 = [車數 * x for x in 衰]

# 實如法得一車
一車 = [x / 法 for x in 實]

# 有分者上下軰之
fractional_parts = [x - x.__floor__() for x in 一車]
if fractional_parts[0] > 0:
	fractional_parts[1] += fractional_parts[0]
	fractional_parts[0] = 0
if fractional_parts[1] - fractional_parts[1].__floor__() > 0:
	fractional_parts[2] += fractional_parts[1] - fractional_parts[1].__floor__()
	fractional_parts[1] = fractional_parts[1].__floor__()
if fractional_parts[3] > 0:
	fractional_parts[2] += fractional_parts[3]
	fractional_parts[3] = 0

一車 = [x.__floor__() + y for x, y in zip(一車, fractional_parts)]

b = 一車[0]
d = 一車[1]
f = 一車[2]
h = 一車[3]

# 以二十五斛乘車數卽粟數
a = 25 * b
c = 25 * d
e = 25 * f
g = 25 * h
