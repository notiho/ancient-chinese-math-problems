"""
今有十等人大官甲等十人官賜金依等次差降之上三人先入得金四斤持出下四人後入得金三斤持出中央三人未到者亦依等次更給問各得金㡬何及未到三人復應得金㡬何
術曰以先入人數分所持金數為上率以後入人數分所持金數為下率二率相減餘為差實併先後入人數而半之以減凡人數餘為差法實如法而一得差數倂一二三以差數乗之以減後入人所持金數餘以後入人數而一又置十人減一餘乗差數併之即第一人所得金數以次每減差數各得之矣并中央未到三人得應持金數
答曰甲 a斤 乙 b斤 丙 c斤 丁 d斤 戊 e斤 己 f斤 庚 g斤 辛 h斤 壬 i斤 癸 j斤 未到 k人 共得 l斤
"""

#----- content starts here -----
"""
Suppose there are ten people of equal rank, with the highest rank being Jia (甲) and the lowest rank being Gui (癸). 
The officials are granted gold according to their rank in descending order.
The first three people (Jia, Yi, Bing) entered first and received 4 jin of gold to distribute among themselves.
The last four people (Geng, Xin, Ren, Gui) entered later and received 3 jin of gold to distribute among themselves.
The middle three people (Ding, Wu, Ji) have not yet arrived but will also be granted gold according to their rank.

Question: How much gold does each person receive, and how much gold should the three people who have not yet arrived receive?

The procedure says:
- Divide the gold held by the first group by the number of people in the first group to get the upper rate.
- Divide the gold held by the last group by the number of people in the last group to get the lower rate.
- Subtract the lower rate from the upper rate to get the difference.
- Add the number of people in the first and last groups, then halve it. Subtract this from the total number of people to get the difference divisor.
- Multiply the difference by the divisor, then divide by the difference divisor to get the difference amount.
- Add 1, 2, 3, etc., to the difference amount, multiply by the difference, and subtract from the gold held by the last group. Divide by the number of people in the last group to get the gold for each person in the last group.
- Subtract the difference iteratively for each rank to determine the gold for each person.
- For the middle three people, calculate their gold based on the difference and their rank.

Answer: Jia (甲) receives *a* jin, Yi (乙) receives *b* jin, Bing (丙) receives *c* jin, Ding (丁) receives *d* jin, Wu (戊) receives *e* jin, Ji (己) receives *f* jin, Geng (庚) receives *g* jin, Xin (辛) receives *h* jin, Ren (壬) receives *i* jin, Gui (癸) receives *j* jin. The three people who have not yet arrived (Ding, Wu, Ji) together receive *l* jin.
"""

# 上三人先入得金四斤
先入人數 = 3
先入金數 = 4

# 下四人後入得金三斤
後入人數 = 4
後入金數 = 3

# 中央三人未到
中央人數 = 3

# 以先入人數分所持金數為上率
上率 = Fraction(先入金數, 先入人數)

# 以後入人數分所持金數為下率
下率 = Fraction(後入金數, 後入人數)

# 二率相減餘為差
差 = 上率 - 下率

# 實併先後入人數而半之
先後人數 = 先入人數 + 後入人數
半人數 = Fraction(先後人數, 2)

# 以減凡人數餘為差法
凡人數 = 10
差法 = 凡人數 - 半人數

# 實如法而一得差數
差數 = Fraction(差, 差法)

# 倂一二三以差數乗之以減後入人所持金數餘以後入人數而一
後入金餘 = 後入金數
後入金餘 -= 差數 * (1 + 2 + 3)
後入金餘 = Fraction(後入金餘, 後入人數)

# 又置十人減一餘乗差數併之即第一人所得金數
第一人金數 = 差數 * (凡人數 - 1) + 後入金餘

# 以次每減差數各得之矣
甲 = 第一人金數
乙 = 甲 - 差數
丙 = 乙 - 差數
丁 = 丙 - 差數
戊 = 丁 - 差數
己 = 戊 - 差數
庚 = 己 - 差數
辛 = 庚 - 差數
壬 = 辛 - 差數
癸 = 壬 - 差數

# 并中央未到三人得應持金數
未到金數 = 丁 + 戊 + 己

# 答案
a = 甲
b = 乙
c = 丙
d = 丁
e = 戊
f = 己
g = 庚
h = 辛
i = 壬
j = 癸
k = 中央人數
l = 未到金數#----- content ends here -----

"""
"""
