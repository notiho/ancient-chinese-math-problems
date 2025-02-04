"""
今有十等人大官甲等十人官賜金依等次差降之上三人先入得金四斤持出下四人後入得金三斤持出中央三人未到者亦依等次更給問各得金㡬何及未到三人復應得金㡬何
術曰以先入人數分所持金數為上率以後入人數分所持金數為下率二率相減餘為差實併先後入人數而半之以減凡人數餘為差法實如法而一得差數倂一二三以差數乗之以減後入人所持金數餘以後入人數而一又置十人減一餘乗差數併之即第一人所得金數以次每減差數各得之矣并中央未到三人得應持金數
答曰甲 a斤 乙 b斤 丙 c斤 丁 d斤 戊 e斤 己 f斤 庚 g斤 辛 h斤 壬 i斤 癸 j斤 未到 k人 共得 l斤
"""

#----- content starts here -----
"""
Suppose there are 10 people ranked in 10 classes. The highest class (甲等) has 10 people. Gold is distributed according to rank differences.
The first three people (先入) receive 4 jin of gold and leave. The next four people (後入) receive 3 jin of gold and leave. 
The middle three people (中央未到) have not yet arrived, but they will also be given gold according to rank differences.

Question: How much gold does each person receive, and how much gold should the three middle people (未到) receive in total?

The procedure says:
1. Divide the gold held by the first group (先入) by the number of people in that group to get the upper rate (上率).
2. Divide the gold held by the second group (後入) by the number of people in that group to get the lower rate (下率).
3. Subtract the lower rate from the upper rate to get the difference (差).
4. Add the number of people in the first and second groups, then halve it. Subtract this from the total number of people to get the difference divisor (差法).
5. Multiply the difference (差) by the difference divisor (差法), then divide by the total divisor (差法而一) to get the difference number (差數).
6. Add the difference number (差數) to the rank numbers (1, 2, 3, ...). Multiply this by the difference number (差數) and subtract it from the gold held by the second group (後入). Divide the remainder by the number of people in the second group (後入人數).
7. Subtract the difference number (差數) from the gold held by each subsequent rank to determine how much each person receives.
8. For the three middle people (中央未到), calculate their total gold based on the rank differences.

Answer: 甲 receives *a* jin, 乙 receives *b* jin, 丙 receives *c* jin, 丁 receives *d* jin, 戊 receives *e* jin, 己 receives *f* jin, 庚 receives *g* jin, 辛 receives *h* jin, 壬 receives *i* jin, 癸 receives *j* jin. The three middle people (未到) receive *k* people in total, and they receive *l* jin of gold.
"""

from fractions import Fraction

# Initial data
總人數 = 10
先入人數 = 3
後入人數 = 4
先入金數 = 4
後入金數 = 3

# Step 1: Calculate the upper rate (上率) and lower rate (下率)
上率 = Fraction(先入金數, 先入人數)
下率 = Fraction(後入金數, 後入人數)

# Step 2: Calculate the difference (差)
差 = 上率 - 下率

# Step 3: Calculate the difference divisor (差法)
差法 = Fraction((先入人數 + 後入人數), 2)
差法 = 總人數 - 差法

# Step 4: Calculate the difference number (差數)
差數 = Fraction(差, 差法)

# Step 5: Calculate the gold for the first person (第一人所得金數)
第一人所得金數 = 後入金數 + (總人數 - 1) * 差數

# Step 6: Calculate the gold for each person
金數 = []
for i in range(總人數):
    金數.append(第一人所得金數 - i * 差數)

# Step 7: Calculate the total gold for the three middle people (中央未到)
中央未到人數 = 總人數 - 先入人數 - 後入人數
中央未到金數 = sum(金數[先入人數:先入人數 + 中央未到人數])

# Assign results
a, b, c, d, e, f, g, h, i, j = 金數
k = 中央未到人數
l = 中央未到金數

# Outputs
a, b, c, d, e, f, g, h, i, j, k, l#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 37/26, Actual: 99/26
Variable 'b' has wrong value. Expected: 4/3, Actual: 145/39
Variable 'c' has wrong value. Expected: 97/78, Actual: 283/78
Variable 'd' has wrong value. Expected: 15/13, Actual: 46/13
Variable 'e' has wrong value. Expected: 83/78, Actual: 269/78
Variable 'f' has wrong value. Expected: 38/39, Actual: 131/39
Variable 'g' has wrong value. Expected: 23/26, Actual: 85/26
Variable 'h' has wrong value. Expected: 31/39, Actual: 124/39
Variable 'i' has wrong value. Expected: 55/78, Actual: 241/78
Variable 'j' has wrong value. Expected: 8/13, Actual: 3
Variable 'l' has wrong value. Expected: 83/26, Actual: 269/26"""
