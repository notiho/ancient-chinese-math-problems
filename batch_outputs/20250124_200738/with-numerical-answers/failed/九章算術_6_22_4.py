"""
今有一人一日矯矢五十，一人一日羽矢三十，一人一日筈矢十五。今令一人一日自矯、羽、筈，問︰成矢幾何？
術曰：矯矢五十，用徒一人。羽矢五十，用徒一人、太半人。筈矢五十，用徒三人、少半人。并之，得六人，以為法。以五十矢為實。實如法得一矢。
荅曰： a(=25/3)矢 。
"""

#----- content starts here -----
"""
Suppose one person can straighten 50 arrows in one day, one person can fletch 30 arrows in one day, and one person can notch 15 arrows in one day.
Now, let one person straighten, fletch, and notch arrows in one day.
Question: how many completed arrows can they make?

The procedure says: Straightening 50 arrows requires 1 person.
Fletching 50 arrows requires 1 person and half a person more.
Notching 50 arrows requires 3 people and half a person less.
Add these, obtaining 6 people as the divisor.
Take 50 arrows as the dividend.
Divide the dividend by the divisor to obtain the number of completed arrows.

Answer: *a*(=25/3) arrows.
"""

# 矯矢五十，用徒一人
矯矢效率 = 1

# 羽矢五十，用徒一人、太半人 (1 + 1/2)
羽矢效率 = 1 + Fraction(1, 2)

# 筈矢五十，用徒三人、少半人 (3 - 1/2)
筈矢效率 = 3 - Fraction(1, 2)

# 并之，得六人，以為法
法 = 矯矢效率 + 羽矢效率 + 筈矢效率

# 以五十矢為實
實 = 50

# 實如法得一矢
a = Fraction(實, 法) # 25/3 arrows#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 25/3, Actual: 10"""
