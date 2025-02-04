"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing 378 people among three regions (北鄉, 西鄉, 南鄉) in proportion to their respective populations. The populations are given as follows:

- 北鄉: 8758
- 西鄉: 7236
- 南鄉: 8356

The solution involves proportional distribution based on the populations. Let's compute the values of `a`, `b`, and `c` using Python.


"""

#----- content starts here -----

from fractions import Fraction

# Given data
population_north = 8758  # 北鄉
population_west = 7236   # 西鄉
population_south = 8356  # 南鄉
total_people = 378       # Total people to distribute

# Total population
total_population = population_north + population_west + population_south

# Calculate the number of people sent to each region
a = Fraction(population_north, total_population) * total_people  # 北鄉遣 a人
b = Fraction(population_west, total_population) * total_people   # 西鄉遣 b人
c = Fraction(population_south, total_population) * total_people  # 南鄉遣 c人

# Results
a, b, c
#----- content ends here -----


"""


This code calculates the values of `a`, `b`, and `c` as fractions to ensure precision. The results represent the number of people sent to 北鄉, 西鄉, and 南鄉, respectively.
"""


"""
"""
