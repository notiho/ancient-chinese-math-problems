"""
今有絲九两得絹一疋，有絲三百二十四斤。問：計得㡬何？
術曰：列三百二十四斤，以十六两乘之，得五千一百八十四两；以九两除之即得。
答曰： a疋 。
"""

#----- content starts here -----
"""
Suppose there are 9 liang of silk that can produce 1 bolt of silk fabric (絹). 
Now, there are 324 jin of silk.
Question: how many bolts of silk fabric can be produced?

The procedure says: Multiply 324 jin by 16 liang (since 1 jin = 16 liang), obtaining the total number of liang.
Divide this total by 9 liang (the amount needed for 1 bolt of silk fabric) to get the result.

Answer: *a* bolts of silk fabric.
"""

from fractions import Fraction

# 絲九两得絹一疋
絲_per_疋 = 9  # 9 liang of silk per bolt of fabric

# 絲三百二十四斤
絲_jin = 324  # 324 jin of silk

# 1斤 = 16两
絲_liang = 絲_jin * 16  # Convert jin to liang

# 以九两除之即得
a = Fraction(絲_liang, 絲_per_疋)  # Calculate the number of bolts of silk fabric

a  # Output the result as a fraction#----- content ends here -----

"""
"""
