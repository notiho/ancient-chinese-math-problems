"""
今有北鄉算八千七百五十八西鄉算七千二百三十六南鄉算八千三百五十六凡三鄉發傜三百七十八人欲以算數多少衰出之問各幾何
術曰各置算數為列衰副并為法以所發傜人數乘未并者各自為實實如法得一人
荅曰北鄉遣 a人 西鄉遣 b人 南鄉遣 c人 
"""

"""
Suppose there are three regions: Beixiang (North Region) with 8758 suan, Xixiang (West Region) with 7236 suan, and Nanxiang (South Region) with 8356 suan.
In total, 378 people are to be conscripted for labor, distributed proportionally based on the suan numbers of each region.

The procedure says: Place the suan numbers of each region in a line.
In auxiliary, add them together to obtain the divisor.
Multiply the total number of conscripted people by the suan numbers that have not been added together, making each of them a dividend.
Do the division, obtaining the number of conscripted people for each region.

The answer says: Beixiang sends *a* people, Xixiang sends *b* people, Nanxiang sends *c* people.
"""

# 北鄉算八千七百五十八
北鄉算 = 8758

# 西鄉算七千二百三十六
西鄉算 = 7236

# 南鄉算八千三百五十六
南鄉算 = 8356

# 凡三鄉發傜三百七十八人
發傜人數 = 378

# 各置算數為列
算數 = [北鄉算, 西鄉算, 南鄉算]

# 衰副并為法
法 = sum(算數)

# 以所發傜人數乘未并者各自為實
實 = [發傜人數 * i for i in 算數]

# 實如法得一人
a, b, c = [Fraction(i, 法) for i in 實]
"""
"""
