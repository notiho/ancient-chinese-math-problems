"""
今有十等人大官甲等十人官賜金依等次差降之上三人先入得金四斤持出下四人後入得金三斤持出中央三人未到者亦依等次更給問各得金㡬何及未到三人復應得金㡬何
術曰以先入人數分所持金數為上率以後入人數分所持金數為下率二率相減餘為差實併先後入人數而半之以減凡人數餘為差法實如法而一得差數倂一二三以差數乗之以減後入人所持金數餘以後入人數而一又置十人減一餘乗差數併之即第一人所得金數以次每減差數各得之矣并中央未到三人得應持金數
答曰甲 a斤 乙 b斤 丙 c斤 丁 d斤 戊 e斤 己 f斤 庚 g斤 辛 h斤 壬 i斤 癸 j斤 未到 k人 共得 l斤
"""

"""
Suppose there are 10 people of equal rank, with officials ranked from A (highest) to J (lowest). 
The officials are granted gold based on their rank in descending order. 
The first three people (A, B, C) enter first and take out 4 jin of gold. 
The last four people (G, H, I, J) enter later and take out 3 jin of gold. 
The middle three people (D, E, F) have not yet arrived, but they will also be given gold based on their rank.

Question: How much gold does each person get, and how much gold should the three middle people (D, E, F) receive?

The procedure says:
1. Divide the amount of gold taken by the first group by the number of people in the first group to get the upper rate.
2. Divide the amount of gold taken by the last group by the number of people in the last group to get the lower rate.
3. Subtract the lower rate from the upper rate to get the difference (差, "difference").
4. Add the number of people in the first and last groups, then halve the sum. Subtract this from the total number of people to get the difference divisor (差法, "difference divisor").
5. Multiply the difference by the difference divisor, then divide by 1 to get the difference amount (差數, "difference amount").
6. Add 1, 2, 3, etc., to the difference amount, and multiply by the difference amount. Subtract this from the gold taken by the last group, then divide by the number of people in the last group to get the base amount for the last group.
7. For the first person, subtract the difference amount repeatedly to calculate the gold for each person in descending order.
8. For the middle three people, calculate the total gold they should receive.

Answer: A gets *a* jin, B gets *b* jin, ..., J gets *j* jin, and the three middle people together get *l* jin.
"""

from fractions import Fraction

# 上三人先入得金四斤
先入人數 = 3
先入金 = 4

# 下四人後入得金三斤
後入人數 = 4
後入金 = 3

# 中央三人未到
中央人數 = 3

# 總人數
總人數 = 10

# 以先入人數分所持金數為上率
上率 = Fraction(先入金, 先入人數)

# 以後入人數分所持金數為下率
下率 = Fraction(後入金, 後入人數)

# 二率相減餘為差
差 = 上率 - 下率

# 實併先後入人數而半之
先後人數 = 先入人數 + 後入人數
半先後人數 = Fraction(先後人數, 2)

# 以減凡人數餘為差法
差法 = 總人數 - 半先後人數

# 實如法而一得差數
差數 = Fraction(差 * 差法, 1)

# 倂一二三以差數乗之以減後入人所持金數
後入基數 = Fraction(後入金 - 差數 * (1 + 2 + 3), 後入人數)

# 計算每個人的金數
甲 = 後入基數 + 6 * 差數
乙 = 甲 - 差數
丙 = 乙 - 差數
丁 = 丙 - 差數
戊 = 丁 - 差數
己 = 戊 - 差數
庚 = 己 - 差數
辛 = 庚 - 差數
壬 = 辛 - 差數
癸 = 壬 - 差數

# 中央三人得應持金數
中央金 = 差數 * 中央人數

# 答案
a, b, c, d, e, f, g, h, i, j = 甲, 乙, 丙, 丁, 戊, 己, 庚, 辛, 壬, 癸
k = 中央人數
l = 中央金
"""
Variable 'a' has wrong value. Expected: 37/26, Actual: 285/16
Variable 'b' has wrong value. Expected: 4/3, Actual: 673/48
Variable 'c' has wrong value. Expected: 97/78, Actual: 491/48
Variable 'd' has wrong value. Expected: 15/13, Actual: 103/16
Variable 'e' has wrong value. Expected: 83/78, Actual: 127/48
Variable 'f' has wrong value. Expected: 38/39, Actual: -55/48
Variable 'g' has wrong value. Expected: 23/26, Actual: -79/16
Variable 'h' has wrong value. Expected: 31/39, Actual: -419/48
Variable 'i' has wrong value. Expected: 55/78, Actual: -601/48
Variable 'j' has wrong value. Expected: 8/13, Actual: -261/16
Variable 'l' has wrong value. Expected: 83/26, Actual: 91/8"""
