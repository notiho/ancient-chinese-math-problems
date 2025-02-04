"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a疋 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 10,000 people: 10 generals, 20 deputy generals, 100 squad leaders, and 9,870 regular soldiers.
They are to be given silk in varying amounts: each general receives 3 zhang, each deputy general receives 2 zhang, each squad leader receives 1 zhang and 5 chi, and each regular soldier receives 9 chi.
Question: how much silk is required in total?

The procedure says: 
List the 10 generals, multiply by 30 chi (3 zhang = 30 chi), obtaining 300 chi.
Then list the 20 deputy generals, multiply by 20 chi (2 zhang = 20 chi), obtaining 400 chi.
Then list the 100 squad leaders, multiply by 15 chi (1 zhang 5 chi = 15 chi), obtaining 1,500 chi.
Then list the 9,870 regular soldiers, multiply by 9 chi, obtaining 88,830 chi.
Add the four results together, obtaining 91,030 chi.
Divide by the silk unit (疋法), obtaining the total number of bolts of silk.

Answer: *a* bolts (疋) with *b* chi remaining.
"""

# 大將十人，每人給三丈
大將人數 = 10
大將每人絹 = 30  # 3丈 = 30尺
大將總絹 = 大將人數 * 大將每人絹

# 裨將二十人，每人給二丈
裨將人數 = 20
裨將每人絹 = 20  # 2丈 = 20尺
裨將總絹 = 裨將人數 * 裨將每人絹

# 隊將一百人，每人給一丈五尺
隊將人數 = 100
隊將每人絹 = 15  # 1丈5尺 = 15尺
隊將總絹 = 隊將人數 *隊將每人絹

# 散兵九千八百七十人，每人給九尺
散兵人數 = 9870
散兵每人絹 = 9  # 9尺
散兵總絹 = 散兵人數 * 散兵每人絹

# 計算總絹數
總絹 = 大將總絹 + 裨將總絹 + 隊將總絹 + 散兵總絹

# 疋法：一疋等於五十尺
疋法 = 50

# 以疋法除之，計算疋數和剩餘尺數
a = 總絹 // 疋法  # 疋數
b = 總絹 % 疋法  # 剩餘尺數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2275, Actual: 1820
Variable 'b' has wrong value. Expected: 3, Actual: 30"""
