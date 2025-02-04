"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a疋 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 10,000 people: 10 generals, 20 deputy generals, 100 squad leaders, and 9,870 regular soldiers.
They are to be given silk in varying amounts:
- Each general is given 3 zhang (30 chi),
- Each deputy general is given 2 zhang (20 chi),
- Each squad leader is given 1 zhang 5 chi (15 chi),
- Each regular soldier is given 9 chi.

Question: How much silk is needed in total?

The procedure says:
- Multiply the number of generals (10) by 30 chi, obtaining 300 chi.
- Multiply the number of deputy generals (20) by 20 chi, obtaining 400 chi.
- Multiply the number of squad leaders (100) by 15 chi, obtaining 1,500 chi.
- Multiply the number of regular soldiers (9,870) by 9 chi, obtaining 88,830 chi.
- Add these four results together to get 91,030 chi.
- Divide by the silk bolt standard (疋法) to determine the number of bolts and leftover chi.

Answer: *a* bolts and *b* chi.
"""

# 人數與給絹標準
大將數 = 10
裨將數 = 20
隊將數 = 100
散兵數 = 9870

大將給絹 = 30  # 每人 30 尺
裨將給絹 = 20  # 每人 20 尺
隊將給絹 = 15  # 每人 15 尺
散兵給絹 = 9   # 每人 9 尺

# 計算各類人員的總絹數
大將總絹 = 大將數 * 大將給絹
裨將總絹 = 裨將數 * 裨將給絹
隊將總絹 = 隊將數 * 队將給絹
散兵總絹 = 散兵數 * 散兵給絹

# 總絹數
總絹 = 大將總絹 + 裨將總絹 + 隊將總絹 + 散兵總絹

# 疋法 (1 疋 = 50 尺)
疋法 = 50

# 計算疋數與剩餘尺數
a = 總絹 // 疋法  # 疋數
b = 總絹 % 疋法   # 剩餘尺數

a, b  # 答案: a 疋 奇 b 文#----- content ends here -----

"""
Code error: name '队將給絹' is not defined"""
