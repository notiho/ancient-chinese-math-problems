"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

#----- content starts here -----
"""
Suppose there are 8,758 suan (population count) in the northern village, 7,236 suan in the western village, and 8,356 suan in the southern village. 
In total, there are three villages, and 378 people are to be conscripted for labor. 
It is desired to distribute the labor proportionally based on the population count of each village. 
Question: how many people are conscripted from each village?

The procedure says: Place the population counts of each village in a sequence of decreasing values. 
Add them together to obtain the divisor. 
Multiply the total number of conscripted people by the population count of each village (without adding them together), obtaining the dividend for each village. 
Divide each dividend by the divisor to obtain the number of conscripted people for each village.

Answer: the northern village sends *a* people, the western village sends *b* people, and the southern village sends *c* people.
"""

from fractions import Fraction

# Population counts for each village
北鄉算 = 8758
西鄉算 = 7236
南鄉算 = 8356

# Total number of people to be conscripted
發傜 = 378

# Add the population counts to get the divisor (法)
法 = 北鄉算 + 西鄉算 + 南鄉算

# Calculate the dividend (實) for each village
北鄉實 = 發傜 * 北鄉算
西鄉實 = 發傜 * 西鄉算
南鄉實 = 發傜 * 南鄉算

# Divide each dividend by the divisor to get the number of conscripted people
a = Fraction(北鄉實, 法)
b = Fraction(西鄉實, 法)
c = Fraction(南鄉實, 法)

# Results
a, b, c#----- content ends here -----

"""
"""
