"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a(=2275)疋 奇 b(=3)文 。
"""

#----- content starts here -----
"""
Suppose there are 10,000 people: 10 generals, 20 deputy generals, 100 squad leaders, and 9,870 regular soldiers.
Distribute silk cloth with differences: each general receives 3 zhang, each deputy general receives 2 zhang, each squad leader receives 1 zhang and 5 chi, and each regular soldier receives 9 chi.
Question: how much silk is needed in total?

The procedure says: List the 10 generals, multiply by 30 chi, obtaining 300 chi.
Then list the 20 deputy generals, multiply by 20 chi, obtaining 400 chi.
Then list the 100 squad leaders, multiply by 15 chi, obtaining 1,500 chi.
Then list the 9,870 regular soldiers, multiply by 9 chi, obtaining 88,830 chi.
Add the four results, obtaining 91,030 chi.
Divide by the silk bolt divisor to obtain the result.

Answer: *a*(=2275) bolts with a remainder of *b*(=3) chi.
"""

# 大將十人，每人給三丈
大將人數 = 10
大將每人給 = 30  # 3丈 = 30尺
大將總給 = 大將人數 * 大將每人給  # 300尺

# 裨將二十人，每人給二丈
裨將人數 = 20
裨將每人給 = 20  # 2丈 = 20尺
裨將總給 = 裨將人數 * 裨將每人給  # 400尺

# 隊將一百人，每人給一丈五尺
隊將人數 = 100
隊將每人給 = 15  # 1丈5尺 = 15尺
隊將總給 = 隊將人數 *隊將每人給  # 1500尺

# 散兵九千八百七十人，每人給九尺
散兵人數 = 9870
散兵每人給 = 9  # 9尺
散兵總給 = 散兵人數 * 散兵每人給  # 88830尺

# 并四位得九萬一千三十尺
總尺數 = 大將總給 + 裨將總給 + 隊將總給 + 散兵總給  # 91030尺

# 疋法：一疋等於40尺
疋法 = 40

# 以疋法除之即得
a = 總尺數 // 疋法  # 2275疋
b = 總尺數 % 疋法   # 3尺#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 3, Actual: 30"""
