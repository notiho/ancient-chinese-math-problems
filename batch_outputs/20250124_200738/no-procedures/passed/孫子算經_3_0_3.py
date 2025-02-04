"""
今有甲、乙、丙、丁、戊、己、庚、辛、壬、癸九家共輸租，甲出三十五斛，乙出四十六斛，丙出五十七斛，丁出六十八斛，戊出七十九斛，己出八十斛，庚出一百斛，辛出二百一十斛，壬出三百二十五斛，凡九家，共輸租一千斛，僦運直折二百斛外。問：家各幾何？
答曰：甲 a斛 ，乙 b斛 ，丙 c斛 ，丁 d斛 ，戊 e斛 ，己 f斛 ，庚 g斛 ，辛 h斛 ，壬 i斛 。
"""

#----- content starts here -----
"""
There are 10 families (甲, 乙, 丙, 丁, 戊, 己, 庚, 辛, 壬) who collectively pay a total rent of 1000 hu.  
The transportation cost is deducted as 200 hu, leaving 800 hu to be distributed proportionally based on their original contributions.

The original contributions are as follows:
甲: 35 hu, 乙: 46 hu, 丙: 57 hu, 丁: 68 hu, 戊: 79 hu, 己: 80 hu, 庚: 100 hu, 辛: 210 hu, 壬: 325 hu.

Question: How much does each family pay after deducting the transportation cost?

Answer: 甲 pays *a* hu, 乙 pays *b* hu, 丙 pays *c* hu, 丁 pays *d* hu, 戊 pays *e* hu, 己 pays *f* hu, 庚 pays *g* hu, 辛 pays *h* hu, 壬 pays *i* hu.
"""

from fractions import Fraction

# Original contributions
contributions = [35, 46, 57, 68, 79, 80, 100, 210, 325]

# Total rent after deducting transportation cost
total_rent = 1000 - 200

# Total original contributions
total_contributions = sum(contributions)

# Calculate proportional rent for each family
proportional_rent = [Fraction(contribution * total_rent, total_contributions) for contribution in contributions]

# Assign results to variables
a, b, c, d, e, f, g, h, i = proportional_rent

# Results
a, b, c, d, e, f, g, h, i#----- content ends here -----

"""
"""
