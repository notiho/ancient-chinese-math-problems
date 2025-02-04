"""
今有一萬人大將十人裨將二十人隊將一百人散兵九千八百七十人給絹有差大將人給三丈裨將人給二丈隊將人給一丈五尺散兵人給九尺問計㡬何
術曰列大將十人以三十尺乘之得三百尺又列裨將二十人以二十尺乘之得四百尺又列隊將一百人以一十五尺乘之得一千五百尺又列散兵九千八百七十人以九尺乘之得八萬八千八百三十尺并四位得九萬一千三十尺以疋法除之即得
答曰 a疋 奇 b文 
"""

#----- content starts here -----
"""
Suppose there are 10,000 people consisting of 10 generals, 20 vice-generals, 100 squad leaders, and 9,870 soldiers.
They are to be given silk in varying amounts:
- Each general is given 3 zhang (30 chi),
- Each vice-general is given 2 zhang (20 chi),
- Each squad leader is given 1 zhang 5 chi (15 chi),
- Each soldier is given 9 chi.

Question: How many bolts of silk (pi) and leftover chi (wen) are required?

The procedure says:
- List the 10 generals and multiply by 30 chi, obtaining 300 chi.
- List the 20 vice-generals and multiply by 20 chi, obtaining 400 chi.
- List the 100 squad leaders and multiply by 15 chi, obtaining 1,500 chi.
- List the 9,870 soldiers and multiply by 9 chi, obtaining 88,830 chi.
- Add the four results together, obtaining 91,030 chi.
- Divide by the bolt standard (pi), which is 240 chi, to obtain the number of bolts and the remainder.

Answer: *a* bolts (pi), with *b* chi (wen) left over.
"""

# 大將十人，每人給三丈 (30尺)
大將數 = 10
大將每人 = 30
大將總 = 大將數 * 大將每人

# 裨將二十人，每人給二丈 (20尺)
裨將數 = 20
裨將每人 = 20
裨將總 = 裨將數 * 裨將每人

# 隊將一百人，每人給一丈五尺 (15尺)
隊將數 = 100
隊將每人 = 15
隊將總 = 隊將數 * 隊將每人

# 散兵九千八百七十人，每人給九尺
散兵數 = 9870
散兵每人 = 9
散兵總 = 散兵數 * 散兵每人

# 并四位得總尺數
總尺數 = 大將總 + 裨將總 + 隊將總 + 散兵總

# 疋法 (每疋 240尺)
疋法 = 240

# 以疋法除之，得疋數和餘尺數
a = 總尺數 // 疋法  # 疋數
b = 總尺數 % 疋法   # 餘尺數 (文)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2275, Actual: 379
Variable 'b' has wrong value. Expected: 3, Actual: 70"""
