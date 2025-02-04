"""
今有稟粟五斛，五人分之，欲令三人得三，二人得二。問︰各幾何？
術曰：置三人，人三；二人，人二，為列衰。副并為法。以五斛乘未并者，各自為實。實如法得一斛。
荅曰： a人 ，人得 b斛 。 c人 ，人得 d斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing 5斛 (hu) of grain among 5 people such that 3 people get 3斛 and 2 people get 2斛. Let's compute the values of the unknowns `a`, `b`, `c`, and `d`.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total grain in hu
total_grain = 5  # 5斛

# Number of people in each group
group1_people = 3  # 3 people
group2_people = 2  # 2 people

# Total grain assigned to each group
group1_grain = 3  # 3斛
group2_grain = 2  # 2斛

# Grain per person in each group
b = Fraction(group1_grain, group1_people)  # Grain per person in group 1
d = Fraction(group2_grain, group2_people)  # Grain per person in group 2

# Assigning the number of people in each group
a = group1_people  # Number of people in group 1
c = group2_people  # Number of people in group 2

# Results
print(f"a = {a}, b = {b}斛, c = {c}, d = {d}斛")
#----- content ends here -----


"""


### Explanation:
1. `a` is the number of people in the first group, which is 3.
2. `b` is the amount of grain each person in the first group gets, calculated as `3斛 / 3人 = 1斛`.
3. `c` is the number of people in the second group, which is 2.
4. `d` is the amount of grain each person in the second group gets, calculated as `2斛 / 2人 = 1斛`.

### Output:
```
a = 3, b = 1斛, c = 2, d = 1斛
```
"""


"""
Variable 'b' has wrong value. Expected: 15/13, Actual: 1
Variable 'd' has wrong value. Expected: 100/13, Actual: 1"""
