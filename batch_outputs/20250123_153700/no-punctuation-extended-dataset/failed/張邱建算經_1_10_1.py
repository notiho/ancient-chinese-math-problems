"""
今有官出庫金五十九斤一兩賜王九人公十二人侯十五人子十八人男二十一人王得金各多公五兩公得金各多侯四兩侯得金各多子三兩子得金各多男二兩問王公侯子男各得金㡬何
術曰置王公侯子男數王位十四之公位九之侯位五之子位二之併之以減出金兩數餘以凡人數而一所得各以本差之數加之得王公侯子男各所得金之數不加即男之得金
答曰王 a斤 公 b斤 侯 c兩 子 d兩 男 e兩
"""

"""
Suppose there is an official distributing 59 jin and 1 liang of gold from the treasury.
It is to be given to 9 kings, 12 dukes, 15 marquises, 18 viscounts, and 21 barons.
Each king receives 5 liang more than each duke.
Each duke receives 4 liang more than each marquis.
Each marquis receives 3 liang more than each viscount.
Each viscount receives 2 liang more than each baron.

Question: How much gold does each king, duke, marquis, viscount, and baron receive?

The procedure says: Place the numbers of kings, dukes, marquises, viscounts, and barons.
Assign the king's position as 14, the duke's position as 9, the marquis's position as 5, and the viscount's position as 2.
Add these together and subtract from the total amount of gold in liang.
Divide the remainder by the total number of people, obtaining the base amount of gold for each baron.
Add the differences for each rank to this base amount to obtain the amount of gold for each king, duke, marquis, viscount, and baron.
Without adding, it is the amount of gold for each baron.

Answer: Each king receives *a* jin, each duke receives *b* liang, each marquis receives *c* liang, each viscount receives *d* liang, and each baron receives *e* liang.
"""

# 官出庫金五十九斤一兩
總金 = 59 * 16 + 1  # Convert to liang (1 jin = 16 liang)

# 王九人、公十二人、侯十五人、子十八人、男二十一人
王數 = 9
公數 = 12
侯數 = 15
子數 = 18
男數 = 21

# 王位十四之、公位九之、侯位五之、子位二之
王位 = 14
公位 = 9
侯位 = 5
子位 = 2
男位 = 1  # Implicitly, barons have no additional weight

# 併之
總位 = 王數 * 王位 + 公數 * 公位 + 侯數 * 侯位 + 子數 * 子位 + 男數 * 男位

# 以減出金兩數
餘金 = 總金 - 總位

# 餘以凡人數而一
總人數 = 王數 + 公數 + 侯數 + 子數 + 男數
男得金 = Fraction(餘金, 總人數)

# 所得各以本差之數加之
子得金 = 男得金 + 2
侯得金 = 子得金 + 3
公得金 =侯得金+4

"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'"""
