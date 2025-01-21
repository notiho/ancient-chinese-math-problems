"""
今有均輸卒：甲縣一千二百人，薄塞；乙縣一千五百五十人，行道一日；丙縣一千二百八十人，行道二日；丁縣九百九十人，行道三日；戊縣一千七百五十人，行道五日。凡五縣，賦輸卒一月一千二百人。欲以遠近、戶率，多少衰出之。問︰縣各幾何？
術曰：令縣卒，各如其居所及行道日數而一，以為衰。甲衰四，乙衰五，丙衰四，丁衰三，戊衰五，副并為法。以人數乘未并者各自為實。實如法而一。有分者，上下輩之。
荅曰：甲縣 a(=229)人 。乙縣 b(=286)人 。丙縣 c(=228)人 。丁縣 d(=171)人 。戊縣 e(=286)人 。
"""

"""
Suppose there are conscripted laborers for equal distribution:
County A has 1200 people, stationed at the border;
County B has 1550 people, traveling for 1 day;
County C has 1280 people, traveling for 2 days;
County D has 990 people, traveling for 3 days;
County E has 1750 people, traveling for 5 days.
In total, the five counties are to supply 1200 conscripted laborers per month.
It is desired to distribute the laborers proportionally according to distance and population.

The procedure says: Let the conscripted laborers of each county be proportional to their location and the number of days traveled, taking these as weights.
The weights are as follows: County A has a weight of 4, County B has a weight of 5, County C has a weight of 4, County D has a weight of 3, and County E has a weight of 5.
Add these weights together to form the divisor.
Multiply the total number of laborers by the weights of each county to form the dividends.
Divide the dividends by the divisor to obtain the number of laborers for each county.
If there are fractions, round them up or down as appropriate.

Answer: County A provides *a*(=229) people, County B provides *b*(=286) people, County C provides *c*(=228) people, County D provides *d*(=171) people, and County E provides *e*(=286) people.
"""

from fractions import Fraction

# 各縣人數
甲人數 = 1200
乙人數 = 1550
丙人數 = 1280
丁人數 = 990
戊人數 = 1750

# 各縣衰數
甲衰 = 4
乙衰 = 5
丙衰 = 4
丁衰 = 3
戊衰 = 5

# 副并為法
法 = 甲衰 + 乙衰 + 丙衰 + 丁衰 + 戊衰

# 賦輸卒總數
總輸卒 = 1200

# 以人數乘未并者各自為實
甲實 = 甲衰 * 總輸卒
乙實 = 乙衰 * 總輸卒
丙實 = 丙衰 * 總輸卒
丁實 = 丁衰 * 總輸卒
戊實 = 戊衰 * 總輸卒

# 實如法而一
a = round(Fraction(甲實, 法))  # 229
b = round(Fraction(乙實, 法))  # 286
c = round(Fraction(丙實, 法))  # 228
d = round(Fraction(丁實, 法))  # 171
e = round(Fraction(戊實, 法))  # 286
"""
Variable 'c' has wrong value. Expected: 228, Actual: 229"""
