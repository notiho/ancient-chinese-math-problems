"""
今有均輸卒：甲縣一千二百人，薄塞；乙縣一千五百五十人，行道一日；丙縣一千二百八十人，行道二日；丁縣九百九十人，行道三日；戊縣一千七百五十人，行道五日。凡五縣，賦輸卒一月一千二百人。欲以遠近、戶率，多少衰出之。問︰縣各幾何？
術曰：令縣卒，各如其居所及行道日數而一，以為衰。甲衰四，乙衰五，丙衰四，丁衰三，戊衰五，副并為法。以人數乘未并者各自為實。實如法而一。有分者，上下輩之。
荅曰：甲縣 a人 。乙縣 b人 。丙縣 c人 。丁縣 d人 。戊縣 e人 。
"""

"""
Suppose there are conscripted laborers for equalized transport duties:
County A has 1200 people, stationed at the frontier;
County B has 1550 people, traveling for 1 day;
County C has 1280 people, traveling for 2 days;
County D has 990 people, traveling for 3 days;
County E has 1750 people, traveling for 5 days.
In total, the five counties must provide 1200 laborers per month.
It is desired to distribute the laborers based on distance and household ratios, adjusting for more or less accordingly.
Question: how many laborers should each county provide?

The procedure says:
Let the laborers from each county be adjusted according to their location and the number of days they travel, assigning a weight for adjustment.
County A's weight is 4, County B's weight is 5, County C's weight is 4, County D's weight is 3, and County E's weight is 5.
Add these weights together to form the divisor.
Multiply the total number of laborers by the uncombined weights for each county to form the dividend.
Divide the dividend by the divisor to obtain the result for each county.
If there are fractions, round up or down as appropriate.

Answer: County A provides *a* people, County B provides *b* people, County C provides *c* people, County D provides *d* people, County E provides *e* people.
"""

# 各縣人數
甲人數 = 1200
乙人數 = 1550
丙人數 = 1280
丁人數 = 990
戊人數 = 1750

# 總輸卒
總輸卒 = 1200

# 各縣衰數
甲衰 = 4
乙衰 = 5
丙衰 = 4
丁衰 = 3
戊衰 = 5

# 副并為法
法 = 甲衰 + 乙衰 + 丙衰 + 丁衰 + 戊衰

# 以人數乘未并者各自為實
甲實 = 總輸卒 * 甲衰
乙實 = 總輸卒 * 乙衰
丙實 = 總輸卒 * 丙衰
丁實 = 總輸卒 * 丁衰
戊實 = 總輸卒 * 戊衰

# 實如法而一
a = Fraction(甲實, 法)
b = Fraction(乙實, 法)
c = Fraction(丙實, 法)
d = Fraction(丁實, 法)
e = Fraction(戊實, 法)
"""
Variable 'a' has wrong value. Expected: 229, Actual: 1600/7
Variable 'b' has wrong value. Expected: 286, Actual: 2000/7
Variable 'c' has wrong value. Expected: 228, Actual: 1600/7
Variable 'd' has wrong value. Expected: 171, Actual: 1200/7
Variable 'e' has wrong value. Expected: 286, Actual: 2000/7"""
