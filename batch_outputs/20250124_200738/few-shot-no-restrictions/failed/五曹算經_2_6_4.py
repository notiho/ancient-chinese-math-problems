"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a疋 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 10,000 people, including 10 generals, 20 deputy generals, 100 squad leaders, and 9,870 regular soldiers.
The distribution of silk varies: each general is given 3 zhang, each deputy general is given 2 zhang, each squad leader is given 1 zhang and 5 chi, and each regular soldier is given 9 chi.
Question: what is the total amount of silk distributed?

The procedure says:
- For the generals: multiply their count (10) by 30 chi (3 zhang = 30 chi), obtaining 300 chi.
- For the deputy generals: multiply their count (20) by 20 chi (2 zhang = 20 chi), obtaining 400 chi.
- For the squad leaders: multiply their count (100) by 15 chi (1 zhang 5 chi = 15 chi), obtaining 1,500 chi.
- For the regular soldiers: multiply their count (9,870) by 9 chi, obtaining 88,830 chi.
- Add all four results together, obtaining the total in chi.
- Divide the total by the silk unit (1 bolt = 240 chi) to get the number of bolts and the remainder in chi.

Answer: *a* bolts and *b* chi.
"""

from fractions import Fraction

# Constants
疋法 = 240  # 1 bolt = 240 chi

# Counts of each group
大將人數 = 10
裨將人數 = 20
隊將人數 = 100
散兵人數 = 9870

# Silk allocation per person (in chi)
大將配給 = 30  # 3 zhang = 30 chi
裨將配給 = 20  # 2 zhang = 20 chi
隊將配給 = 15  # 1 zhang 5 chi = 15 chi
散兵配給 = 9   # 9 chi

# Calculate total silk for each group
大將總配給 = 大將人數 * 大將配給
裨將總配給 = 裨將人數 * 裨將配給
隊將總配給 = 隊將人數 * 队將配給
散兵總配給 = 散兵人數 * 散兵配給

# Total silk in chi
總配給 = 大將總配給 + 裨將總配給 + 隊將總配給 + 散兵總配給

# Convert total chi into bolts and remainder chi
a = 總配給 // 疋法  # Number of bolts
b = 總配給 % 疋法   # Remaining chi

# Output the results
a, b#----- content ends here -----

"""
Code error: name '队將配給' is not defined"""
