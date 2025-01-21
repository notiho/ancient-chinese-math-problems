"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a疋 奇 b文 。
"""

"""
Suppose there are 10,000 people consisting of:
- 10 generals (大將),
- 20 deputy generals (裨將),
- 100 squad leaders (隊將),
- 9,870 ordinary soldiers (散兵).

The distribution of silk varies:
- Each general receives 3 zhang (30 chi),
- Each deputy general receives 2 zhang (20 chi),
- Each squad leader receives 1 zhang 5 chi (15 chi),
- Each ordinary soldier receives 9 chi.

Question: How much silk is required in total?

The procedure says:
- List the 10 generals, multiply by 30 chi, obtaining 300 chi.
- List the 20 deputy generals, multiply by 20 chi, obtaining 400 chi.
- List the 100 squad leaders, multiply by 15 chi, obtaining 1,500 chi.
- List the 9,870 ordinary soldiers, multiply by 9 chi, obtaining 88,830 chi.
- Add the four results, obtaining 91,030 chi.
- Divide by the silk unit (疋法) to get the total number of bolts of silk.

Answer: *a* bolts (疋) and *b* chi (文) remaining.
"""

# 大將十人，以三十尺乘之
大將人數 = 10
大將每人絹 = 30  # 尺
大將總絹 = 大將人數 * 大將每人絹

# 裨將二十人，以二十尺乘之
裨將人數 = 20
裨將每人絹 = 20  # 尺
裨將總絹 = 裨將人數 * 裨將每人絹

# 隊將一百人，以一十五尺乘之
隊將人數 = 100
隊將每人絹 = 15  # 尺
隊將總絹 = 隊將人數 * 隊將每人絹

# 散兵九千八百七十人，以九尺乘之
散兵人數 = 9870
散兵每人絹 = 9  # 尺
散兵總絹 = 散兵人數 * 散兵每人絹

# 并四位得九萬一千三十尺
總絹 = 大將總絹 + 裨將總絹 + 隊將總絹 + 散兵總絹

# 疋法：一疋等於五十尺
疋法 = 50  # 尺

# 以疋法除之即得
a = 總絹 // 疋法  # 疋 (整數部分)
b = 總絹 % 疋法   # 文 (餘數部分 in 尺)
"""
Variable 'a' has wrong value. Expected: 2275, Actual: 1820
Variable 'b' has wrong value. Expected: 3, Actual: 30"""
