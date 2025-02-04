"""
今有一人一日矯矢五十，一人一日羽矢三十，一人一日筈矢十五。今令一人一日自矯、羽、筈，問︰成矢幾何？
術曰：矯矢五十，用徒一人。羽矢五十，用徒一人、太半人。筈矢五十，用徒三人、少半人。并之，得六人，以為法。以五十矢為實。實如法得一矢。
荅曰： a矢 。
"""

"""
To solve this problem, we need to calculate how many arrows ("矢") one person can produce in one day when they perform all three tasks (矯, 羽, 筈) themselves.

### Problem Breakdown:
1. **矯矢**: One person can produce 50 arrows in one day.
2. **羽矢**: One person and half another person (1.5 people) can produce 50 arrows in one day.
3. **筈矢**: Three people and half another person (3.5 people) can produce 50 arrows in one day.

We need to find how many arrows one person can produce in one day when they perform all three tasks.

### Solution:
Let the number of arrows one person can produce in one day be `a`. Using the given information, we can calculate `a` as follows:



### Explanation:
1. We calculate the total number of people required to produce 50 arrows for all tasks: `1 + 1.5 + 3.5 = 6`.
2. Since 50 arrows are produced by 6 people in one day, the number of arrows one person can produce in one day is `50 / 6`.

### Final Answer:

"""


from fractions import Fraction

# Total number of people required to produce 50 arrows for each task
矯_people = Fraction(1)  # 1 person for 矯矢
羽_people = Fraction(3, 2)  # 1.5 people for 羽矢
筈_people = Fraction(7, 2)  # 3.5 people for 筈矢

# Total people required to produce 50 arrows for all tasks
total_people = 矯_people + 羽_people + 筈_people

# Total arrows produced by one person in one day
a = Fraction(50) / total_people

# Output the result
a

a矢 = Fraction(50, 6)  # Simplified to Fraction(25, 3)


"""

"""


"""
"""
