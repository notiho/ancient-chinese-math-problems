"""
今有北鄉算八千七百五十八西鄉算七千二百三十六南鄉算八千三百五十六凡三鄉發傜三百七十八人欲以算數多少衰出之問各幾何
術曰各置算數為列衰副并為法以所發傜人數乘未并者各自為實實如法得一人
荅曰北鄉遣 a人 西鄉遣 b人 南鄉遣 c人 
"""

"""
Suppose there are 8758 suan (units of population or resources) in the northern district, 7236 suan in the western district, and 8356 suan in the southern district.
In total, 378 people are to be conscripted for labor.
Question: how many people are conscripted from each district, proportional to their suan?

The procedure says: Place the suan numbers for each district in a line.
Add them together to form the divisor.
Multiply the total number of conscripted people by the suan numbers that have not been added together, forming the dividend for each district.
Divide each dividend by the divisor to obtain the number of conscripted people for each district.

The answer says: the northern district sends *a* people, the western district sends *b* people, and the southern district sends *c* people.
"""

# 北鄉算八千七百五十八
北鄉 = 8758

# 西鄉算七千二百三十六
西鄉 = 7236

# 南鄉算八千三百五十六
南鄉 = 8356

# 三鄉發傜三百七十八人
總傜 = 378

# 衰副并為法
法 = 北鄉 + 西鄉 + 南鄉

# 以所發傜人數乘未并者各自為實
北實 = 總傜 * 北鄉
西實 = 總傜 * 西鄉
南實 = 總傜 * 南鄉

# 實如法得一人
a = Fraction(北實, 法)
b = Fraction(西實, 法)
c = Fraction(南實, 法)
"""
"""
