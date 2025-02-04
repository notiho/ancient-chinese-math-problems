"""
今有一人一日矯矢五十，一人一日羽矢三十，一人一日筈矢十五。今令一人一日自矯、羽、筈，問︰成矢幾何？
術曰：矯矢五十，用徒一人。羽矢五十，用徒一人、太半人。筈矢五十，用徒三人、少半人。并之，得六人，以為法。以五十矢為實。實如法得一矢。
荅曰： a矢 。
"""

"""
Suppose one person in one day straightens 50 arrows, one person in one day feathers 30 arrows, and one person in one day notches 15 arrows.
Now, let one person in one day straighten, feather, and notch arrows by themselves.
Question: how many arrows can they complete in one day?

The procedure says: Straightening 50 arrows requires 1 person.
Feathering 50 arrows requires 1 person and more than half a person.
Notching 50 arrows requires 3 people and less than half a person.
Add these together, obtaining 6 people as the divisor.
Take 50 arrows as the dividend.
Do the division, obtaining the number of arrows completed in one day.

Answer: *a* arrows.
"""

# 矯矢五十，用徒一人
矯率 = 1

# 羽矢五十，用徒一人、太半人
羽率 = 1 + Fraction(1, 2)

# 筈矢五十，用徒三人、少半人
筈率 = 3 + Fraction(1, 2)

# 并之，得六人，以為法
法 = 矯率 + 羽率 + 筈率

# 以五十矢為實
實 = 50

# 實如法得一矢
a = Fraction(實, 法)
"""
"""
