"""
今有官出庫金五十九斤一兩賜王九人公十二人侯十五人子十八人男二十一人王得金各多公五兩公得金各多侯四兩侯得金各多子三兩子得金各多男二兩問王公侯子男各得金㡬何
術曰置王公侯子男數王位十四之公位九之侯位五之子位二之併之以減出金兩數餘以凡人數而一所得各以本差之數加之得王公侯子男各所得金之數不加即男之得金
答曰王 a斤 公 b斤 侯 c兩 子 d兩 男 e兩
"""

"""
Suppose there is an official distributing 59 jin and 1 liang of gold from the treasury to various ranks:
9 kings, 12 dukes, 15 marquises, 18 viscounts, and 21 barons.
Each king receives 5 liang more than each duke.
Each duke receives 4 liang more than each marquis.
Each marquis receives 3 liang more than each viscount.
Each viscount receives 2 liang more than each baron.
Question: how much gold does each rank receive?

The procedure says:
1. Place the numbers of kings, dukes, marquises, viscounts, and barons.
2. Assign weights to their positions: kings are weighted 14, dukes 9, marquises 5, viscounts 2, and barons 1.
3. Add these weights together and subtract from the total amount of gold (in liang).
4. Divide the remainder by the total number of people to find the base amount of gold for the barons.
5. Add the respective differences to the base amount according to the weights to find the gold received by each rank.
6. The amount without adding differences is the amount received by the barons.

Answer: Each king receives *a* jin, each duke receives *b* liang, each marquis receives *c* liang, each viscount receives *d* liang, and each baron receives *e* liang.
"""

# Total gold in liang (convert 59 jin and 1 liang to liang)
total_gold_liang = 59 * 16 + 1

# Number of people in each rank
num_kings = 9
num_dukes = 12
num_marquises = 15
num_viscounts = 18
num_barons = 21

# Weight of each rank
king_weight = 14
duke_weight = 9
marquis_weight = 5
viscount_weight = 2
baron_weight = 1

# Total weight
total_weight = (
    num_kings * king_weight
    + num_dukes * duke_weight
    + num_marquises * marquis_weight
    + num_viscounts * viscount_weight
    + num_barons * baron_weight
)

# Subtract total weight from total gold
remaining_gold = total_gold_liang - total_weight

# Total number of people
total_people = num_kings + num_dukes + num_marquises + num_viscounts + num_barons

# Base amount of gold for barons
base_gold = Fraction(remaining_gold, total_people)

# Calculate gold for each rank
gold_per_baron = base_gold
gold_per_viscount = base_gold + 2
gold_per_marquis = base_gold + 3
gold_per_duke = base_gold + 4
gold_per_king = base_gold + 5

# Convert results to jin and liang
a = Fraction(gold_per_king, 16)  # Kings' gold in jin
b = gold_per_duke  # Dukes' gold in liang
c = gold_per_marquis  # Marquises' gold in liang
d = gold_per_viscount  # Viscounts' gold in liang
e = gold_per_baron  # Barons' gold in liang
"""
Variable 'a' has wrong value. Expected: 11/8, Actual: 159/200
Variable 'b' has wrong value. Expected: 17/16, Actual: 293/25
Variable 'c' has wrong value. Expected: 13, Actual: 268/25
Variable 'd' has wrong value. Expected: 10, Actual: 243/25
Variable 'e' has wrong value. Expected: 8, Actual: 193/25"""
