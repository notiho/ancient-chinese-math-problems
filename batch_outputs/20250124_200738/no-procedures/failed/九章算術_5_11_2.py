"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose in an autumn project, the total work is 300 chi, and it requires 33,582 person-days of labor. However, there is a shortfall of 14 chi and 4 cun.

If 1,000 workers arrive first, how much length of the project should they complete?

Answer: *a* zhang.
"""

# Total work in chi
total_work = 300

# Total person-days required
total_person_days = 33582

# Shortfall in chi (convert 14 chi 4 cun to chi)
shortfall = 14 + Fraction(4, 10)

# Effective total work after accounting for the shortfall
effective_work = total_work - shortfall

# Work completed per person-day (in chi)
work_per_person_day = effective_work / total_person_days

# Number of workers arriving first
workers = 1000

# Total work completed by the first group of workers
work_done_by_first_group = workers * work_per_person_day

# Convert the work done into zhang (1 zhang = 10 chi)
a = work_done_by_first_group / 10#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 4760/5597"""
