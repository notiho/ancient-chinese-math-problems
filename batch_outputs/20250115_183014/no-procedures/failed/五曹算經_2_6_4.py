"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
答曰： a疋 奇 b文 。
"""

"""
Suppose there are 10,000 people in total, consisting of:
- 10 generals (大將), each receiving 3 zhang of silk,
- 20 vice generals (裨將), each receiving 2 zhang of silk,
- 100 squad leaders (隊將), each receiving 1 zhang 5 chi of silk,
- 9,870 soldiers (散兵), each receiving 9 chi of silk.

Question: How much silk is needed in total?
Answer: *a* bolts (疋) and *b* wen (文) of silk.
"""

from fractions import Fraction

# Define the number of people in each rank
大將 = 10
裨將 = 20
隊將 = 100
散兵 = 9870

# Define the silk given to each rank (in chi)
# 1 zhang = 10 chi
大將_每人 = 3 * 10  # 3 zhang = 30 chi
裨將_每人 = 2 * 10  # 2 zhang = 20 chi
隊將_每人 = 1 * 10 + 5  # 1 zhang 5 chi = 15 chi
散兵_每人 = 9  # 9 chi

# Calculate the total silk required (in chi)
總絹_尺 = (
    大將 * 大將_每人 +
    裨將 * 裨將_每人 +
    隊將 * 隊將_每人 +
    散兵 * 散兵_每人
)

# Convert chi to bolts (疋) and remaining chi
# 1 bolt (疋) = 50 chi
a = 總絹_尺 // 50  # Number of bolts
b = 總絹_尺 % 50  # Remaining chi

# Output the result
a, b
"""
Variable 'a' has wrong value. Expected: 2275, Actual: 1820
Variable 'b' has wrong value. Expected: 3, Actual: 30"""
