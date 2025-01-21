"""
今有均輸卒甲縣一千二百人薄塞乙縣一千五百五十人行道一日丙縣一千二百八十人行道二日丁縣九百九十人行道三日戊縣一千七百五十人行道五日凡五縣賦輸卒一月一千二百人欲以遠近戶率多少衰出之問縣各幾何
術曰令縣卒各如其居所及行道日數而一以為衰甲衰四乙衰五丙衰四丁衰三戊衰五副并為法以人數乘未并者各自為實實如法而一有分者上下輩之
荅曰甲縣 a人 乙縣 b人 丙縣 c人 丁縣 d人 戊縣 e人 
"""

"""
Suppose there are conscripted laborers distributed among five counties:
- County Jia has 1200 people, traveling 1 day.
- County Yi has 1550 people, traveling 1 day.
- County Bing has 1280 people, traveling 2 days.
- County Ding has 990 people, traveling 3 days.
- County Wu has 1750 people, traveling 5 days.

In total, the five counties contribute 1200 people per month. It is desired to distribute the labor burden based on distance and household ratios.

The procedure says: Let the conscripted laborers in each county be weighted by their distance and travel days, with 1 as the base unit.
- Jia's weight is 4.
- Yi's weight is 5.
- Bing's weight is 4.
- Ding's weight is 3.
- Wu's weight is 5.
Add these weights together to form the divisor.
Multiply the total number of people by the uncombined weights for each county to form the dividend.
Divide each dividend by the divisor to get the result. If there are fractions, adjust them by rounding up or down.

The answer says: County Jia gets *a* people, County Yi gets *b* people, County Bing gets *c* people, County Ding gets *d* people, County Wu gets *e* people.
"""

# Define the weights (衰) for each county
甲衰 = 4
乙衰 = 5
丙衰 = 4
丁衰 = 3
戊衰 = 5

# Combine the weights to form the divisor (法)
法 = 甲衰 + 乙衰 + 丙衰 + 丁衰 + 戊衰

# Total number of people to distribute
總人數 = 1200

# Calculate the dividend (實) for each county
甲實 = 總人數 * 甲衰
乙實 = 總人數 * 乙衰
丙實 = 總人數 * 丙衰
丁實 = 總人數 * 丁衰
戊實 = 總人數 * 戊衰

# Divide each dividend by the divisor to get the result
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
