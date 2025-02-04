"""
今有一人一日矯矢五十一人一日羽矢三十一人一日筈矢十五今令一人一日自矯羽筈問成矢幾何
術曰矯矢五十用徒一人羽矢五十用徒一人太半人筈矢五十用徒三人少半人并之得六人以為法以五十矢為實實如法得一矢
荅曰 a矢 
"""

#----- content starts here -----
"""
Suppose one person in one day straightens 50 arrows, one person in one day feathers 30 arrows, and one person in one day notches 15 arrows.
Now, let one person in one day straighten, feather, and notch arrows by themselves.
Question: how many arrows can they complete in one day?

The procedure says: Straightening 50 arrows requires 1 person.
Feathering 50 arrows requires 1 and a half people.
Notching 50 arrows requires 3 and a half people.
Add these, obtaining 6 people as the divisor.
Take 50 arrows as the dividend.
Divide the dividend by the divisor, obtaining the number of arrows completed by one person in one day.

The answer says: *a* arrows.
"""

# 矯矢五十用徒一人
矯率 = 1

# 羽矢五十用徒一人太半人
羽率 = 1 + Fraction(1, 2)

# 筈矢五十用徒三人少半人
筈率 = 3 + Fraction(1, 2)

# 并之得六人，以為法
法 = 矯率 + 羽率 + 筈率

# 以五十矢為實
實 = 50

# 實如法得一矢
a = Fraction(實, 法)#----- content ends here -----

"""
"""
