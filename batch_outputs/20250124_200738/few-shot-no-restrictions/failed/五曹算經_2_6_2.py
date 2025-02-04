"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a疋 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 10,000 people: 10 generals, 20 vice-generals, 100 squad leaders, and 9,870 regular soldiers.
They are to be given silk in varying amounts: each general is given 3 zhang, each vice-general is given 2 zhang, each squad leader is given 1 zhang 5 chi, and each regular soldier is given 9 chi.
Question: how much silk is required in total?

The procedure says: 
List the 10 generals, multiply by 30 chi (3 zhang = 30 chi), obtaining 300 chi.
List the 20 vice-generals, multiply by 20 chi (2 zhang = 20 chi), obtaining 400 chi.
List the 100 squad leaders, multiply by 15 chi (1 zhang 5 chi = 15 chi), obtaining 1,500 chi.
List the 9,870 regular soldiers, multiply by 9 chi, obtaining 88,830 chi.
Add the four results together, obtaining 91,030 chi.
Divide by the silk conversion factor (疋法) to get the total number of bolts of silk.

Answer: *a* bolts of silk, with *b* wen remaining.
"""

# Conversion factors
一疋 = 240  # 1 bolt of silk = 240 chi

# 大將 10人，每人給 3丈 = 30尺
大將數 = 10
大將每人 = 30
大將總 = 大將數 * 大將每人

# 裨將 20人，每人給 2丈 = 20尺
裨將數 = 20
裨將每人 = 20
裨將總 = 裨將數 * 裨將每人

# 隊將 100人，每人給 1丈5尺 = 15尺
隊將數 = 100
隊將每人 = 15
隊將總 = 隊將數 * 隊將每人

# 散兵 9870人，每人給 9尺
散兵數 = 9870
散兵每人 = 9
散兵總 = 散兵數 * 散兵每人

# 計算總尺數
總尺數 = 大將總 + 裨將總 + 队將總 + 散兵總

# 以疋法除之
a = 總尺數 // 一疋  # 整數部分為疋數
b = 總尺數 % 一疋   # 餘數為文數

a疋 = a
b文 = b#----- content ends here -----

"""
Code error: name '队將總' is not defined"""
