"""
今有十等人大官甲等十人官賜金依等次差降之上三人先入得金四斤持出下四人後入得金三斤持出中央三人未到者亦依等次更給問各得金㡬何及未到三人復應得金㡬何
術曰以先入人數分所持金數為上率以後入人數分所持金數為下率二率相減餘為差實併先後入人數而半之以減凡人數餘為差法實如法而一得差數倂一二三以差數乗之以減後入人所持金數餘以後入人數而一又置十人減一餘乗差數併之即第一人所得金數以次每減差數各得之矣并中央未到三人得應持金數
答曰甲 a斤 乙 b斤 丙 c斤 丁 d斤 戊 e斤 己 f斤 庚 g斤 辛 h斤 壬 i斤 癸 j斤 未到 k人 共得 l斤
"""

"""
Suppose there are 10 people ranked in 10 levels. The highest-ranked (甲等) has 10 people. Gold is distributed according to rank differences.
The first 3 people enter first and take out 4 jin of gold. The next 4 people enter later and take out 3 jin of gold. The middle 3 people have not yet arrived, but they will also be given gold according to rank differences.
Question: How much gold does each person receive, and how much gold should the 3 people who have not yet arrived receive?

The procedure says:
1. Divide the amount of gold taken by the first group by the number of people in the first group to get the upper rate.
2. Divide the amount of gold taken by the second group by the number of people in the second group to get the lower rate.
3. Subtract the lower rate from the upper rate to get the difference.
4. Add the number of people in the first and second groups, then halve it. Subtract this from the total number of people to get the difference divisor.
5. Use the difference divisor to divide the difference to get the difference value.
6. Add the difference value to 1, 2, 3, etc., and multiply by the difference value. Subtract this from the gold taken by the second group, then divide by the number of people in the second group.
7. Subtract 1 from the total number of people, multiply the result by the difference value, and add it to the gold taken by the first group to get the gold for the first person.
8. Subtract the difference value for each subsequent person to determine how much each receives.
9. Include the gold for the middle 3 people who have not yet arrived.

Answer: 甲 receives *a* jin, 乙 receives *b* jin, 丙 receives *c* jin, 丁 receives *d* jin, 戊 receives *e* jin, 己 receives *f* jin, 庚 receives *g* jin, 辛 receives *h* jin, 壬 receives *i* jin, 癸 receives *j* jin. The 3 people who have not yet arrived receive *k* people, and they collectively receive *l* jin.
"""

from fractions import Fraction

# 上三人先入得金四斤
先入人數 = 3
先入金數 = 4

# 下四人後入得金三斤
後入人數 = 4
後入金數 = 3

# 中央三人未到
未到人數 = 3

# 以先入人數分所持金數為上率
上率 = Fraction(先入金數, 先入人數)

# 以後入人數分所持金數為下率
下率 = Fraction(後入金數, 後入人數)

# 二率相減餘為差
差 = 上率 - 下率

# 實併先後入人數而半之
實 = (先入人數 + 後入人數) / 2

# 以減凡人數餘為差法
凡人數 = 10
差法 = 凡人數 - 實

# 實如法而一得差數
差數 = Fraction(差, 差法)

# 倂一二三以差數乗之以減後入人所持金數餘以後入人數而一
後入金餘 = 後入金數 - 差數 * sum(range(1, 後入人數 + 1))
後入金每人 = Fraction(後入金餘, 後入人數)

# 又置十人減一餘乗差數併之即第一人所得金數
第一人金數 = 先入金數 + (凡人數 - 1) * 差數

# 以次每減差數各得之矣
金數 = [第一人金數 - i * 差數 for i in range(凡人數)]

# 并中央未到三人得應持金數
未到金數 = sum(金數[先入人數:先入人數 + 未到人數])

# 答案
a, b, c, d, e, f, g, h, i, j = [金數[i] for i in range(10)]
k = 未到人數
l = 未到金數
"""
Code error: both arguments should be Rational instances"""
