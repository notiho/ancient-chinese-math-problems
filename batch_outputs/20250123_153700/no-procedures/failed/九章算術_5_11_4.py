"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
荅曰： a丈 。
"""

"""
This problem involves calculating the amount of work (measured in "person-work" or "人功") required to complete a task and distributing the workload among workers. Let's break it down step by step:

---

### Problem Breakdown:
1. **Autumn Workload**: The total workload is 300 chi (尺), which corresponds to 33,582 person-work (人功), with a remainder of 14 chi and 4 cun (寸).
2. **1,000 workers arrive first**: The question asks how much length (in zhang, 丈) these 1,000 workers should complete.

---

### Assumptions:
- 1 zhang = 10 chi.
- Work is distributed proportionally based on the number of workers and the total workload.

---

### Solution in Python:


"""


from fractions import Fraction

# Total workload in person-work
total_person_work = 33582 + Fraction(14, 10)  # 14 chi = 14/10 zhang

# Total length of the task in zhang
total_length = Fraction(300, 10)  # 300 chi = 30 zhang

# Work per unit length (person-work per zhang)
work_per_zhang = total_person_work / total_length

# Number of workers who arrive first
workers_first = 1000

# Length they should complete (in zhang)
a = workers_first / work_per_zhang

# Output the result
a


"""


---

### Explanation:
1. **Convert Units**: The total workload is converted into person-work and the total length into zhang.
2. **Work per Unit Length**: Calculate how much person-work is required per zhang of length.
3. **Distribute Work**: Divide the workload proportionally among the 1,000 workers to determine how much length they should complete.

---

### Final Answer:
The value of `a` (in zhang) will be the length that the 1,000 workers should complete.
"""


"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 150000/167917"""
