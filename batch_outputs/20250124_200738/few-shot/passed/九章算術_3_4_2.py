"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

#----- content starts here -----
"""
Suppose there are 8,758 suan (population count) in the northern district, 7,236 suan in the western district, and 8,356 suan in the southern district. In total, there are three districts, and 378 people are to be conscripted. 
It is desired to distribute the conscription proportionally based on the population count. 
Question: how many people are conscripted from each district?

The procedure says: Place the population counts in a sequence as the weights. Add them together to obtain the divisor. Multiply the total number of conscripted people by the unadded weights for each district, making each its own dividend. Divide the dividend by the divisor to obtain the number of conscripted people for each district.

Answer: The northern district sends *a* people, the western district sends *b* people, and the southern district sends *c* people.
"""

# 北鄉算八千七百五十八
北鄉算 = 8758

# 西鄉算七千二百三十六
西鄉算 = 7236

# 南鄉算八千三百五十六
南鄉算 = 8356

# 發傜三百七十八人
發傜人數 = 378

# 各置算數為列衰
算數列 = [北鄉算, 西鄉算, 南鄉算]

# 副并為法
法 = sum(算數列)

# 以所發傜人數乘未并者，各自為實
北鄉實 = 發傜人數 * 北鄉算
西鄉實 = 發傜人數 * 西鄉算
南鄉實 = 發傜人數 * 南鄉算

# 實如法得一人
a = Fraction(北鄉實, 法)
b = Fraction(西鄉實, 法)
c = Fraction(南鄉實, 法)#----- content ends here -----

"""
"""
