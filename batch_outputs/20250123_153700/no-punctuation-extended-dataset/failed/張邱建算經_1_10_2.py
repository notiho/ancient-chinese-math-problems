"""
今有官出庫金五十九斤一兩賜王九人公十二人侯十五人子十八人男二十一人王得金各多公五兩公得金各多侯四兩侯得金各多子三兩子得金各多男二兩問王公侯子男各得金㡬何
術曰置王公侯子男數王位十四之公位九之侯位五之子位二之併之以減出金兩數餘以凡人數而一所得各以本差之數加之得王公侯子男各所得金之數不加即男之得金
答曰王 a斤 公 b斤 侯 c兩 子 d兩 男 e兩
"""

"""
Suppose there is an official distributing 59 jin and 1 liang of gold from the treasury to 9 kings, 12 dukes, 15 marquises, 18 viscounts, and 21 barons.
Each king receives 5 liang more than each duke.
Each duke receives 4 liang more than each marquis.
Each marquis receives 3 liang more than each viscount.
Each viscount receives 2 liang more than each baron.
Question: how much gold does each king, duke, marquis, viscount, and baron receive?

The procedure says:
1. Place the numbers of kings, dukes, marquises, viscounts, and barons.
2. Assign weights: kings are weighted as 14, dukes as 9, marquises as 5, viscounts as 2, and barons as 1.
3. Add the weighted values together, and subtract this from the total amount of gold (converted to liang).
4. Divide the remainder by the total number of people to find the base amount of gold received by the barons.
5. Add the respective differences to the base amount to find the amounts received by the kings, dukes, marquises, and viscounts.
6. The base amount itself is the amount received by the barons.

Answer: Each king receives *a* jin, each duke receives *b* liang, each marquis receives *c* liang, each viscount receives *d* liang, and each baron receives *e* liang.
"""

# 官出庫金五十九斤一兩
總金兩 = 59 * 16 + 1  # Convert to liang (1 jin = 16 liang)

# 王九人、公十二人、侯十五人、子十八人、男二十一人
王數 = 9
公數 = 12
侯數 = 15
子數 = 18
男數 = 21

# 王位十四之、公位九之、侯位五之、子位二之、男位一之
王位 = 14
公位 = 9
侯位 = 5
子位 = 2
男位 = 1

# 計算總權重
總權重 = 王數 * 王位 + 公數 * 公位 + 侯數 * 侯位 + 子數 * 子位 + 男數 * 男位

# 計算剩餘金兩
剩餘金兩 = 總金兩 - 總權重

# 計算每人基礎金兩（男所得）
基礎金兩 = Fraction(剩餘金兩, 王數 + 公數 + 侯數 + 子數 + 男數)

# 計算各級所得金兩
男所得 = 基礎金兩
子所得 = 男所得 + 2
侯所得 = 子所得 + 3
公所得 =侯所得+4

"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'"""
