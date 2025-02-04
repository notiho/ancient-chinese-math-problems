"""
今有一萬人，大將十人，裨將二十人，隊將一百人，散兵九千八百七十人。給絹有差，大將人給三丈，裨將人給二丈，隊將人給一丈五尺，散兵人給九尺。問：計㡬何？
術曰：列大將十人，以三十尺乘之，得三百尺；又列裨將二十人，以二十尺乘之，得四百尺；又列隊將一百人，以一十五尺乘之，得一千五百尺；又列散兵九千八百七十人，以九尺乘之，得八萬八千八百三十尺。并四位得九萬一千三十尺，以疋法除之即得。
答曰： a疋 奇 b文 。
"""

"""
To solve this problem, we will calculate the total amount of silk required for all the people and then convert the total length into bolts ("疋") and leftover lengths in "文" (1 bolt = 40丈, 1丈 = 10尺). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
大將 = 10
裨將 = 20
隊將 = 100
散兵 = 9870

# Silk allocation per person
大將_給絹 = 30  # in 尺
裨將_給絹 = 20  # in 尺
隊將_給絹 = 15  # in 尺
散兵_給絹 = 9   # in 尺

# Calculate total silk required in 尺
total_silk = (大將 * 大將_給絹) + (裨將 * 裨將_給絹) + (隊將 * 隊將_給絹) + (散兵 * 散兵_給絹)

# Convert 尺 to bolts (疋) and leftover 尺
丈_per_疋 = 40  # 1 bolt = 40丈
尺_per_丈 = 10  # 1丈 = 10尺
尺_per_疋 = 丈_per_疋 * 尺_per_丈  # Total 尺 in 1 bolt

a = total_silk // 尺_per_疋  # Number of bolts (疋)
remaining_尺 = total_silk % 尺_per_疋  # Remaining 尺
b = Fraction(remaining_尺, 尺_per_疋)  # Remaining fraction of a bolt (文)

# Results
print(f"a = {a} 疋")
print(f"b = {b} 文")
#----- content ends here -----


"""


### Explanation:
1. We calculate the total silk required in 尺 by multiplying the number of people in each category by the silk allocation per person.
2. Convert the total silk from 尺 into bolts (疋) and leftover 尺.
3. The leftover 尺 is expressed as a fraction of a bolt (文).

### Output:
The variables `a` and `b` will hold the number of bolts and the leftover fraction, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 2275, Actual: 227
Variable 'b' has wrong value. Expected: 3, Actual: 23/40"""
