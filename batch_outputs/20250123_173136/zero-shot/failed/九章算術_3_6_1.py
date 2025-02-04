"""
今有稟粟五斛，五人分之，欲令三人得三，二人得二。問︰各幾何？
術曰：置三人，人三；二人，人二，為列衰。副并為法。以五斛乘未并者，各自為實。實如法得一斛。
荅曰： a人 ，人得 b斛 。 c人 ，人得 d斗 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. The problem involves dividing 5斛 (hu) of grain among 5 people such that 3 people get 3斛 and 2 people get 2斛. We will compute the values of the unknowns `a`, `b`, `c`, and `d`.

Here's the Python code:


"""


from fractions import Fraction

# Total grain in hu
total_grain = 5  # 5斛

# Number of people
total_people = 5  # 5 people

# Grain distribution
grain_for_three_people = 3  # 3斛 for 3 people
grain_for_two_people = 2  # 2斛 for 2 people

# Calculate how much each person in the group of 3 gets
b = Fraction(grain_for_three_people, 3)  # Each of the 3 people gets b斛

# Calculate how much each person in the group of 2 gets
d = Fraction(grain_for_two_people, 2)  # Each of the 2 people gets d斛

# Assign the number of people in each group
a = 3  # 3 people
c = 2  # 2 people

# Results
print(f"a = {a}, each person gets b = {b}斛")
print(f"c = {c}, each person gets d = {d}斛")


"""


### Explanation of the Code:
1. `total_grain` is the total amount of grain (5斛).
2. `grain_for_three_people` is the amount of grain allocated to 3 people (3斛).
3. `grain_for_two_people` is the amount of grain allocated to 2 people (2斛).
4. `b` is calculated as the grain per person in the group of 3: `3斛 ÷ 3 = 1斛`.
5. `d` is calculated as the grain per person in the group of 2: `2斛 ÷ 2 = 1斛`.
6. `a` is the number of people in the first group (3 people).
7. `c` is the number of people in the second group (2 people).

### Output:
```
a = 3, each person gets b = 1斛
c = 2, each person gets d = 1斛
```
"""


"""
Variable 'b' has wrong value. Expected: 15/13, Actual: 1
Variable 'd' has wrong value. Expected: 100/13, Actual: 1"""
