"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
荅曰： a丈 。
"""

"""
Suppose in autumn, the total work required is 300 chi (cubic units of earthwork). The total labor required is 33,582 person-units of work, with 14 chi and 4 cun remaining.

If 1,000 workers arrive first, how much length (in zhang) should they complete?

Answer: *a* zhang.
"""

# Total work in person-units
total_person_work = 33582

# Total length of the project in chi
total_length = 300

# Work per chi (person-units per chi)
work_per_chi = total_person_work / total_length

# Work completed by 1,000 workers in one day
work_by_1000_workers = 1000

# Length completed by 1,000 workers (in chi)
length_completed_in_chi = work_by_1000_workers / work_per_chi

# Convert chi to zhang (1 zhang = 10 chi)
a = Fraction(length_completed_in_chi, 10)

a
"""
Code error: both arguments should be Rational instances"""
