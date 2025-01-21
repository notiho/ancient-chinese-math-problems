"""
今有婦人於河上蕩杯津吏問曰杯何以多婦人
術曰列置共杯人數於右方又共置共杯數於左方以人數互乘杯數併以為法令人數相乘以乘杯數為實實如法得一
答曰家中有客不知其數但 a人 共醬 b人 共羮 c人 共飯凡用杯 d 問人幾何答曰 e人
"""

"""
Suppose a woman is at the riverside washing cups. The official at the ferry asks: Why are there so many cups for just one woman?

The procedure says: Arrange the total number of cups and the total number of people on the right side. Also, arrange the total number of cups on the left side.
Multiply the number of people alternately with the number of cups, and combine them to form the divisor.
Multiply the number of people with the number of cups to form the dividend.
Perform the division to obtain the result.

Answer: There are guests at home, but their exact number is unknown. However:
*a* people share the sauce,
*b* people share the soup,
*c* people share the rice,
and in total, *d* cups are used.
Question: How many people are there in total?
Answer: *e* people.
"""

# Given data
共醬 = a  # Number of people sharing the sauce
共羮 = b  # Number of people sharing the soup
共飯 = c  # Number of people sharing the rice
共杯 = d  # Total number of cups used

# Procedure
# Arrange the total number of cups and people
杯數 = 共杯
人數 = 共醬 + 共羮 + 共飯

# Multiply the number of people alternately with the number of cups
法 = 共醬 * 共羮 + 共羮 * 共飯 + 共飯 * 共醬

# Multiply the number of people with the number of cups to form the dividend
實 = 杯數 * 人數

# Perform the division to obtain the total number of people
e = Fraction(實, 法)
"""
Code error: name 'a' is not defined"""
