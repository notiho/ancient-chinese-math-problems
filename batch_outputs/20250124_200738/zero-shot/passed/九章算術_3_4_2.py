"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing 378 people among three regions (北鄉, 西鄉, 南鄉) in proportion to their respective population counts. The populations are given as follows:

- 北鄉: 8758
- 西鄉: 7236
- 南鄉: 8356

The solution involves proportional distribution based on the populations. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Population counts
north_population = 8758
west_population = 7236
south_population = 8356

# Total population
total_population = north_population + west_population + south_population

# Total people to distribute
total_people = 378

# Calculate the number of people for each region
a = Fraction(north_population * total_people, total_population)
b = Fraction(west_population * total_people, total_population)
c = Fraction(south_population * total_people, total_population)

# Results
a, b, c
#----- content ends here -----


"""


The variables `a`, `b`, and `c` represent the number of people sent to 北鄉, 西鄉, and 南鄉, respectively, as fractions.
"""


"""
"""
