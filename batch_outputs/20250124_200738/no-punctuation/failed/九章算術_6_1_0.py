"""
今有均輸卒甲縣一千二百人薄塞乙縣一千五百五十人行道一日丙縣一千二百八十人行道二日丁縣九百九十人行道三日戊縣一千七百五十人行道五日凡五縣賦輸卒一月一千二百人欲以遠近戶率多少衰出之問縣各幾何
術曰令縣卒各如其居所及行道日數而一以為衰甲衰四乙衰五丙衰四丁衰三戊衰五副并為法以人數乘未并者各自為實實如法而一有分者上下輩之
荅曰甲縣 a人 乙縣 b人 丙縣 c人 丁縣 d人 戊縣 e人 
"""

#----- content starts here -----
"""
Suppose there are conscripted laborers distributed among five counties:
- County Jia has 1200 people, traveling 1 day.
- County Yi has 1550 people, traveling 1 day.
- County Bing has 1280 people, traveling 2 days.
- County Ding has 990 people, traveling 3 days.
- County Wu has 1750 people, traveling 5 days.

In total, the five counties need to provide 1200 people per month. 
It is desired to distribute the labor based on the distance and the number of households in each county.

The procedure says: Let the conscripted laborers in each county be weighted according to their location and the number of days they travel, taking 1 as the base.
This gives the weights:
- Jia weight = 4
- Yi weight = 5
- Bing weight = 4
- Ding weight = 3
- Wu weight = 5

Add these weights together to form the divisor. Multiply the total number of people by the uncombined weights for each county to form the dividend. Divide the dividend by the divisor to get the result. If there are fractions, adjust them by distributing the remainder.

Answer: County Jia provides *a* people, County Yi provides *b* people, County Bing provides *c* people, County Ding provides *d* people, County Wu provides *e* people.
"""

# 人數和行道日數
縣人數 = [1200, 1550, 1280, 990, 1750]
行道日數 = [1, 1, 2, 3, 5]

# 各縣衰
衰 = [人數 + 日數 for 人數, 日數 in zip(行道日數, [3,4....#----- content ends here -----

"""
Code error: '[' was never closed (<string>, line 31)"""
