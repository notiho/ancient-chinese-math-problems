"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
答曰： a疋 奇 b文 。
"""

"""
Suppose there are 10,000 people in total:
- 10 are "Da Jiang" (Generals), each receives 3 zhang of silk.
- 20 are "Pi Jiang" (Deputy Generals), each receives 2 zhang of silk.
- 100 are "Dui Jiang" (Unit Leaders), each receives 1 zhang 5 chi of silk.
- 9,870 are "San Bing" (Regular Soldiers), each receives 9 chi of silk.

Question: How much silk is needed in total?
Answer: *a* bolts of silk, with *b* wen (units of silk) left over.
"""

from fractions import Fraction

# Define the number of people in each rank
大將 = 10
裨將 = 20
隊將 = 100
散兵 = 9870

# Define the amount of silk each rank receives
大將_絹 = 3  # 3 zhang
裨將_絹 = 2  # 2 zhang
隊將_絹 = Fraction(15, 10)  # 1 zhang 5 chi = 1.5 zhang
散兵_絹 = Fraction(9, 10)  # 9 chi = 0.9 zhang

# Calculate the total silk required for each rank
大將_總絹 = 大將 * 大將_絹
裨將_總絹 = 裨將 * 裨將_絹
隊將_總絹 = 隊將 * 隊將_絹
散兵_總絹 = 散兵 * 散兵_絹

# Calculate the total silk required
總絹 = 大將_總絹 + 裨將_總絹 + 隊將_總絹 + 散兵_總絹

# Convert the total silk into bolts (1 bolt = 40 zhang)
a = 總絹 // 40  # Number of full bolts
b = 總絹 % 40  # Remaining silk in zhang

a = int(a)  # Convert to integer for bolts
b = float(b)  # Remaining silk in zhang

a, b
"""
Variable 'a' has wrong value. Expected: 2275, Actual: 227
Variable 'b' has wrong value. Expected: 3, Actual: 23.0"""
