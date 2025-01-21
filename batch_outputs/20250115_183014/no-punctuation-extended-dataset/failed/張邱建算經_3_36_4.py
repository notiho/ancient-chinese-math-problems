"""
今有婦人於河上蕩杯津吏問曰杯何以多婦人
術曰列置共杯人數於右方又共置共杯數於左方以人數互乘杯數併以為法令人數相乘以乘杯數為實實如法得一
答曰家中有客不知其數但 a人 共醬 b人 共羮 c人 共飯凡用杯 d 問人幾何答曰 e人
"""

"""
Suppose there is a woman at the riverbank washing cups. A ferry officer asks: why are there so many cups for one woman?

The procedure says: Place the total number of cups and people on the right side. Also, place the total number of cups on the left side.
Multiply the number of people mutually with the number of cups, and combine them as the divisor.
Multiply the number of people mutually to calculate the cups used, and treat this as the dividend.
Divide the dividend by the divisor to obtain the result.

Answer: In the household, there are guests, but their number is unknown. However:
*a* people share sauce,
*b* people share soup,
*c* people share rice,
and in total, *d* cups are used.
Question: how many people are there in total?
Answer: *e* people.
"""

# Input values
共醬 = a  # Number of people sharing sauce
共羮 = b  # Number of people sharing soup
共飯 = c  # Number of people sharing rice
用杯 = d  # Total number of cups used

# Procedure
# 列置共杯人數於右方
右方 = [共醬, 共羮, 共飯]

# 又共置共杯數於左方
左方 = [用杯, 用杯, 用杯]

# 以人數互乘杯數併以為法
法 = 共醬 * 用杯 + 共羮 * 用杯 + 共飯 * 用杯

# 令人數相乘以乘杯數為實
實 = 共醬 * 共羮 * 共飯 * 用杯

# 實如法得一
e = Fraction(實, 法)
"""
Code error: name 'a' is not defined"""
