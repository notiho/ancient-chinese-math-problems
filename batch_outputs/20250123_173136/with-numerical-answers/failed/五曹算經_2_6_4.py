"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a(=2275)疋 奇 b(=3)文 。
"""

"""
Suppose there are 10,000 people: 10 generals, 20 deputy generals, 100 squad leaders, and 9,870 regular soldiers.
The distribution of silk varies: each general is given 3 zhang, each deputy general is given 2 zhang, each squad leader is given 1 zhang 5 chi, and each regular soldier is given 9 chi.
Question: how much silk is needed in total?

The procedure says: List the 10 generals, multiply by 30 chi (3 zhang), obtaining 300 chi.
Then list the 20 deputy generals, multiply by 20 chi (2 zhang), obtaining 400 chi.
Then list the 100 squad leaders, multiply by 15 chi (1 zhang 5 chi), obtaining 1,500 chi.
Then list the 9,870 regular soldiers, multiply by 9 chi, obtaining 88,830 chi.
Add the four results, obtaining 91,030 chi.
Divide by the silk bolt divisor (240 chi per bolt), obtaining the number of bolts and the remainder.

Answer: *a*(=2275) bolts, remainder *b*(=3) chi.
"""

# 大將十人，每人給三丈
大將人數 = 10
大將每人絹 = 30  # 3丈 = 30尺
大將總絹 = 大將人數 * 大將每人絹  # 300尺

# 裨將二十人，每人給二丈
裨將人數 = 20
裨將每人絹 = 20  # 2丈 = 20尺
裨將總絹 = 裨將人數 * 裨將每人絹  # 400尺

# 隊將一百人，每人給一丈五尺
隊將人數 = 100
隊將每人絹 = 15  # 1丈5尺 = 15尺
隊將總絹 = 隊將人數 * 隊將每人絹  # 1500尺

# 散兵九千八百七十人，每人給九尺
散兵人數 = 9870
散兵每人絹 = 9  # 9尺
散兵總絹 = 散兵人數 * 散兵每人絹  # 88830尺

# 計算總絹
總絹 = 大將總絹 + 裨將總絹 + 隊將總絹 + 散兵總絹  # 91030尺

# 疋法：一疋等於240尺
疋法 = 240

# 以疋法除之
a = 總絹 // 疋法  # 2275疋
b = 總絹 % 疋法  # 3尺
"""
Variable 'a' has wrong value. Expected: 2275, Actual: 379
Variable 'b' has wrong value. Expected: 3, Actual: 70"""
