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
衰 = [4, 5, 4, 3, 5]  # 甲衰4，乙衰5，丙衰4，丁衰3，戊衰5

# 副并為法
法 = sum(衰)

# 以人數乘未并者各自為實
實 = [人數 * 衰值 for 人數, 衰值 in zip(縣人數, 衰)]

# 實如法而一
總輸卒 = 1200  # 一月輸卒總數
分配 = [Fraction(實值, 法) * 總輸卒 for 實值 in 實]

# 有分者，上下輩之
a, b, c, d, e = [round(分) for 分 in 分配]

# 結果
print(f"甲縣 {a}人。乙縣 {b}人。丙縣 {c}人。丁縣 {d}人。戊縣 {e}人。")
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 229, Actual: 274286
Variable 'b' has wrong value. Expected: 286, Actual: 442857
Variable 'c' has wrong value. Expected: 228, Actual: 292571
Variable 'd' has wrong value. Expected: 171, Actual: 169714
Variable 'e' has wrong value. Expected: 286, Actual: 500000"""
