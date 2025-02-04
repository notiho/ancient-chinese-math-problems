"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

#----- content starts here -----
"""
Suppose there are 8,758 suan (population count) in the northern district, 7,236 suan in the western district, and 8,356 suan in the southern district. 
In total, there are three districts, and 378 people need to be conscripted. 
It is desired to distribute the conscription proportionally based on the population count of each district.

The procedure says: Place the population counts of each district in a sequence as the weights. 
Add them together to form the divisor. 
Multiply the total number of conscripted people by each individual population count (not yet summed), forming the dividend for each district. 
Divide each dividend by the divisor to obtain the number of conscripted people for each district.

Answer: The northern district sends *a* people, the western district sends *b* people, and the southern district sends *c* people.
"""

from fractions import Fraction

# Population counts for each district
北鄉 = 8758
西鄉 = 7236
南鄉 = 8356

# Total conscription
總傜 = 378

# Add all population counts to form the divisor
法 = 北鄉 + 西鄉 + 南鄉

# Calculate the conscription for each district
a = Fraction(總傜 * 北鄉, 法)
b = Fraction(總傜 * 西鄉, 法)
c = Fraction(總傜 * 南鄉, 法)

# Results
a, b, c#----- content ends here -----

"""
"""
