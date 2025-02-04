"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a疋 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 10,000 people: 10 generals, 20 vice-generals, 100 squad leaders, and 9,870 regular soldiers. 
They are to be allocated silk according to their ranks:
- Each general receives 3 zhang (30 chi),
- Each vice-general receives 2 zhang (20 chi),
- Each squad leader receives 1 zhang 5 chi (15 chi),
- Each regular soldier receives 9 chi.

Question: How much silk is needed in total?

The procedure says:
- Multiply the number of generals (10) by 30 chi, obtaining 300 chi.
- Multiply the number of vice-generals (20) by 20 chi, obtaining 400 chi.
- Multiply the number of squad leaders (100) by 15 chi, obtaining 1,500 chi.
- Multiply the number of regular soldiers (9,870) by 9 chi, obtaining 88,830 chi.
- Add these four results together to get the total chi: 91,030 chi.
- Divide the total by the silk bolt unit (疋法), which is 240 chi per bolt, to obtain the number of bolts and the remainder in chi.

Answer: *a* bolts and *b* chi.
"""

from fractions import Fraction

# Define the number of people in each rank
大將 = 10
裨將 = 20
隊將 = 100
散兵 = 9870

# Define the silk allocation per person in chi
大將配給 = 30  # 3丈 = 30尺
裨將配給 = 20  # 2丈 = 20尺
隊將配給 = 15  # 1丈5尺 = 15尺
散兵配給 = 9   # 9尺

# Calculate the total silk needed for each rank
大將總配給 = 大將 * 大將配給
裨將總配給 = 裨將 * 裨將配給
隊將總配給 = 隊將 * 队將配給
散兵總配給 = 散兵 * 散兵配給

# Calculate the total silk needed in chi
總配給 = 大將總配給 + 裨將總配給 + 隊將總配給 + 散兵總配給

# Define the silk bolt unit (疋法)
疋法 = 240  # 1疋 = 240尺

# Calculate the number of bolts and the remainder
a = 總配給 // 疋法  # Number of full bolts
b = 總配給 % 疋法  # Remaining chi

# Output the results
a, b#----- content ends here -----

"""
Code error: name '队將配給' is not defined"""
