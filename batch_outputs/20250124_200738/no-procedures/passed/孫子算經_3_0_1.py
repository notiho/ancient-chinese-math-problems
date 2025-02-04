"""
今有甲、乙、丙、丁、戊、己、庚、辛、壬、癸九家共輸租，甲出三十五斛，乙出四十六斛，丙出五十七斛，丁出六十八斛，戊出七十九斛，己出八十斛，庚出一百斛，辛出二百一十斛，壬出三百二十五斛，凡九家，共輸租一千斛，僦運直折二百斛外。問：家各幾何？
答曰：甲 a斛 ，乙 b斛 ，丙 c斛 ，丁 d斛 ，戊 e斛 ，己 f斛 ，庚 g斛 ，辛 h斛 ，壬 i斛 。
"""

#----- content starts here -----
"""
There are 10 families (甲, 乙, 丙, 丁, 戊, 己, 庚, 辛, 壬) who collectively pay rent. 
The rent paid by each family is as follows:
甲 pays 35 hu, 乙 pays 46 hu, 丙 pays 57 hu, 丁 pays 68 hu, 戊 pays 79 hu, 己 pays 80 hu, 庚 pays 100 hu, 辛 pays 210 hu, 壬 pays 325 hu.
In total, they collectively pay 1000 hu of rent. After deducting transportation costs of 200 hu, the remaining rent is distributed proportionally among the families.

Question: How much rent does each family contribute after deducting transportation costs?

Answer: 甲 contributes *a* hu, 乙 contributes *b* hu, 丙 contributes *c* hu, 丁 contributes *d* hu, 戊 contributes *e* hu, 己 contributes *f* hu, 庚 contributes *g* hu, 辛 contributes *h* hu, 壬 contributes *i* hu.
"""

# Rent paid by each family
甲 = 35
乙 = 46
丙 = 57
丁 = 68
戊 = 79
己 = 80
庚 = 100
辛 = 210
壬 = 325

# Total rent paid
total_rent = 甲 + 乙 + 丙 + 丁 + 戊 + 己 + 庚 + 辛 + 壬

# Transportation cost deducted
transport_cost = 200

# Remaining rent to distribute
remaining_rent = total_rent - transport_cost

# Proportional distribution of remaining rent
a = Fraction(甲 * remaining_rent, total_rent)
b = Fraction(乙 * remaining_rent, total_rent)
c = Fraction(丙 * remaining_rent, total_rent)
d = Fraction(丁 * remaining_rent, total_rent)
e = Fraction(戊 * remaining_rent, total_rent)
f = Fraction(己 * remaining_rent, total_rent)
g = Fraction(庚 * remaining_rent, total_rent)
h = Fraction(辛 * remaining_rent, total_rent)
i = Fraction(壬 * remaining_rent, total_rent)

# Results
a, b, c, d, e, f, g, h, i#----- content ends here -----

"""
"""
