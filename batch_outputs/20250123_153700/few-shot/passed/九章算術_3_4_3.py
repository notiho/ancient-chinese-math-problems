"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

"""
Suppose there are 8,758 suan (population count) in the northern district, 7,236 suan in the western district, and 8,356 suan in the southern district. 
In total, there are three districts, and 378 people are to be conscripted. 
It is desired to distribute the conscription based on the population count of each district. 
Question: how many people are conscripted from each district?

The procedure says: Place the population counts of each district in a line as the decreasing sequence. 
Add them together to obtain the divisor. 
Multiply the total number of conscripted people by the unadded population counts of each district, making each its own dividend. 
Divide the dividend by the divisor to obtain the number of conscripted people for each district.

Answer: the northern district sends *a* people, the western district sends *b* people, and the southern district sends *c* people.
"""

# 北鄉算八千七百五十八
北鄉 = 8758

# 西鄉算七千二百三十六
西鄉 = 7236

# 南鄉算八千三百五十六
南鄉 = 8356

# 發傜三百七十八人
發傜 = 378

# 各置算數為列衰
算數 = [北鄉, 西鄉, 南鄉]

# 副并為法
法 = sum(算數)

# 以所發傜人數乘未并者，各自為實
實 = [發傜 * i for i in 算數]

# 實如法得一人
a, b, c = [Fraction(i, 法) for i in 實]
"""
"""
