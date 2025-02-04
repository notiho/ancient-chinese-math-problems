"""
今有人盗馬乗去已行三十七里馬主乃覺追之一百四十五里不及二十三里而還今不還追之問㡬何里及之
術曰置不及里數以馬主追里數乗之為實以不及里數減已行里數餘為法實如法而一
答曰 a里
"""

#----- content starts here -----
"""
Suppose someone steals a horse and rides away, traveling 37 li. The horse's owner notices and chases after them for 145 li but falls short by 23 li before returning. 
Now, if the owner does not return but continues the chase, how many li will it take to catch up?

The procedure says: Place the number of li by which the owner falls short. Multiply it by the number of li the owner chased, obtaining the dividend.
Subtract the number of li already traveled by the thief from the number of li by which the owner falls short, obtaining the divisor.
Divide the dividend by the divisor, obtaining the number of li required to catch up.

Answer: *a* li.
"""

# 已行三十七里
已行里數 = 37

# 馬主追之一百四十五里
追里數 = 145

# 不及二十三里
不及里數 = 23

# 置不及里數，以馬主追里數乘之，為實
實 = 不及里數 * 追里數

# 以不及里數減已行里數，餘為法
法 = 不及里數 - 已行里數

# 實如法而一
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3335/14, Actual: -3335/14"""
