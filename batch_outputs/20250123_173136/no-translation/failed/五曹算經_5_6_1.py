"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
術曰：列錢一百三十一貫八百一十文為實，并絲貴賤價得九十八文為法，以法除實得絲一千三百四十五两以十六两除之得八十四斤餘一两次置之以三十斤除之即得。
答曰：各 a鈞 。
"""

"""
To solve this problem, let's break it down step by step and translate the procedure into Python code:


"""


from fractions import Fraction

# 貴絲一两直錢五十六文
貴絲價 = 56

# 賤絲一两直錢四十二文
賤絲價 = 42

# 有錢一百三十一貫八百一十文
總錢 = 131 * 1000 + 810  # Convert 貫 and 文 to total 文

# 並絲貴賤價得九十八文為法
法 = 貴絲價 + 賤絲價

# 以法除實得絲一千三百四十五两
總絲兩 = Fraction(總錢, 法)

# 以十六两除之得八十四斤餘一两
總絲斤 = 總絲兩 // 16  # Whole number of 斤
餘兩 = 總絲兩 % 16      # Remaining 两

# 次置之以三十斤除之即得
貴絲斤 = Fraction(貴絲價 * 總絲兩, 法) // 16
賤絲斤 = 總絲斤 - 貴絲斤

# 答案
a = 貴絲斤
b = 賤絲斤

print(f"貴絲得 {a} 鈞，賤絲得 {b} 鈞。")


"""


### Explanation of the Code:
1. **Convert 貫 and 文 to total 文**: Since 1 貫 = 1000 文, we calculate the total money in 文.
2. **法**: The sum of the prices of 貴絲 and 賤絲 per 两.
3. **總絲兩**: Divide the total money by the 法 to get the total 两 of silk.
4. **Convert 两 to 斤 and 两**: Since 1 斤 = 16 两, we calculate the whole number of 斤 and the remaining 两.
5. **Distribute silk**: Use the ratio of 貴絲價 and 賤絲價 to distribute the total silk between 貴絲 and 賤絲.

This code will calculate the amount of 貴絲 and 賤絲 in 鈞 (斤).
"""


"""
Variable 'a' has wrong value. Expected: 269/96, Actual: 48"""
