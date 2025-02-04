"""
今有均輸卒：甲縣一千二百人，薄塞；乙縣一千五百五十人，行道一日；丙縣一千二百八十人，行道二日；丁縣九百九十人，行道三日；戊縣一千七百五十人，行道五日。凡五縣，賦輸卒一月一千二百人。欲以遠近、戶率，多少衰出之。問︰縣各幾何？
術曰：令縣卒，各如其居所及行道日數而一，以為衰。甲衰四，乙衰五，丙衰四，丁衰三，戊衰五，副并為法。以人數乘未并者各自為實。實如法而一。有分者，上下輩之。
荅曰：甲縣 a人 。乙縣 b人 。丙縣 c人 。丁縣 d人 。戊縣 e人 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 各縣人數與行道日數
縣人數 = [1200, 1550, 1280, 990, 1750]
行道日數 = [0, 1, 2, 3, 5]

# 令縣卒，各如其居所及行道日數而一，以為衰
衰 = [4, 5, 4, 3, 5]

# 副并為法
法 = sum(衰)

# 以人數乘未并者各自為實
實 = [縣人數[i] * 衰[i] for i in range(len(縣人數))]

# 實如法而一
總輸卒 = 1200  # 每月輸卒總數
分配 = [Fraction(實[i], 法) * 總輸卒 for i in range(len(實))]

# 有分者，上下輩之
a = 分配[0]
b = 分配[1]
c = 分配[2]
d = 分配[3]
e = 分配[4]
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 229, Actual: 1920000/7
Variable 'b' has wrong value. Expected: 286, Actual: 3100000/7
Variable 'c' has wrong value. Expected: 228, Actual: 2048000/7
Variable 'd' has wrong value. Expected: 171, Actual: 1188000/7
Variable 'e' has wrong value. Expected: 286, Actual: 500000"""
