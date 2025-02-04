"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a疋 奇 b文 。
"""

"""
To solve this problem, we will calculate the total amount of silk required for the given number of people in each category and then convert the total length into bolts ("疋") and leftover lengths in "文" (1 bolt = 40丈, 1丈 = 10尺). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
大將 = 10
裨將 = 20
隊將 = 100
散兵 = 9870

# Silk allocation per person
大將_給 = 3 * 10  # 3丈 = 30尺
裨將_給 = 2 * 10  # 2丈 = 20尺
隊將_給 = 1.5 * 10  # 1丈5尺 = 15尺
散兵_給 = 9  # 9尺

# Calculate total silk required in 尺
total_silk = (大將 * 大將_給) + (裨將 * 裨將_給) + (隊將 * 队將_給) + (散兵 * 散兵_給)

# Convert total silk to bolts (疋) and leftover lengths in 文
丈_per_疋 = 40
尺_per_丈 = 10
尺_per_疋 = 丈_per_疋 * 尺_per_丈

a = total_silk // 尺_per_疋  # Number of bolts (疋)
b = total_silk % 尺_per_疋  # Remaining length in 尺

# Output the results
a = Fraction(a)  # Number of bolts (疋)
b = Fraction(b)  # Remaining length in 尺
#----- content ends here -----


"""


After running this code, the variables `a` and `b` will contain the number of bolts (`疋`) and the leftover length in `尺` respectively.
"""


"""
Code error: name '队將_給' is not defined"""
