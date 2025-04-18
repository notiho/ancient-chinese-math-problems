"""
今有官出庫金五十九斤一兩賜王九人公十二人侯十五人子十八人男二十一人王得金各多公五兩公得金各多侯四兩侯得金各多子三兩子得金各多男二兩問王公侯子男各得金㡬何
術曰置王公侯子男數王位十四之公位九之侯位五之子位二之併之以減出金兩數餘以凡人數而一所得各以本差之數加之得王公侯子男各所得金之數不加即男之得金
答曰王 a斤 公 b斤 侯 c兩 子 d兩 男 e兩
"""

#----- content starts here -----
"""
Suppose there is an official distributing 59 jin and 1 liang of gold from the treasury.
It is to be distributed among 9 kings, 12 dukes, 15 marquises, 18 viscounts, and 21 barons.
Each king receives 5 liang more than each duke, each duke receives 4 liang more than each marquis, each marquis receives 3 liang more than each viscount, and each viscount receives 2 liang more than each baron.
Question: how much gold does each king, duke, marquis, viscount, and baron receive?

The procedure says: Place the numbers of kings, dukes, marquises, viscounts, and barons.
The position of the king is multiplied by 14, the duke by 9, the marquis by 5, and the viscount by 2.
Add these together, and subtract from the total amount of gold in liang.
The remainder is divided by the total number of people, and the result is the amount of gold each baron receives.
Each person's share is obtained by adding their respective differences to this base amount.
The baron's share is the base amount without any additions.

Answer: Each king receives *a* jin, each duke receives *b* jin, each marquis receives *c* liang, each viscount receives *d* liang, and each baron receives *e* liang.
"""

# 官出庫金五十九斤一兩
總金兩 = 59 * 16 + 1  # Convert to liang (1 jin = 16 liang)

# 王九人，公十二人，侯十五人，子十八人，男二十一人
王數 = 9
公數 = 12
侯數 = 15
子數 = 18
男數 = 21

# 王位十四之，公位九之，侯位五之，子位二之
王位 = 14
公位 = 9
侯位 = 5
子位 = 2
男位 = 1  # Implicitly 1 for barons

# 併之
總位 = 王數 * 王位 + 公數 * 公位 + 侯數 * 侯位 + 子數 * 子位 + 男數 * 男位

# 以減出金兩數
餘金 = 總金兩 - 總位

# 餘以凡人數而一
總人數 = 王數 + 公數 + 侯數 + 子數 + 男數
男得金 = Fraction(餘金, 總人數)

# 所得各以本差之數加之
子得金 = 男得金 + 2
侯得金 = 子得金 + 3
公得金 = 侯得金 + 4
王得金 = 公得金 + 5

# Convert to jin and liang
a = Fraction(王得金, 16)  # 王得金 in jin
b = Fraction(公得金, 16)  # 公得金 in jin
c = 侯得金  # 侯得金 in liang
d = 子得金  # 子得金 in liang
e = 男得金  # 男得金 in liang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 11/8, Actual: 543/400
Variable 'b' has wrong value. Expected: 17/16, Actual: 209/200
Variable 'c' has wrong value. Expected: 13, Actual: 318/25
Variable 'd' has wrong value. Expected: 10, Actual: 243/25
Variable 'e' has wrong value. Expected: 8, Actual: 193/25"""
