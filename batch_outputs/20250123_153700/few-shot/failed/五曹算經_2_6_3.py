"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a疋 奇 b文 。
"""

"""
Suppose there are 10,000 people: 10 generals, 20 vice-generals, 100 squad leaders, and 9,870 ordinary soldiers.
They are to be given silk in varying amounts: 3 zhang per general, 2 zhang per vice-general, 1 zhang 5 chi per squad leader, and 9 chi per ordinary soldier.
Question: how much silk is required in total?

The procedure says: List the 10 generals, multiply by 30 chi (3 zhang), obtaining 300 chi.
Then list the 20 vice-generals, multiply by 20 chi (2 zhang), obtaining 400 chi.
Then list the 100 squad leaders, multiply by 15 chi (1 zhang 5 chi), obtaining 1,500 chi.
Then list the 9,870 ordinary soldiers, multiply by 9 chi, obtaining 88,830 chi.
Add the four results, obtaining 91,030 chi.
Divide by the silk bolt standard (疋法) to obtain the result.

Answer: *a* bolts of silk, with *b* chi remaining.
"""

# 大將十人
大將人數 = 10
# 裨將二十人
裨將人數 = 20
# 隊將一百人
隊將人數 = 100
# 散兵九千八百七十人
散兵人數 = 9870

# 大將人給三丈 (1丈 = 10尺, so 3丈 = 30尺)
大將給絹 = 30
# 裨將人給二丈 (2丈 = 20尺)
裨將給絹 = 20
# 隊將人給一丈五尺 (1丈5尺 = 15尺)
隊將給絹 = 15
# 散兵人給九尺
散兵給絹 = 9

# 計算各類人員所需絹
大將所需 = 大將人數 * 大將給絹
裨將所需 = 裨將人數 * 裨將給絹
隊將所需 = 隊將人數 * 队將給絹
散兵所需 = 散兵人數 * 散兵給絹

# 并四位得總尺數
總尺數 = 大將所需 + 裨將所需 + 隊將所需 + 散兵所需

# 疋法 (1疋 = 50尺)
疋法 = 50

# 以疋法除之即得
a = 總尺數 // 疋法  # 疋數
b = 總尺數 % 疋法   # 剩餘尺數
"""
Code error: name '队將給絹' is not defined"""
