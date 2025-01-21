"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a疋 奇 b文 。
"""

"""
To solve the problem, we will calculate the total amount of silk required for all the soldiers and then convert the total length into bolts ("疋") and leftover lengths ("文"). A bolt of silk is 40 feet (疋法). Here's the Python code:


"""


from fractions import Fraction

# Given data
大將 = 10  # 大將人數
裨將 = 20  # 裨將人數
隊將 = 100  # 隊將人數
散兵 = 9870  # 散兵人數

# Silk allocation per person
大將_絹 = 30  # 大將每人給 30 尺
裨將_絹 = 20  # 裨將每人給 20 尺
隊將_絹 = 15  # 隊將每人給 15 尺
散兵_絹 = 9   # 散兵每人給 9 尺

# Total silk required
總絹 = (大將 * 大將_絹) + (裨將 * 裨將_絹) + (隊將 * 隊將_絹) + (散兵 * 散兵_絹)

# Convert total silk into bolts (疋) and leftover lengths (文)
疋法 = 40  # 1 疋 = 40 尺
a = 總絹 // 疋法  # Number of bolts
b = 總絹 % 疋法   # Remaining length in feet

# Results
a, b


"""


This code calculates the total silk required and then determines how many bolts ("疋") and leftover lengths ("文") are needed. The variables `a` and `b` store the final answers.
"""


"""
Variable 'b' has wrong value. Expected: 3, Actual: 30"""
