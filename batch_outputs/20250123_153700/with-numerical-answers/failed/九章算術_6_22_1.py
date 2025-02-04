"""
今有一人一日矯矢五十，一人一日羽矢三十，一人一日筈矢十五。今令一人一日自矯、羽、筈，問︰成矢幾何？
術曰：矯矢五十，用徒一人。羽矢五十，用徒一人、太半人。筈矢五十，用徒三人、少半人。并之，得六人，以為法。以五十矢為實。實如法得一矢。
荅曰： a(=25/3)矢 。
"""

"""
Suppose one person in one day straightens 50 arrows, one person in one day feathers 30 arrows, and one person in one day notches 15 arrows.
Now, let one person in one day straighten, feather, and notch arrows by themselves.
Question: how many arrows can they complete?

The procedure says: Straightening 50 arrows requires 1 person. Feathering 50 arrows requires 1 person and half a person more. Notching 50 arrows requires 3 people and half a person less. Add these, obtaining 6 as the divisor. Take 50 arrows as the dividend. Do the division, obtaining the number of arrows completed by one person in one day.

Answer: *a*(=25/3) arrows.
"""

# 矯矢五十，用徒一人
矯矢率 = 1

# 羽矢五十，用徒一人、太半人
羽矢率 = 1 + Fraction(1, 2)

# 筈矢五十，用徒三人、少半人
筈矢率 = 3 - Fraction(1, 2)

# 并之，得六人，以為法
法 = 矯矢率 + 羽矢率 + 筈矢率

# 以五十矢為實
實 = 50

# 實如法得一矢
a = Fraction(實, 法) # 25/3
"""
Variable 'a' has wrong value. Expected: 25/3, Actual: 10"""
