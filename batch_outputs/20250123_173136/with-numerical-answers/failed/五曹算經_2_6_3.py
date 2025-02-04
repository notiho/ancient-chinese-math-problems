"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a(=2275)疋 奇 b(=3)文 。
"""

"""
Suppose there are 10,000 people: 10 generals, 20 deputy generals, 100 squad leaders, and 9,870 ordinary soldiers.
They are to be given silk in varying amounts: each general receives 3 zhang, each deputy general receives 2 zhang, each squad leader receives 1 zhang and 5 chi, and each ordinary soldier receives 9 chi.
Question: how much silk is required in total?

The procedure says: 
List the 10 generals, multiply by 30 chi (3 zhang = 30 chi), obtaining 300 chi.
List the 20 deputy generals, multiply by 20 chi (2 zhang = 20 chi), obtaining 400 chi.
List the 100 squad leaders, multiply by 15 chi (1 zhang 5 chi = 15 chi), obtaining 1,500 chi.
List the 9,870 ordinary soldiers, multiply by 9 chi, obtaining 88,830 chi.
Add the results of the four groups, obtaining 91,030 chi.
Divide by the silk bolt divisor (1 bolt = 40 chi), obtaining the result.

Answer: *a*(=2275) bolts, remainder *b*(=3) chi.
"""

# 大將十人，每人給三丈 (30 尺)
大將人數 = 10
大將每人給 = 30  # 尺
大將總量 = 大將人數 * 大將每人給  # 300 尺

# 裨將二十人，每人給二丈 (20 尺)
裨將人數 = 20
裨將每人給 = 20  # 尺
裨將總量 = 裨將人數 * 裨將每人給  # 400 尺

# 隊將一百人，每人給一丈五尺 (15 尺)
隊將人數 = 100
隊將每人給 = 15  # 尺
隊將總量 = 隊將人數 * 隊將每人給  # 1500 尺

# 散兵九千八百七十人，每人給九尺
散兵人數 = 9870
散兵每人給 = 9  # 尺
散兵總量 = 散兵人數 * 散兵每人給  # 88830 尺

# 并四位得總量
總量 = 大將總量 + 裨將總量 + 隊將總量 + 散兵總量  # 91030 尺

# 疋法 (每疋 40 尺)
疋法 = 40

# 以疋法除之即得
a = 總量 // 疋法  # 2275 疋
b = 總量 % 疋法   # 3 尺
"""
Variable 'b' has wrong value. Expected: 3, Actual: 30"""
