"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
答曰： a疋 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 10,000 people in total, consisting of:
- 10 generals (大將), each receiving 3 zhang of silk,
- 20 vice-generals (裨將), each receiving 2 zhang of silk,
- 100 squad leaders (隊將), each receiving 1 zhang 5 chi of silk,
- 9,870 soldiers (散兵), each receiving 9 chi of silk.

Question: How much silk is needed in total, expressed in bolts (疋) and leftover silk in wen (文)?

Answer: *a* bolts (疋) and *b* wen (文).
"""

from fractions import Fraction

# Define the number of people in each category
大將 = 10
裨將 = 20
隊將 = 100
散兵 = 9870

# Define the silk allocation for each person in zhang and chi
大將_絹 = 3  # 3 zhang
裨將_絹 = 2  # 2 zhang
隊將_絹 = Fraction(15, 10)  # 1 zhang 5 chi = 1.5 zhang
散兵_絹 = Fraction(9, 10)  # 9 chi = 0.9 zhang

# Calculate the total silk needed in zhang
總絹 = (
    大將 * 大將_絹
    + 裨將 * 裨將_絹
    + 隊將 * 隊將_絹
    + 散兵 * 散兵_絹
)

# Convert zhang to bolts (疋) and leftover silk in wen (文)
# 1 bolt (疋) = 40 zhang
a = 總絹 // 40  # Number of full bolts
b = 總絹 % 40  # Remaining zhang (in wen)

# Output the results
a = int(a)
b = b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2275, Actual: 227
Variable 'b' has wrong value. Expected: 3, Actual: 23"""
