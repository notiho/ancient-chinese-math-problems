"""
今有一萬人大將十人裨將二十人隊將一百人散兵九千八百七十人給絹有差大將人給三丈裨將人給二丈隊將人給一丈五尺散兵人給九尺問計㡬何
術曰列大將十人以三十尺乘之得三百尺又列裨將二十人以二十尺乘之得四百尺又列隊將一百人以一十五尺乘之得一千五百尺又列散兵九千八百七十人以九尺乘之得八萬八千八百三十尺并四位得九萬一千三十尺以疋法除之即得
答曰 a疋 奇 b文 
"""

"""
Suppose there are 10,000 people: 10 are Da Jiang (Generals), 20 are Pi Jiang (Deputy Generals), 100 are Dui Jiang (Unit Leaders), and 9,870 are San Bing (Regular Soldiers).
They are to be given silk with differences in allocation:
- Each Da Jiang is given 3 zhang.
- Each Pi Jiang is given 2 zhang.
- Each Dui Jiang is given 1 zhang and 5 chi.
- Each San Bing is given 9 chi.

Question: What is the total amount of silk in bolts and leftover chi?

The procedure says:
- List the 10 Da Jiang and multiply by 30 chi (3 zhang = 30 chi), obtaining 300 chi.
- List the 20 Pi Jiang and multiply by 20 chi (2 zhang = 20 chi), obtaining 400 chi.
- List the 100 Dui Jiang and multiply by 15 chi (1 zhang 5 chi = 15 chi), obtaining 1,500 chi.
- List the 9,870 San Bing and multiply by 9 chi, obtaining 88,830 chi.
- Add the four results together, obtaining 91,030 chi.
- Divide by the bolt divisor (1 bolt = 240 chi) to obtain the number of bolts and the remainder.

Answer: *a* bolts, with *b* chi remaining.
"""

# 大將十人，每人給三丈 (30尺)
大將人數 = 10
大將每人給 = 30  # 尺
大將總給 = 大將人數 * 大將每人給

# 裨將二十人，每人給二丈 (20尺)
裨將人數 = 20
裨將每人給 = 20  # 尺
裨將總給 = 裨將人數 * 裨將每人給

# 隊將一百人，每人給一丈五尺 (15尺)
隊將人數 = 100
隊將每人給 = 15  # 尺
隊將總給 = 隊將人數 * 隊將每人給

# 散兵九千八百七十人，每人給九尺
散兵人數 = 9870
散兵每人給 = 9  # 尺
散兵總給 = 散兵人數 * 散兵每人給

# 合計總尺數
總尺數 = 大將總給 + 裨將總給 + 隊將總給 + 散兵總給

# 疋法 (1疋 = 240尺)
疋法 = 240

# 計算疋數和剩餘尺數
a = 總尺數 // 疋法  # 疋數
b = 總尺數 % 疋法  # 剩餘尺數
"""
Variable 'a' has wrong value. Expected: 2275, Actual: 379
Variable 'b' has wrong value. Expected: 3, Actual: 70"""
