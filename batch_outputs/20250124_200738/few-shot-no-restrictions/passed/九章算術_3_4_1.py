"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

#----- content starts here -----
"""
Suppose there are three regions: the northern region has 8758 suan, the western region has 7236 suan, and the southern region has 8356 suan. 
In total, 378 people are to be conscripted for labor. 
It is desired to distribute the labor proportionally based on the suan numbers of each region.
Question: how many people are conscripted from each region?

The procedure says: Place the suan numbers of each region in a sequence as weights. 
Add them together to form the divisor. 
Multiply the total number of conscripted people by the suan numbers of each region (individually, without summing). 
Each product becomes a dividend. 
Divide each dividend by the divisor to obtain the number of conscripted people for each region.

Answer: the northern region sends *a* people, the western region sends *b* people, and the southern region sends *c* people.
"""

from fractions import Fraction

# 北鄉算數
北鄉算 = 8758

# 西鄉算數
西鄉算 = 7236

# 南鄉算數
南鄉算 = 8356

# 發傜人數
發傜 = 378

# 各置算數為列衰
算數列 = [北鄉算, 西鄉算, 南鄉算]

# 副并為法
法 = sum(算數列)

# 以所發傜人數乘未并者，各自為實
北鄉實 = 發傜 * 北鄉算
西鄉實 = 發傜 * 西鄉算
南鄉實 = 發傜 * 南鄉算

# 實如法得一人
a = Fraction(北鄉實, 法)
b = Fraction(西鄉實, 法)
c = Fraction(南鄉實, 法)

# Results
a, b, c#----- content ends here -----

"""
"""
