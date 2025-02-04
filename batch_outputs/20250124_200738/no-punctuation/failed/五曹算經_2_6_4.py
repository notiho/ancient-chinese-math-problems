"""
今有一萬人大將十人裨將二十人隊將一百人散兵九千八百七十人給絹有差大將人給三丈裨將人給二丈隊將人給一丈五尺散兵人給九尺問計㡬何
術曰列大將十人以三十尺乘之得三百尺又列裨將二十人以二十尺乘之得四百尺又列隊將一百人以一十五尺乘之得一千五百尺又列散兵九千八百七十人以九尺乘之得八萬八千八百三十尺并四位得九萬一千三十尺以疋法除之即得
答曰 a疋 奇 b文 
"""

#----- content starts here -----
"""
Suppose there are 10,000 people: 10 are generals (Da Jiang), 20 are deputy generals (Pi Jiang), 100 are squad leaders (Dui Jiang), and 9,870 are ordinary soldiers (San Bing).
They are to be given silk, with differences in allocation:
- Each general receives 3 zhang (30 chi),
- Each deputy general receives 2 zhang (20 chi),
- Each squad leader receives 1 zhang 5 chi (15 chi),
- Each ordinary soldier receives 9 chi.

Question: What is the total amount of silk in bolts (疋) and leftover chi (文)?

The procedure says:
- List the 10 generals and multiply by 30 chi, obtaining 300 chi.
- List the 20 deputy generals and multiply by 20 chi, obtaining 400 chi.
- List the 100 squad leaders and multiply by 15 chi, obtaining 1,500 chi.
- List the 9,870 ordinary soldiers and multiply by 9 chi, obtaining 88,830 chi.
- Add the four results together, obtaining 91,030 chi.
- Divide by the bolt standard (疋法), which is 240 chi per bolt, to obtain the number of bolts and leftover chi.

Answer: *a* bolts, with *b* chi remaining.
"""

# 大將十人，每人給三丈 (30尺)
大將人數 = 10
大將每人給 = 30
大將總給 = 大將人數 * 大將每人給

# 裨將二十人，每人給二丈 (20尺)
裨將人數 = 20
裨將每人給 = 20
裨將總給 = 裨將人數 * 裨將每人給

# 隊將一百人，每人給一丈五尺 (15尺)
隊將人數 = 100
隊將每人給 = 15
隊將總給 = 隊將人數 * 隊將每人給

# 散兵九千八百七十人，每人給九尺
散兵人數 = 9870
散兵每人給 = 9
散兵總給 = 散兵人數 * 散兵每人給

# 合計總尺數
總尺數 = 大將總給 + 裨將總給 + 隊將總給 + 散兵總給

# 疋法 (每疋240尺)
疋法 = 240

# 計算疋數和剩餘尺數
a = 總尺數 // 疋法  # 疋數
b = 總尺數 % 疋法   # 剩餘尺數 (文)

a, b  # 答案: a疋, 奇b文#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2275, Actual: 379
Variable 'b' has wrong value. Expected: 3, Actual: 70"""
