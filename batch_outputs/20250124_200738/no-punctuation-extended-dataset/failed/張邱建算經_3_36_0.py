"""
今有婦人於河上蕩杯津吏問曰杯何以多婦人
術曰列置共杯人數於右方又共置共杯數於左方以人數互乘杯數併以為法令人數相乘以乘杯數為實實如法得一
答曰家中有客不知其數但 a人 共醬 b人 共羮 c人 共飯凡用杯 d 問人幾何答曰 e人
"""

#----- content starts here -----
"""
Suppose there is a woman by the river washing cups. The ferry officer asks: why are there so many cups for just one woman?

The procedure says: Place the total number of cups and the number of people on the right side.
Also place the total number of cups on the left side.
Multiply the number of people alternately with the number of cups, and combine them as the divisor.
Multiply the number of people with the cups to form the dividend.
Divide the dividend by the divisor to find the answer.

Answer: There are guests at home, but their number is unknown. However:
*a* people share the sauce,
*b* people share the soup,
*c* people share the rice,
and in total, *d* cups are used.
Question: how many people are there in total?
Answer: *e* people.
"""

# Input values
共醬 = a  # Number of people sharing the sauce
共羮 = b  # Number of people sharing the soup
共飯 = c  # Number of people sharing the rice
共杯 = d  # Total number of cups used

# Procedure
# 列置共杯人數於右方，又共置共杯數於左方
杯數 = [共醬, 共羮, 共飯]
人數 = [1, 1, 1]  # Each group represents one set of people sharing

# 以人數互乘杯數併以為法
法 = sum([人數[i] * 杯數[i] for i in range(len(杯數))])

# 令人數相乘以乘杯數為實
實 = sum([杯數[i] * 杯數[i] for i in range(len(杯數))])

# 實如法得一
e = Fraction(實, 法)#----- content ends here -----

"""
Code error: name 'a' is not defined"""
