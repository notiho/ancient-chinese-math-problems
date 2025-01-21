"""
今有北鄉算八千七百五十八西鄉算七千二百三十六南鄉算八千三百五十六凡三鄉發傜三百七十八人欲以算數多少衰出之問各幾何
術曰各置算數為列衰副并為法以所發傜人數乘未并者各自為實實如法得一人
荅曰北鄉遣 a人 西鄉遣 b人 南鄉遣 c人 
"""

"""
Suppose there are three regions: Beixiang (North Region), Xixiang (West Region), and Nanxiang (South Region).
The counts of people in each region are as follows:
Beixiang: 8758
Xixiang: 7236
Nanxiang: 8356
In total, 378 people are to be conscripted.
Question: How many people should each region contribute, proportional to their population?

The procedure says: Place the population counts of each region in a line.
Add them together to form the divisor.
Multiply the total number of conscripted people by the population count of each region (excluding the sum).
Each becomes its own dividend.
Divide each dividend by the divisor to obtain the number of conscripted people for each region.

Answer: Beixiang sends *a* people, Xixiang sends *b* people, Nanxiang sends *c* people.
"""

# 各置算數為列
北鄉 = 8758
西鄉 = 7236
南鄉 = 8356

# 衰副并為法
法 = 北鄉 + 西鄉 + 南鄉

# 以所發傜人數乘未并者
所發傜 = 378
北鄉實 = 所發傜 * 北鄉
西鄉實 = 所發傜 * 西鄉
南鄉實 = 所發傜 * 南鄉

# 各自為實，實如法得一人
a = Fraction(北鄉實, 法)
b = Fraction(西鄉實, 法)
c = Fraction(南鄉實, 法)
"""
"""
