"""
今有一萬人大將十人裨將二十人隊將一百人散兵九千八百七十人給絹有差大將人給三丈裨將人給二丈隊將人給一丈五尺散兵人給九尺問計㡬何
術曰列大將十人以三十尺乘之得三百尺又列裨將二十人以二十尺乘之得四百尺又列隊將一百人以一十五尺乘之得一千五百尺又列散兵九千八百七十人以九尺乘之得八萬八千八百三十尺并四位得九萬一千三十尺以疋法除之即得
答曰 a疋 奇 b文 
"""

"""
Suppose there are 10,000 people: 10 generals, 20 deputy generals, 100 squad leaders, and 9,870 ordinary soldiers.
They are to be given silk with differences in allocation:
- Each general is given 3 zhang (30 chi).
- Each deputy general is given 2 zhang (20 chi).
- Each squad leader is given 1 zhang 5 chi (15 chi).
- Each ordinary soldier is given 9 chi.

Question: how much silk in bolts (pi) and leftover chi (wen) is needed in total?

The procedure says:
List the 10 generals, multiply by 30 chi, obtaining 300 chi.
List the 20 deputy generals, multiply by 20 chi, obtaining 400 chi.
List the 100 squad leaders, multiply by 15 chi, obtaining 1,500 chi.
List the 9,870 ordinary soldiers, multiply by 9 chi, obtaining 88,830 chi.
Add the four results, obtaining 91,030 chi.
Divide by the bolt standard (pi), obtaining the number of bolts and leftover chi.

Answer: *a* bolts, with *b* chi remaining.
"""

# 大將十人，每人給三丈 (30尺)
大將數 = 10
大將給 = 30
大將總 = 大將數 * 大將給

# 裨將二十人，每人給二丈 (20尺)
裨將數 = 20
裨將給 = 20
裨將總 = 裨將數 * 裨將給

# 隊將一百人，每人給一丈五尺 (15尺)
隊將數 = 100
隊將給 = 15
隊將總 = 隊將數 * 隊將給

# 散兵九千八百七十人，每人給九尺
散兵數 = 9870
散兵給 = 9
散兵總 = 散兵數 * 散兵給

# 并四位得總尺數
總尺數 = 大將總 + 裨將總 + 隊將總 + 散兵總

# 疋法 (1疋 = 50尺)
疋法 = 50

# 以疋法除之，得疋數和剩餘尺數
a = 總尺數 // 疋法  # 疋數
b = 總尺數 % 疋法   # 剩餘尺數 (文)

a疋 = a
b文 = b
"""
Variable 'a' has wrong value. Expected: 2275, Actual: 1820
Variable 'b' has wrong value. Expected: 3, Actual: 30"""
