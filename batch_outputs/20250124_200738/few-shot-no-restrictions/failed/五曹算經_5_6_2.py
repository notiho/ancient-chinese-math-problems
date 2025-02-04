"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
術曰：列錢一百三十一貫八百一十文為實，并絲貴賤價得九十八文為法，以法除實得絲一千三百四十五两以十六两除之得八十四斤餘一两次置之以三十斤除之即得。
答曰：各 a鈞 。
"""

#----- content starts here -----
"""
Suppose there is expensive silk, where 1 liang costs 56 wen, and cheap silk, where 1 liang costs 42 wen. 
There is a total of 131 guan and 810 wen. 
Question: how much of each type of silk can be obtained?

The procedure says: 
List the total money, 131 guan and 810 wen, as the dividend. 
Add the prices of the expensive and cheap silk, obtaining 98 wen as the divisor. 
Divide the dividend by the divisor, obtaining 1345 liang of silk. 
Divide this by 16 liang to get 84 jin, with 1 liang remaining. 
Then divide by 30 jin to determine the final answer.

Answer: each type of silk is *a* jun.
"""

from fractions import Fraction

# 貴絲一两直錢五十六文
貴絲價 = 56

# 賤絲一两直錢四十二文
賤絲價 = 42

# 有錢一百三十一貫八百一十文
總錢 = 131 * 1000 + 810  # Convert 131 guan and 810 wen to total wen

# 并絲貴賤價得九十八文為法
法 = 貴絲價 + 賤絲價

# 以法除實得絲一千三百四十五两
絲總量_兩 = Fraction(總錢, 法)

# 以十六两除之得八十四斤餘一两
絲總量_斤 = 丝總量_兩 // 16  # Integer division to get jin
餘量_兩 = 丝總量_兩 % 16  # Remainder in liang

# 次置之以三十斤除之即得
a = Fraction(丝總量_斤, 30)  # Divide by 30 jin to get jun

a#----- content ends here -----

"""
Code error: name '丝總量_兩' is not defined"""
