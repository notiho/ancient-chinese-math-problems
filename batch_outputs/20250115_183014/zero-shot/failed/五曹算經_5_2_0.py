"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 b 絫 c黍 奇 d銖 e黍 。
"""

"""
To solve this problem, we need to calculate how much silk each household gets. The total silk is given as 27斤5两, and there are 738 households. The units are as follows:

1 斤 = 16 两  
1 两 = 24 銖  
1 銖 = 10 黍  

The answer is expressed in terms of 銖, 絫 (24黍 = 1絫), 黍, and 奇 (remainder 銖 and 黍).

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Total silk in 两
total_silk_liang = 27 * 16 + 5  # Convert 27斤5两 to 两
# Total silk in 銖
total_silk_zhu = total_silk_liang * 24  # Convert 两 to 銖

# Silk per household in 銖
silk_per_household_zhu = Fraction(total_silk_zhu, 738)

# Convert to 銖, 絫, 黍, 奇
a = silk_per_household_zhu.numerator // silk_per_household_zhu.denominator  # 銖
remainder_zhu = silk_per_household_zhu - a  # Remaining 銖 as a fraction

b = (remainder_zhu * 10).numerator // (remainder_zhu * 10).denominator  # 絫 (24黍 = 1絫)
remainder_li = (remainder_zhu * 10) - b  # Remaining 黍 as a fraction

c = (remainder_li * 24).numerator // (remainder_li * 24).denominator  # 黍
remainder_mi = (remainder_li * 24) - c  # Remaining 奇 as a fraction

d = remainder_mi.numerator // remainder_mi.denominator  # 奇 銖
e = remainder_mi.numerator

"""

"""


"""
Variable 'c' has wrong value. Expected: 1, Actual: 2
Variable 'd' has wrong value. Expected: 1, Actual: 0
Variable 'e' has wrong value. Expected: 2, Actual: 30"""
