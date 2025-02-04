"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a疋 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 10,000 people: 10 generals, 20 vice-generals, 100 squad leaders, and 9,870 regular soldiers.
They are to be given silk in varying amounts: each general is given 3 zhang, each vice-general is given 2 zhang, each squad leader is given 1 zhang and 5 chi, and each regular soldier is given 9 chi.
Question: how much silk is needed in total?

The procedure says:
- List the 10 generals, multiply by 30 chi (3 zhang = 30 chi), obtaining 300 chi.
- List the 20 vice-generals, multiply by 20 chi (2 zhang = 20 chi), obtaining 400 chi.
- List the 100 squad leaders, multiply by 15 chi (1 zhang 5 chi = 15 chi), obtaining 1,500 chi.
- List the 9,870 regular soldiers, multiply by 9 chi, obtaining 88,830 chi.
- Add the four results together, obtaining 91,030 chi.
- Divide by the silk bolt standard (疋法), obtaining the number of bolts and leftover chi.

Answer: *a* bolts and *b* chi.
"""

from fractions import Fraction

# Define the number of people in each category
大將 = 10
裨將 = 20
隊將 = 100
散兵 = 9870

# Define the silk allocation per person in chi
大將給 = 30  # 3 zhang = 30 chi
裨將給 = 20  # 2 zhang = 20 chi
隊將給 = 15  # 1 zhang 5 chi = 15 chi
散兵給 = 9   # 9 chi

# Calculate the total silk needed for each category
大將總 = 大將 * 大將給
裨將總 = 裨將 * 裨將給
隊將總 = 隊將 * 队將給
散兵總 = 散兵 * 散兵給

# Add up the total silk needed
總絹 = 大將總 + 裨將總 + 隊將總 + 散兵總

# Define the silk bolt standard (1 bolt = 240 chi)
疋法 = 240

# Calculate the number of bolts and leftover chi
a = 總絹 // 疋法  # Number of bolts
b = 總絹 % 疋法   # Leftover chi

# Output the results
a, b#----- content ends here -----

"""
Code error: name '队將給' is not defined"""
