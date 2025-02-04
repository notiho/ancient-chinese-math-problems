"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
答曰： a疋 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 10,000 people consisting of:
- 10 generals (大將), each receiving 3 zhang of silk,
- 20 vice generals (裨將), each receiving 2 zhang of silk,
- 100 squad leaders (隊將), each receiving 1 zhang 5 chi of silk,
- 9,870 soldiers (散兵), each receiving 9 chi of silk.

Question: How much silk is required in total? The answer is given in bolts (疋) and leftover silk in wen (文), where 1 bolt = 40 zhang.

Answer: *a* bolts and *b* wen.
"""

from fractions import Fraction

# Constants
大將數 = 10
裨將數 = 20
隊將數 = 100
散兵數 = 9870

大將每人絹 = 3  # zhang
裨將每人絹 = 2  # zhang
隊將每人絹 = 1 + Fraction(5, 10)  # 1 zhang 5 chi = 1.5 zhang
散兵每人絹 = Fraction(9, 10)  # 9 chi = 0.9 zhang

# Total silk required
總絹 = (
    大將數 * 大將每人絹 +
    裨將數 * 裨將每人絹 +
    隊將數 * 隊將每人絹 +
    散兵數 * 散兵每人絹
)

# Convert total silk into bolts and remaining silk
a = 總絹 // 40  # Number of bolts (疋)
b = 總絹 % 40  # Remaining silk in zhang (文)

a, b  # Output the result as bolts and leftover zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2275, Actual: 227
Variable 'b' has wrong value. Expected: 3, Actual: 23"""
