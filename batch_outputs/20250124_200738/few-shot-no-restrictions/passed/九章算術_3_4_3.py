"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

#----- content starts here -----
"""
Suppose there are 8,758 suan (population count) in the northern district, 7,236 suan in the western district, and 8,356 suan in the southern district. 
In total, there are three districts, and 378 people are to be drafted for labor. 
It is desired to distribute the labor based on the population count of each district. 
Question: how many people are drafted from each district?

The procedure says: Place the population counts of each district in a sequence of decreasing values. 
Add them together to form the divisor. 
Multiply the total number of people to be drafted by the population count of each district (before summing). 
Each becomes its own dividend. 
Divide the dividend by the divisor to obtain the number of people drafted from each district.

Answer: The northern district drafts *a* people, the western district drafts *b* people, and the southern district drafts *c* people.
"""

from fractions import Fraction

# Population counts for each district
北鄉算 = 8758
西鄉算 = 7236
南鄉算 = 8356

# Total labor to be drafted
發傜 = 378

# Add the population counts to form the divisor (法)
法 = 北鄉算 + 西鄉算 + 南鄉算

# Calculate the number of people drafted from each district
北鄉實 = 發傜 * 北鄉算
西鄉實 = 發傜 * 西鄉算
南鄉實 = 發傜 * 南鄉算

# Divide each by the divisor to get the number of people drafted
a = Fraction(北鄉實, 法)
b = Fraction(西鄉實, 法)
c = Fraction(南鄉實, 法)

# Results
a, b, c#----- content ends here -----

"""
"""
