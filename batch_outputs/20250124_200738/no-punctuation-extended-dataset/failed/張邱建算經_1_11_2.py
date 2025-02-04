"""
今有十等人大官甲等十人官賜金依等次差降之上三人先入得金四斤持出下四人後入得金三斤持出中央三人未到者亦依等次更給問各得金㡬何及未到三人復應得金㡬何
術曰以先入人數分所持金數為上率以後入人數分所持金數為下率二率相減餘為差實併先後入人數而半之以減凡人數餘為差法實如法而一得差數倂一二三以差數乗之以減後入人所持金數餘以後入人數而一又置十人減一餘乗差數併之即第一人所得金數以次每減差數各得之矣并中央未到三人得應持金數
答曰甲 a斤 乙 b斤 丙 c斤 丁 d斤 戊 e斤 己 f斤 庚 g斤 辛 h斤 壬 i斤 癸 j斤 未到 k人 共得 l斤
"""

#----- content starts here -----
"""
Suppose there are ten people ranked in ten classes. Officials of the highest class (甲等) number 10 people. 
The officials are granted gold according to their rank in descending order. 
The first three people (上三人) enter first and receive 4 jin of gold to take out. 
The next four people (下四人) enter later and receive 3 jin of gold to take out. 
The middle three people (中央三人) have not yet arrived but will also be granted gold according to their rank.

Question: How much gold does each person receive, and how much gold should the three who have not yet arrived receive?

The procedure says:
- Divide the gold received by the first group by the number of people in the first group to get the upper rate (上率).
- Divide the gold received by the second group by the number of people in the second group to get the lower rate (下率).
- Subtract the lower rate from the upper rate to get the difference (差).
- Add the number of people in the first and second groups, then halve the sum. Subtract this from the total number of people to get the difference divisor (差法).
- Multiply the difference (差) by the difference divisor (差法), then divide by 1 to get the difference value (差數).
- Add 1, 2, 3, etc., to the difference value (差數) and multiply by it. Subtract the gold received by the second group, then divide by the number of people in the second group to get the gold for each person.
- For the ten people, subtract 1 from the total number of people, multiply the remainder by the difference value (差數), and add it to the gold received by the first person to determine the gold for each subsequent person.
- Also calculate the gold for the three middle people who have not yet arrived.

Answer: 甲 receives *a* jin, 乙 receives *b* jin, 丙 receives *c* jin, 丁 receives *d* jin, 戊 receives *e* jin, 己 receives *f* jin, 庚 receives *g* jin, 辛 receives *h* jin, 壬 receives *i* jin, 癸 receives *j* jin. The three who have not yet arrived (未到) receive *k* people in total, and they receive *l* jin of gold.
"""

from fractions import Fraction

# 上三人先入得金四斤
上人數 = 3
上金數 = 4

# 下四人後入得金三斤
下人數 = 4
下金數 = 3

# 中央三人未到
中央人數 = 3

# 以先入人數分所持金數為上率
上率 = Fraction(上金數, 上人數)

# 以後入人數分所持金數為下率
下率 = Fraction(下金數, 下人數)

# 二率相減餘為差
差 = 上率 - 下率

# 實併先後入人數而半之
先後人數 = 上人數 + 下人數
半先後人數 = Fraction(先後人數, 2)

# 以減凡人數餘為差法
凡人數 = 10
差法 = 凡人數 - 半先後人數

# 實如法而一得差數
差數 = Fraction(差 * 差法, 1)

# 倂一二三以差數乗之以減後入人所持金數餘以後入人數而一
後入金數餘 = 下金數 - 差數 * sum(range(1, 下人數 + 1))
後入人金 = Fraction(後入金數餘, 下人數)

# 又置十人減一餘乗差數併之即第一人所得金數
金數 = []
for i in range(凡人數):
    金數.append(上率 - i * 差數)

# 中央未到三人得應持金數
未到金數 = sum(金數[上人數:上人數 + 中央人數])

# Assign results
a, b, c, d, e, f, g, h, i, j = 金數
k = 中央人數
l = 未到金數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 37/26, Actual: 4/3
Variable 'b' has wrong value. Expected: 4/3, Actual: -59/24
Variable 'c' has wrong value. Expected: 97/78, Actual: -25/4
Variable 'd' has wrong value. Expected: 15/13, Actual: -241/24
Variable 'e' has wrong value. Expected: 83/78, Actual: -83/6
Variable 'f' has wrong value. Expected: 38/39, Actual: -141/8
Variable 'g' has wrong value. Expected: 23/26, Actual: -257/12
Variable 'h' has wrong value. Expected: 31/39, Actual: -605/24
Variable 'i' has wrong value. Expected: 55/78, Actual: -29
Variable 'j' has wrong value. Expected: 8/13, Actual: -787/24
Variable 'l' has wrong value. Expected: 83/26, Actual: -83/2"""
