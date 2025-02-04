"""
今有均輸卒甲縣一千二百人薄塞乙縣一千五百五十人行道一日丙縣一千二百八十人行道二日丁縣九百九十人行道三日戊縣一千七百五十人行道五日凡五縣賦輸卒一月一千二百人欲以遠近戶率多少衰出之問縣各幾何
術曰令縣卒各如其居所及行道日數而一以為衰甲衰四乙衰五丙衰四丁衰三戊衰五副并為法以人數乘未并者各自為實實如法而一有分者上下輩之
荅曰甲縣 a人 乙縣 b人 丙縣 c人 丁縣 d人 戊縣 e人 
"""

#----- content starts here -----
"""
Suppose there are conscripted laborers distributed among five counties for transportation duties:
- County Jia has 1200 people and is 1 day away.
- County Yi has 1550 people and is 1 day away.
- County Bing has 1280 people and is 2 days away.
- County Ding has 990 people and is 3 days away.
- County Wu has 1750 people and is 5 days away.

In total, the five counties contribute 1200 people per month. It is desired to distribute the labor burden proportionally based on the distance and the number of households in each county.

The procedure says: Let the conscripted laborers in each county be weighted by their distance (in days) and the number of households, and take 1 as the base unit for each. This gives the weights:
- Jia: weight 4
- Yi: weight 5
- Bing: weight 4
- Ding: weight 3
- Wu: weight 5.
Sum these weights to obtain the divisor. Multiply the total number of people by the weights of each county to obtain the dividend for each county. Divide the dividend by the divisor to obtain the number of people for each county. If there are fractions, adjust them by distributing the remainder.

The answer says: County Jia gets *a* people, County Yi gets *b* people, County Bing gets *c* people, County Ding gets *d* people, and County Wu gets *e* people.
"""

# 縣卒數與行道日數
縣卒數 = [1200, 1550, 1280, 990, 1750]
行道日數 = [1, 1, 2, 3, 5]

# 各縣衰
衰 = [卒數 // 300 + 日數 for 卒數, 日數 in zip(縣卒數, 行道日數)]

# 副并為法
法 = sum(衰)

# 總人數
總人數 = 1200

# 以人數乘未并者各自為實
實 = [總人數 * 衰值 for 衰值 in 衰]

# 實如法而一
分配 = [Fraction(實值, 法) for 實值 in 實]

# 有分者上下輩之 (取整數部分)
a, b, c, d, e = [分數.numerator // 分數.denominator for 分數 in 分配]#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 229, Actual: 181
Variable 'b' has wrong value. Expected: 286, Actual: 218
Variable 'c' has wrong value. Expected: 228, Actual: 218
Variable 'd' has wrong value. Expected: 171, Actual: 218
Variable 'e' has wrong value. Expected: 286, Actual: 363"""
