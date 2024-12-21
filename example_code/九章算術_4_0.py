#今有田廣一步半求田一畝問從幾何
#術曰下有半是二分之一以一爲二半爲一并之得三爲法置田二百四十步亦以一爲二乘之爲實實如法得從步
#荅曰 a步

"""
Suppose there is a field with a width of one bu and a half. A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is a half, that is, 1/2. 
Take 1 as 2, and a half as 1.
Add these, obtaining 3 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 2, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

# 廣一步半
廣 = 1 + Fraction(1, 2)

# 田一畝
田 = 1

# 以一爲二
一 = 2
# 半爲一
半 = 1
# 并之得三爲法
法 = 一 + 半

# 置田二百四十步
田 = 240

# 亦以一爲二乘之爲實
實 = 2 * 田

# 實如法得從步
a = Fraction(實, 法)
