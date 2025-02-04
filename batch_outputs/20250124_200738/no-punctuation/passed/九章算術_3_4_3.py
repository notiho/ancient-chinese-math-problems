"""
今有北鄉算八千七百五十八西鄉算七千二百三十六南鄉算八千三百五十六凡三鄉發傜三百七十八人欲以算數多少衰出之問各幾何
術曰各置算數為列衰副并為法以所發傜人數乘未并者各自為實實如法得一人
荅曰北鄉遣 a人 西鄉遣 b人 南鄉遣 c人 
"""

#----- content starts here -----
"""
Suppose there are 8758 suan (units of population or resources) in the northern district, 7236 suan in the western district, and 8356 suan in the southern district.
In total, 378 people are to be conscripted for labor.
It is desired to distribute the conscription proportionally based on the suan numbers of each district.
Question: how many people are conscripted from each district?

The procedure says: Place the suan numbers for each district in a line.
Add them together to form the divisor.
Multiply the total number of conscripted people by the suan numbers that have not been added together.
Each becomes its own dividend.
Divide each dividend by the divisor to obtain the number of conscripted people for each district.

Answer: the northern district sends *a* people, the western district sends *b* people, and the southern district sends *c* people.
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

# 以所發傜人數乘未并者，各自為實
實 = [發傜人數 * i for i in 算數]

# 實如法得一人
a, b, c = [Fraction(i, 法) for i in 實]#----- content ends here -----

"""
"""
