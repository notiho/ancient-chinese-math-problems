"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
術曰：列錢一百三十一貫八百一十文為實，并絲貴賤價得九十八文為法，以法除實得絲一千三百四十五两以十六两除之得八十四斤餘一两次置之以三十斤除之即得。
答曰：各 a鈞 。
"""

"""
To solve this problem, let's translate the ancient Chinese mathematical procedure into Python code step by step.


"""

#----- content starts here -----

from fractions import Fraction

# 貴絲一两直錢五十六文
貴絲價 = 56

# 賤絲一两直錢四十二文
賤絲價 = 42

# 有錢一百三十一貫八百一十文
# 1 貫 = 1000 文
總錢 = 131 * 1000 + 810

# 并絲貴賤價得九十八文為法
法 = 貴絲價 + 賤絲價

# 以法除實得絲一千三百四十五两
總絲兩 = Fraction(總錢, 法)

# 以十六两除之得八十四斤餘一两
斤 = 總絲兩 // 16
餘兩 = 總絲兩 % 16

# 次置之以三十斤除之即得
# 貴絲與賤絲的比例是 56:42 = 4:3
貴絲比例 = 4
賤絲比例 = 3
總比例 = 貴絲比例 + 賤絲比例

貴絲斤 = Fraction(斤 * 貴絲比例, 總比例)
賤絲斤 = Fraction(斤 * 賤絲比例, 總比例)

a = 貴絲斤
b = 賤絲斤

print(f"貴絲得 {a} 鈞，賤絲得 {b} 鈞。")
#----- content ends here -----


"""
 

### Explanation:
1. **Convert 貫 to 文**: Since 1 貫 = 1000 文, the total money is converted into 文.
2. **法**: The combined price of 貴絲 and 賤絲 per 两 is used as the divisor.
3. **總絲兩**: Divide the total money by the combined price to get the total 两 of silk.
4. **斤 and 餘兩**: Convert 两 into 斤 (16 两 = 1 斤) and calculate the remainder.
5. **Proportion**: Distribute the total silk in the ratio of 貴絲價:賤絲價 (4:3).
6. **Output**: The result is expressed in 鈞 (斤).

Let me know if you need further clarification!
"""


"""
Variable 'a' has wrong value. Expected: 269/96, Actual: 48"""
