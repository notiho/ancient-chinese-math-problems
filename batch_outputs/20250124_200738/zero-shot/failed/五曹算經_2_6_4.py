"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a疋 奇 b文 。
"""

"""
To solve this problem, we will calculate the total amount of silk required for the given number of people in each rank, and then convert the total length into bolts of silk (`疋`) and leftover lengths in `尺` (converted to `文`).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
大將 = 10  # 大將人數
裨將 = 20  # 裨將人數
隊將 = 100  # 隊將人數
散兵 = 9870  # 散兵人數

# Silk allocation per person
大將_給絹 = 30  # 每人給 30 尺
裨將_給絹 = 20  # 每人給 20 尺
隊將_給絹 = 15  # 每人給 15 尺
散兵_給絹 = 9   # 每人給 9 尺

# Calculate total silk in 尺
total_silk = (大將 * 大將_給絹) + (裨將 * 裨將_給絹) + (隊將 * 隊將_給絹) + (散兵 * 散兵_給絹)

# Convert total silk to 疋 and 文
# 1 疋 = 240 尺
a = total_silk // 240  # Number of 疋
b = total_silk % 240   # Remaining 尺 (converted to 文)

# Output the results
a = Fraction(a)  # Number of 疋
b = Fraction(b)  # Remaining 文
#----- content ends here -----


"""


After running this code, the variables `a` and `b` will contain the number of bolts of silk (`疋`) and the leftover length in `文`, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 2275, Actual: 379
Variable 'b' has wrong value. Expected: 3, Actual: 70"""
