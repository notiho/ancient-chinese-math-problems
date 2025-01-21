"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 b 絫 c黍 奇 d銖 e黍 。
"""

"""
To solve this problem, we will calculate how much silk each household gets. The problem involves converting the total silk weight into smaller units (銖 and 黍) and then dividing it among the households.

1斤 = 16两  
1两 = 24銖  
1銖 = 10黍  

The total silk is 27斤5两. First, we convert this into 銖 and 黍, then divide it by the number of households (738). Finally, we express the result in terms of 銖, 絫 (24銖), 黍, and 奇 (remainder).

Here is the Python code:


"""


from fractions import Fraction

# Total silk in jin and liang
total_jin = 27
total_liang = 5

# Conversion factors
liang_to_zhu = 24
zhu_to_shu = 10
jin_to_liang = 16

# Total households
households = 738

# Convert total silk to 銖
total_liang_in_jin = total_jin * jin_to_liang
total_liang_combined = total_liang_in_jin + total_liang
total_zhu = total_liang_combined * liang_to_zhu

# Convert 銖 to 黍
total_shu = total_zhu * zhu_to_shu

# Divide by the number of households
shu_per_household = Fraction(total_shu, households)

# Convert back to 銖, 絫, 黍, 奇
a = shu_per_household // zhu_to_shu  # 銖
remaining_shu = shu_per_household % zhu_to_shu

b = a // liang_to_zhu  # 絫 (24銖)
a = a % liang_to_zhu

c = remaining_shu  # 黍
d = c // zhu_to_shu  # 奇 (銖)
e = c % zhu_to_shu  # 黍

# Results
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)


"""


The variables `a`, `b`, `c`, `d`, and `e` will contain the final answer in terms of 銖, 絫, 黍, 奇, and 黍 respectively.
"""


"""
Variable 'b' has wrong value. Expected: 2, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 2
Variable 'd' has wrong value. Expected: 1, Actual: 0"""
