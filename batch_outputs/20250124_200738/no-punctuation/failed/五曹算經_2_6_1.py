"""
今有一萬人大將十人裨將二十人隊將一百人散兵九千八百七十人給絹有差大將人給三丈裨將人給二丈隊將人給一丈五尺散兵人給九尺問計㡬何
術曰列大將十人以三十尺乘之得三百尺又列裨將二十人以二十尺乘之得四百尺又列隊將一百人以一十五尺乘之得一千五百尺又列散兵九千八百七十人以九尺乘之得八萬八千八百三十尺并四位得九萬一千三十尺以疋法除之即得
答曰 a疋 奇 b文 
"""

#----- content starts here -----
"""
Suppose there are 10,000 people: 10 generals, 20 deputy generals, 100 squad leaders, and 9,870 regular soldiers.
They are to be given silk with differences in allocation:
Each general is given 3 zhang (30 chi), each deputy general is given 2 zhang (20 chi), each squad leader is given 1 zhang 5 chi (15 chi), and each regular soldier is given 9 chi.
Question: what is the total amount of silk in bolts and leftover chi?

The procedure says:
List the 10 generals and multiply by 30 chi, obtaining 300 chi.
List the 20 deputy generals and multiply by 20 chi, obtaining 400 chi.
List the 100 squad leaders and multiply by 15 chi, obtaining 1,500 chi.
List the 9,870 regular soldiers and multiply by 9 chi, obtaining 88,830 chi.
Add these four results, obtaining 91,030 chi.
Divide by the bolt standard (1 bolt = 240 chi), and the result is the number of bolts and leftover chi.

Answer: *a* bolts, with *b* chi remaining.
"""

# 大將十人
大將人數 = 10
大將配給 = 30  # 每人給 30 尺
大將總尺 = 大將人數 * 大將配給

# 裨將二十人
裨將人數 = 20
裨將配給 = 20  # 每人給 20 尺
裨將總尺 = 裨將人數 * 裨將配給

# 隊將一百人
隊將人數 = 100
隊將配給 = 15  # 每人給 15 尺
隊將總尺 = 隊將人數 * 隊將配給

# 散兵九千八百七十人
散兵人數 = 9870
散兵配給 = 9  # 每人給 9 尺
散兵總尺 = 散兵人數 * 散兵配給

# 并四位
總尺 = 大將總尺 + 裨將總尺 + 隊將總尺 + 散兵總尺

# 疋法
疋法 = 240  # 1 疋 = 240 尺

# 以疋法除之
a = 總尺 // 疋法  # 疋數
b = 總尺 % 疋法  # 剩餘尺數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2275, Actual: 379
Variable 'b' has wrong value. Expected: 3, Actual: 70"""
