"""
今有均輸卒：甲縣一千二百人，薄塞；乙縣一千五百五十人，行道一日；丙縣一千二百八十人，行道二日；丁縣九百九十人，行道三日；戊縣一千七百五十人，行道五日。凡五縣，賦輸卒一月一千二百人。欲以遠近、戶率，多少衰出之。問︰縣各幾何？
術曰：令縣卒，各如其居所及行道日數而一，以為衰。甲衰四，乙衰五，丙衰四，丁衰三，戊衰五，副并為法。以人數乘未并者各自為實。實如法而一。有分者，上下輩之。
荅曰：甲縣 a人 。乙縣 b人 。丙縣 c人 。丁縣 d人 。戊縣 e人 。
"""

"""
This problem involves distributing a total of 1,200 conscripted workers among five counties (甲, 乙, 丙, 丁, 戊) based on their distance and the number of days they must travel. The distribution is weighted by the "衰" (decline factor), which is calculated based on the distance and travel days.

Here is the solution encoded in Python:


"""

#----- content starts here -----

from fractions import Fraction

# 人數 (population of each county)
甲 = 1200
乙 = 1550
丙 = 1280
丁 = 990
戊 = 1750

# 行道日數 (travel days for each county)
甲行道 = 1
乙行道 = 1
丙行道 = 2
丁行道 = 3
戊行道 = 5

# 衰 (decline factors for each county)
甲衰 = 甲行道 + 3  # 1 + 3 = 4
乙衰 = 乙行道 + 4  # 1 + 4 = 5
丙衰 = 丙行道 + 2  # 2 + 2 = 4
丁衰 = 丁行道      # 3
戊衰 = 戊行道      # 5

# 副并為法 (sum of decline factors as the divisor)
法 = 甲衰 + 乙衰 + 丙衰 + 丁衰 + 戊衰

# 總輸卒 (total conscripted workers)
總輸卒 = 1200

# 以人數乘未并者各自為實 (calculate the dividend for each county)
甲實 = 總輸卒 * 甲衰
乙實 = 總輸卒 * 乙衰
丙實 = 總輸卒 * 丙衰
丁實 = 總輸卒 * 丁衰
戊實 = 總輸卒 * 戊衰

# 實如法而一 (divide each dividend by the divisor to get the result for each county)
a = Fraction(甲實, 法)
b = Fraction(乙實, 法)
c = Fraction(丙實, 法)
d = Fraction(丁實, 法)
e = Fraction(戊實, 法)

# Output the results
print(f"甲縣: {a} 人")
print(f"乙縣: {b} 人")
print(f"丙縣: {c} 人")
print(f"丁縣: {d} 人")
print(f"戊縣: {e} 人")
#----- content ends here -----


"""


### Explanation of the Procedure:
1. **Calculate Decline Factors (衰):**
   Each county's decline factor is determined by adding a base value (depending on their distance and travel days). For example, 甲 has a decline factor of 4 because it has 1 travel day plus a base of 3.

2. **Sum of Decline Factors (法):**
   The total decline factor is the sum of all individual decline factors.

3. **Calculate Dividends (實):**
   Multiply the total number of conscripted workers (1,200) by each county's decline factor.

4. **Divide by the Total Decline Factor:**
   Divide each county's dividend by the total decline factor to determine the number of workers assigned to each county.

5. **Output Results:**
   The results are expressed as fractions to ensure precision.

### Final Answer:
The number of workers assigned to each county is:
- 甲縣: `a` 人
- 乙縣: `b` 人
- 丙縣: `c` 人
- 丁縣: `d` 人
- 戊縣: `e` 人
"""


"""
Variable 'a' has wrong value. Expected: 229, Actual: 1600/7
Variable 'b' has wrong value. Expected: 286, Actual: 2000/7
Variable 'c' has wrong value. Expected: 228, Actual: 1600/7
Variable 'd' has wrong value. Expected: 171, Actual: 1200/7
Variable 'e' has wrong value. Expected: 286, Actual: 2000/7"""
