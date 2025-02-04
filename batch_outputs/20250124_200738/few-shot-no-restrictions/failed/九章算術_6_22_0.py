"""
今有一人一日矯矢五十，一人一日羽矢三十，一人一日筈矢十五。今令一人一日自矯、羽、筈，問︰成矢幾何？
術曰：矯矢五十，用徒一人。羽矢五十，用徒一人、太半人。筈矢五十，用徒三人、少半人。并之，得六人，以為法。以五十矢為實。實如法得一矢。
荅曰： a矢 。
"""

#----- content starts here -----
"""
Suppose one person in one day can straighten 50 arrows, one person in one day can fletch 30 arrows, and one person in one day can notch 15 arrows.
Now, let one person in one day straighten, fletch, and notch arrows by themselves.
Question: how many arrows can they complete in one day?

The procedure says: Straightening 50 arrows requires 1 person. Fletching 50 arrows requires 1 person and half a person more. Notching 50 arrows requires 3 people and half a person less.
Add these together, obtaining 6 people as the divisor.
Take 50 arrows as the dividend.
Divide the dividend by the divisor to obtain the number of arrows completed in one day.

Answer: *a* arrows.
"""

from fractions import Fraction

# 矯矢五十，用徒一人
矯率 = 1  # 1 person for 50 arrows

# 羽矢五十，用徒一人、太半人
羽率 = 1 + Fraction(1, 2)  # 1.5 people for 50 arrows

# 筈矢五十，用徒三人、少半人
筈率 = 3 - Fraction(1, 2)  # 2.5 people for 50 arrows

# 并之，得六人，以為法
法 = 矯率 + 羽率 + 筈率  # Total people required for 50 arrows

# 以五十矢為實
實 = 50  # 50 arrows as the base

# 實如法得一矢
a = Fraction(實, 法)  # Number of arrows completed in one day

a  # Output the result#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 25/3, Actual: 10"""
