"""
今有邑方不知大小，各中開門。出北門二十步有木。出南門十四步，折而西行一千七百七十五步見木。問︰邑方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a square city (yi) of unknown size, with gates in the middle of each side.
From the north gate, walking 20 bu north leads to a tree.
From the south gate, walking 14 bu south, then turning west and walking 1775 bu, also leads to the same tree.
Question: what is the side length of the square city?

Answer: the side length is *a* bu.
"""

from fractions import Fraction

# Distance from the north gate to the tree
北門距離 = 20

# Distance from the south gate to the tree
南門距離 = 14

# Distance walked west from the south gate
西行距離 = 1775

# The side length of the square city (邑方) is the difference between the westward distance and the sum of the distances from the north and south gates to the tree
a = 西行距離 - (北門距離 + 南門距離)

# Convert to a Fraction for exact representation
a = Fraction(a)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 250, Actual: 1741"""
